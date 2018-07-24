"""
自定义分页器
"""
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class StandardResultsSetPagination(PageNumberPagination):
    """
    自定义结果集分页器
    """
    page_size = 30
    page_size_query_param = 'pageSize'
    page_query_param = 'currentPage'

    def get_paginated_response(self, data):
        return Response({
            'pagination': {
                'current': self.page.number,
                'pageSize': self.page.paginator.per_page,
                'total': self.page.paginator.count
            },
            'list': data,
        })
