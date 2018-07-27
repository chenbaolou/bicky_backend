"""
AP管理试图
"""
import json
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from ap.serializers import APTypeSerializer, APSerializer
from ap.models import APType, AP


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
