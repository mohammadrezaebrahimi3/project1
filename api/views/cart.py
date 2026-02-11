from django.utils.functional import cached_property
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from core.models import Cart,CartItem
from core.serializers import ( CartSerializer ,
                               CartItemSerializer,
                               AddCartItemSerializer,
                               UpdateCartItemSerializer )



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

    def cart_item(self):
        return get_object_or_404(
            CartItem,
            pk=self.kwargs['items_pk']
        )
    

    @cached_property
    def cart(self):
        return get_object_or_404(Cart, pk=self.kwargs['pk'])
        
    def get(self,request,*args,**kwargs):
        serilizer=self.serializer_class(self.cart)
        return Response(serilizer.data, status=status.HTTP_200_OK)

    def delete(self,request,*args,**kwargs):
        self.cart.delete()
        if self.cart.DoesNotExist():
            self.cart_item.delete()
            return Response({'message':'deleted'})
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
     

class CartItemDetailApiView(APIView):
        
    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer
    

    @cached_property
    def cart_item(self):
        return get_object_or_404(
            CartItem,
            cart__pk=self.kwargs['pk'],
            pk=self.kwargs['items_pk']
        )
    
    def get(self ,request , *args , **kwargs ):
        serializer=self.get_serializer_class()(self.cart_item)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def patch(self,request,*args,**kwargs):
        serializer=self.get_serializer_class()(self.cart_item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data ,status=status.HTTP_200_OK)
    def delete(self,request,*args,**kwargs):
        self.cart_item.delete()
        return Response({'message':'deleted'})