from django.utils.functional  import cached_property
from django.http import HttpRequest
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from core.models import Category
from core.serializers import CategorySerializer

class CategoryListApiView(APIView):
    serializer_class = CategorySerializer
    
    
    def get(self, request):
        #interaction with database
        category = Category.objects.all()
        #interaction with serialzier
        serializer = self.serializer_class(category, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryDetailApiView(APIView):
    serializer_class = CategorySerializer
    
    @cached_property
    def category(self):
        return get_object_or_404(Category, pk=self.kwargs['pk'])
        
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        self.category.delete()
        return Response({'detail': 'deleted'}, status=status.HTTP_204_NO_CONTENT)
        
