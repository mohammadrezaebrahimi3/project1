from rest_framework.viewsets import ModelViewSet
from core.models import Comments
from core.serializers import CommentsSerializer
class CommentViewSet(ModelViewSet):
    serializer_class=CommentsSerializer
    
    def get_queryset(self):
        product_pk=self.kwargs['product_pk']
        return  Comments.objects.filter(product_id=product_pk).select_related('author')

    def get_serializer_context(self):
        response = super().get_serializer_context()
        response['product_pk']=self.kwargs['product_pk']
        return response
    
