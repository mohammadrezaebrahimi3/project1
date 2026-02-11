from django.urls import path,include 
from api.views import CartApiView,CartDetailApiView,CartItemApiView,CartItemDetailApiView

app_name='cart'

urlpatterns=[
    path('', CartApiView.as_view(),name='cart_list'),
    path('<uuid:pk>',CartDetailApiView.as_view(), name='cart_detail' ),
    path('<uuid:pk>/items/', CartItemApiView.as_view() ,name='cart_items'),
    path('<uuid:pk>/items/<uuid:items_pk>/', CartItemDetailApiView.as_view(), name='cart_items_detail')

]