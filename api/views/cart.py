from django.utils.functional import cached_property
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from core.models import Cart
from core.serializers import CartSerializer , CartItemSerializer,AddCartItemSerializer



class CartApiView(APIView):
    serializer_class=CartSerializer

    def get(self,request):
        cart=Cart.objects.all()
        serializer=self.serializer_class(cart,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartDetailApiView(APIView):
    serializer_class=CartSerializer

    @cached_property
    def cart(self):
        return get_object_or_404(Cart, pk=self.kwargs['pk'])
        
    def get(self,request,*args,**kwargs):
        serilizer=self.serializer_class(self.cart)
        return Response(serilizer.data, status=status.HTTP_200_OK)

    def delete(self,request,*args,**kwargs):
        self.cart.delete()
        return Response({'detail':'deleted'}, status=status.HTTP_204_NO_CONTENT)
    

class CartItemApiView(APIView):

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        return CartItemSerializer

    @cached_property
    def cart(self):
        return get_object_or_404(Cart, pk=self.kwargs['pk'])
    

    def get(self,request,*args,**kwargs):
        item=self.cart.items.select_related('product')
        serializer=self.get_serializer_class()(item, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    



    def post(self, request,*args,**kwargs):
        serializer=self.get_serializer_class()(data=request.data,context={'cart':self.cart})
        if serializer.is_valid():
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
     

