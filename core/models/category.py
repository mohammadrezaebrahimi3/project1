from django.db import models
from .base import BaseModel


class Category(BaseModel):
    title = models.CharField(max_length=128)