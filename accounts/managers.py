from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None):
        if not phone_number:
            raise ValidationError('There is No Phone Number')
        user = self.model(phone_number=phone_number)
        user.set_unusable_password()
        user.save(using=self._db)
        return user
    
    def create_superuser(self, phone_number, password=None):
        user = self.create_user(phone_number, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user