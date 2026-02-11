from rest_framework import status
from rest_framework.response import Response
from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet
from core.serializers import OrderSerializer,OrderCreateSerializer
from core.models import OrderItem,Order



class OrderViewSet(ModelViewSet):
    queryset=Order.objects.all()

    def get_serializer_class(self):
        if self.request.method  == 'POST':
            pass
        return OrderSerializer
    def get_serializer_context(self):
        return {'request':self.request}
    def get_queryset(self):
        try:
            queryset=\
            Order.\
            objects.\
            select_related('customer__user').\
            prefetch_related(
                Prefetch(
                'items' 
                , queryset=OrderItem.objects.select_related('product')
            )
        ).all()
            if self.request.user.is_staff:
                return queryset
        
            return queryset.filter(customer__user_id=self.request.user.id)
        except Exception as e:
            return Order.objects.none()

    def create(self, request, *args, **kwargs):
        post_serializer=OrderCreateSerializer(data=request.data , context=self.get_serializer_context())
        if post_serializer.is_valid():
            created_order=post_serializer.save()
            serializer=OrderSerializer(created_order)
            return Response(serializer.data  , status=status.HTTP_200_OK)
        return Response(post_serializer.errors , status=status.HTTP_400_BAD_REQUEST)