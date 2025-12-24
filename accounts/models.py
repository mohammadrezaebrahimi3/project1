from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.utils import timezone
from core.validators import validate_phone_number
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=11,
                                    validators=[validate_phone_number],
                                    unique=True
                                    )
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    objects = UserManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    
