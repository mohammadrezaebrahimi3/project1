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
        fields=['cart','product','quantity']

    def create(self, validated_data):
        pass

class CartSerializer(serializers.ModelSerializer):
    items=CartItemSerializer(many=True,read_only=True)
    class Meta:
        model=Cart
        fields=['id','created','items']

