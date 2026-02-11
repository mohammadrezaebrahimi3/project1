from rest_framework import serializers
from core.models import Cart,CartItem,Product

class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','title','price']

class CartItemSerializer(serializers.ModelSerializer):
    product=CartProductSerializer()
    class Meta:
        model=CartItem
        fields=['id','product','quantity']
class AddCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=['product','quantity']

    def create(self, validated_data):
        cart=self.context['cart']
        product=validated_data.get('product')
        quantity=validated_data.get('quantity')

        try:
            cart_item=CartItem.objects.get(cart=cart , product_id=product.id )
            cart_item.quantity +=quantity
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item=CartItem.objects.create(cart=cart, **validated_data)
        self.instance=cart_item
        return self.instance 
       
class UpdateCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=['quantity']

class CartSerializer(serializers.ModelSerializer):
    items=CartItemSerializer(many=True,read_only=True)
    class Meta:
        model=Cart
        fields=['id','created','items']

