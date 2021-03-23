from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class questionnaireOffsetLimitPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class questionnairePageNumberPagination(PageNumberPagination):
    page_size = 2