from rest_framework import serializers
from core.models import Customer
from django.contrib.auth import get_user_model
from accounts.models import User


class UserCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'phone_number', 'first_name', 'last_name', 'is_staff']


class CustomerSerializer(serializers.ModelSerializer):
    user = UserCustomerSerializer(read_only=True)
    
    class Meta:
        model = Customer
        fields = ['id', 'user', 'age']
        

class CustomerCreateSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='user.phone_number')

    class Meta:
        model = Customer
        fields = ['id', 'phone_number', 'age']
        
    def create(self, validated_data):
        phone_number = validated_data['user']['phone_number']
        age = validated_data.get('age')
        user = User.objects.create_user(phone_number=phone_number)
        
        return Customer.objects.create(user=user, age=age)

        
# {'customer': {'user': {'phone_number': '09876543322'}}, 'age': 21}