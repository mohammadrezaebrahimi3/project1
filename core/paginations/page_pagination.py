from rest_framework.pagination import PageNumberPagination

class CustomerPaginator(PageNumberPagination):
    page_size = 3

class ProductPaginator(PageNumberPagination):
    page_size=3