from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'pageSize'
    page_query_param = 'page'
