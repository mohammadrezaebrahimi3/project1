from django.db import models
from .base import BaseModel
from django.contrib.auth import get_user_model
from .product import Product

class Comments(BaseModel):
    COMMENT_STATUS=[
        ('draft' , 'Draft'),
        ('approved' , 'Approved' ),
        ('notapproved' , 'NotApproved' )
    ]
    author=models.ForeignKey(get_user_model()
    ,on_delete=models.CASCADE
    ,related_name='comments')
# User.comments.all()

    product=models.ForeignKey(
        Product,
        on_delete=models.CASCADE
        ,related_name='comment'
    ) #Product.comments.all()
    body= models.TextField()
    status=models.CharField(max_length=15, choices=COMMENT_STATUS, default=[0][0])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author.first_name}, {self.author.last_name} wrote {self.body} and status is {self.status}'
    
