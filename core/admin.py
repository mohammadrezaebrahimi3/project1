from django.contrib import admin
from core.models import Category,Product,Cart,CartItem,Order,OrderItem


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)


class OrderItemTabular(admin.TabularInline):
    model=OrderItem
    extra=1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['customer', 'status' , 'created']
    inlines=[
        OrderItemTabular
    ]

