from django.urls import path,include
from rest_framework_nested import routers
from api.views import ProductViewSet,CommentViewSet


app_name='product'

router=routers.DefaultRouter()

router.register('',
                ProductViewSet,
                basename='product')

product_router= routers.NestedDefaultRouter(router,
                                            '',
                                            lookup='product')  

product_router.register('comments',
                        CommentViewSet,
                        basename='product_comments') 



urlpatterns= [
    path(r'',include(router.urls)),
    path(r'', include(product_router.urls)),

]