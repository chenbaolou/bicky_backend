"""
AP管理试图
"""
import json
import os
import time
import operator
import xlrd
from xlwt import Workbook
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from ap.serializers import APTypeSerializer, APSerializer
from ap.models import APType, AP
from group.models import Group

# excel表头定义
excel_title = ('apIndex', 'basemac', 'typeName', 'groupName', 'location', 'apMemo')


class APTypeList(generics.ListAPIView):
    """
    AP设备类型列表视图
    """
    queryset = APType.objects.all()
    pagination_class = None
    serializer_class = APTypeSerializer


class APList(generics.ListCreateAPIView):
    """
    AP列表视图，包括创建和过滤功能
    """
    queryset = AP.objects.all().order_by('apIndex')
    serializer_class = APSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('apname', 'basemac',)

    def perform_create(self, serializer):
        serializer.save(apType=APType.objects.get(apType=self.request.data.get('apType')))


class APDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    AP详情视图
    """
    queryset = AP.objects.all()
    serializer_class = APSerializer

    def perform_update(self, serializer):
        ap_type = self.request.data.get('apType')
        if ap_type is None:
            serializer.save()
        else:
            serializer.save(apType=APType.objects.get(apType=ap_type))


def check_ap_unique(request):
    """
    检查AP名称和MAC地址是否存在重复
    参数: apname/basemac, [apIndex]
    """
    ap_index = request.GET.get('apIndex', default=None)
    apname = request.GET.get('apname', default=None)
    basemac = request.GET.get('basemac', default=None)
    kwargs = {}
    if apname is not None:
        kwargs['apname'] = apname
    if basemac is not None:
        kwargs['basemac'] = basemac
    count = AP.objects.exclude(apIndex=ap_index).filter(**kwargs).count()
    return JsonResponse({"count": count})


def batch(request):
    """
    批量操作:
    1.批量删除
    """
    ids = json.loads(request.body).get('delete')
    if ids is not None:
        ids = ids.split(",")
    affected_rows = AP.objects.filter(apIndex__in=ids).delete()[0]
    return JsonResponse({"affectedRows": affected_rows})


def value_tostring(val):
    val = val.value
    if isinstance(val, (int, float)):
        return str(int(val))
    else:
        return val


def batch_import_ap(request):
    """
    批量导入AP
    :param request:
    :return:
    """
    execel_file = os.path.join(settings.TEMP_PATH, request.POST.get('fileName'))
    import_ret = dict({
        'insert': 0,
        'update': 0,
        'error': 0,
        'formatError': 0
    })
    try:
        data = xlrd.open_workbook(execel_file)
        table = data.sheets()[0]
        title = tuple(map(lambda x: x.value, table.row(0)))
        if not operator.eq(excel_title, title):
            raise AttributeError('excel title is not valid')
    except Exception as e:
        # os.remove(execel_file)
        return JsonResponse({'success': False,'errmsg': str(e)})

    for idx in range(1, table.nrows):
        try:
            row_value = tuple(map(value_tostring, table.row(idx)))
            row_dict = dict(zip(title, row_value))
        except Exception:
            import_ret['formatError'] = import_ret['formatError'] + 1
            continue

        try:
            # AP已存在
            ap_obj = AP.objects.get(basemac=row_dict['basemac'])
            ap_obj.location = row_dict['location']
            ap_obj.apMemo = row_dict['apMemo']
            ap_obj.save()
            import_ret['update'] = import_ret['update'] + 1
        except AP.DoesNotExist:
            try:
                # AP不存在, 但是apIndex已被使用
                AP.objects.get(apIndex=row_dict['apIndex'])
                try:
                    AP.objects.create(basemac=row_dict['basemac'],
                                      apname=row_dict['basemac'],
                                      apType=APType.objects.get(typeName=row_dict['typeName']),
                                      group=Group.objects.get(groupName=row_dict['groupName']),
                                      location=row_dict['location'],
                                      apMemo=row_dict['apMemo'])
                    import_ret['insert'] = import_ret['insert'] + 1
                except (Group.DoesNotExist, APType.DoesNotExist, Exception):
                    # 插入失败
                    import_ret['error'] = import_ret['error'] + 1

            except AP.DoesNotExist:
                # AP不存在, apIndex也没被使用
                try:
                    AP.objects.create(apIndex=row_dict['apIndex'],
                                      basemac=row_dict['basemac'],
                                      apname=row_dict['basemac'],
                                      apType=APType.objects.get(typeName=row_dict['typeName']),
                                      group=Group.objects.get(groupName=row_dict['groupName']),
                                      location=row_dict['location'],
                                      apMemo=row_dict['apMemo'])
                except (Group.DoesNotExist, APType.DoesNotExist, Exception) as e:
                    # 插入失败
                    import_ret['error'] = import_ret['error'] + 1

    return JsonResponse({'success': True, 'data': import_ret})


def export_ap(request):
    ap_list = AP.objects.filter(ap_flag=0).order_by('apIndex')
    work_book = Workbook()
    sheet = work_book.add_sheet('sheet1')

    # 设置表头
    for idx in range(len(excel_title)):
        sheet.write(0, idx, excel_title[idx])

    # 设置列宽
    sheet.col(0).width = 256 * 10
    sheet.col(1).width = 256 * 24
    sheet.col(2).width = 256 * 24
    sheet.col(3).width = 256 * 24
    sheet.col(4).width = 256 * 24
    sheet.col(5).width = 256 * 24

    excel_row = 1
    for obj in ap_list:
        sheet.write(excel_row, 0, obj.apIndex)
        sheet.write(excel_row, 1, obj.basemac)
        sheet.write(excel_row, 2, obj.apType.typeName)
        sheet.write(excel_row, 3, obj.group.groupName)
        sheet.write(excel_row, 4, obj.location)
        sheet.write(excel_row, 5, obj.apMemo)
        excel_row += 1

    export_file_name = 'APList-%s.xlsx' % (time.strftime("%Y%m%d%H%I%S", time.localtime(time.time())))
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=' + export_file_name
    work_book.save(response)

    return response


