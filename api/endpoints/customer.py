from django.urls import path
from api.views import CustomerListApiView, CustomerDetailApiView


app_name = 'customer'

urlpatterns = [
    path('', CustomerListApiView.as_view(), name='customer_list'),
    path('<int:pk>/', CustomerDetailApiView.as_view(), name='customer_detail')
]