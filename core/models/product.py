from django.db import models
from .base  import BaseModel

class Product(BaseModel):
    title= models.CharField(max_length=127)
    slug=models.SlugField()
    category=models.ForeignKey('core.category', on_delete=models.CASCADE , related_name='products')
    price=models.FloatField()
    body=models.TextField()
    stash=models.PositiveIntegerField()
    active=models.BooleanField(default=True)


    def __str__(self):
        return f'{self.title}'
