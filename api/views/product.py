from rest_framework.viewsets import ModelViewSet
from core.models import Product 
from core.serializers import ProductSerializer
from core.paginations import ProductPaginator


class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    pagination_class=ProductPaginator
