import uuid
from django.db import models

from .base import BaseModel
from .product import Product


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)    


class CartItem(BaseModel):
    cart=models.ForeignKey(Cart,
                           on_delete=models.CASCADE,
                           related_name='items')#cart.items.all()
    product=models.ForeignKey(Product,
                              on_delete=models.CASCADE,
                              related_name='cart')
    quantity=models.PositiveSmallIntegerField()

    class Meta:
        unique_together=[['cart','product']]
