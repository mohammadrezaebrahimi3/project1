from django.contrib import admin
from core.models import Category,Product,Cart,CartItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)


