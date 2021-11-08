from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class WatchListPagination(PageNumberPagination):
    page_size = 3  # number of elements shown per page
    page_query_param = 'p'  # change query parameters for page navigation
    page_size_query_param = 'size'  # override page size query parameters
    max_page_size = 5  # maximum elements shown per page


class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5
