from django.contrib.auth import get_user_model
from rest_framework import serializers 
from core.models import Order,OrderItem , Customer, Product,Cart,CartItem
from core.services import create_order_from_cart

class CustomerOrderSerializer(serializers.ModelSerializer):
    phone_number=serializers.CharField(source='user.phone_number')
    first_name=serializers.CharField(source='user.first_name')  
    last_name=serializers.CharField(source='user.last_name')  
    class Meta:
        model=Customer
        fields=[ 'phone_number','first_name','last_name', 'age']


class OrderItemProductserializer(serializers.ModelSerializer):
    class Meta:
        model=Product 
        fields=['id', 'title' , 'active']

class OrderItemSerializer(serializers.ModelSerializer):
    product=OrderItemProductserializer()
    class Meta:
        model=OrderItem
        fields=[ 'product', 'quantity', 'unit_price']


class OrderSerializer(serializers.ModelSerializer):
    customer=CustomerOrderSerializer()
    items=OrderItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model=Order
        fields=['id' , 'customer' , 'items' , 'status' , 'total_price' ]

    def get_total_price(self, obj):
        return sum(
            item.unit_price * item.quantity
            for item in obj.items.all()
        )
    
class OrderCreateSerializer(serializers.ModelSerializer):
    cart_id=serializers.UUIDField()

    def validate_cart_id(self,cart_id):
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError('there must be a cart')
        if CartItem.objects.filter(cart_id=cart_id).count() == 0:
            raise serializers.ValidationError('your cart must atleast contain a item')
        return cart_id
    def save(self , **kwargs):
        cart_id=self.validated_data['cart_id']
        user = self.context['user']
        return create_order_from_cart(cart_id=cart_id, user=user)




