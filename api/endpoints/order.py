from rest_framework import routers
from api.views import OrderViewSet

app_name='order'

router=routers.DefaultRouter()

router.register('' , OrderViewSet ,basename='order')

urlpatterns=router.urls


