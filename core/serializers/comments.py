from rest_framework import serializers
from core.models import Comments, Product
from django.contrib.auth import get_user_model
from django.utils import timezone

class CommentsSerializer(serializers.ModelSerializer):
    author=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Comments
        fields=['id','author','body','status']
        extra_kwargs={'status':{'read_only':True}}

    def get_author(self, data:Comments):
        if data.author:
            return data.author.last_name
        return None
    
    def create(self, validated_data):
        validated_data['date'] = timezone.now()        
        #getting pk from modelviewset
        request_user=self.context.get('request').user
        product_pk=self.context['product_pk']

        if not request_user.is_authenticated:
            raise serializers.ValidationError('you must sign up first')
        
        product_instance=Product.objects.get(pk=product_pk)
        
        return Comments.objects.create(product=product_instance,
                                       author=request_user,
                                       **validated_data)