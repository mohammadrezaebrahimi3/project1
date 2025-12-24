from django.urls import path,include


app_name= 'api'

urlpatterns=[
    path('category/', include('api.endpoints.category' , namespace='category')),
    path('customer/', include('api.endpoints.customer' , namespace='customer' )),
    path('product/', include('api.endpoints.product' , namespace='product' )),
    path('swagger/', include('api.endpoints.swagger')),
    path('cart/', include('api.endpoints.cart', namespace='cart'))
]
