from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from core.paginations import CustomerPaginator
from core.serializers import CustomerSerializer,CustomerCreateSerializer
from core.models import Customer



class CustomerListApiView(ListCreateAPIView):
    queryset=Customer.objects.select_related('user').all()
    serializer_class=CustomerSerializer
    pagination_class=CustomerPaginator
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CustomerCreateSerializer
        return CustomerSerializer

class CustomerDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset=Customer.objects.select_related('user').all()
    lookup_url_kwarg='pk'
    serializer_class=CustomerSerializer
    