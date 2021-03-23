from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

class adoptionOffsetLimitPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class questionnaireOffsetLimitPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class adoptionPageNumberPagination(PageNumberPagination):
    page_size = 2


class questionnairePageNumberPagination(PageNumberPagination):
    page_size = 2