from django.db import models
from core.models.base import BaseModel

class Order(BaseModel):
    STATUS_CHOICE=[
        ('unpaid' , 'unpaid'),
        ('paid' , 'paid'),
        ('canceled' , 'caneled')
    ]
    customer=models.ForeignKey('core.Customer',
                               on_delete=models.CASCADE,
                               related_name='orders')  
    status=models.CharField(max_length=8,
                             choices=STATUS_CHOICE,
                               default=STATUS_CHOICE[0][0])


    def __str__(self):
        return str(self.id)


class OrderItem(BaseModel):
    order=models.ForeignKey('Order' 
                            , on_delete=models.CASCADE,
                              related_name='items')
    product=models.ForeignKey('core.Product',
                               on_delete=models.CASCADE,
                                 related_name='ordered')
    quantity=models.PositiveSmallIntegerField(default=1)
    unit_price=models.DecimalField(max_digits=10,decimal_places=2)

    class Meta:
        unique_together=[['order', 'product']]

    def __str__(self):
        return f"{self.order_id}"

