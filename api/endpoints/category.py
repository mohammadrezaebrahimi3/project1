from django.urls import path
from api.views import (CategoryListApiView,
                       CategoryDetailApiView,
                       )

app_name = 'category'
urlpatterns = [
    path('', CategoryListApiView.as_view(), name='category_list'),
    path('<uuid:pk>/', CategoryDetailApiView.as_view(), name='category_detail')
]