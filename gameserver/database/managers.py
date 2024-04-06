from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext

class PlayerManager(BaseUserManager):
    def _create_user(self, name, password, **extra_fields):
        if not name:
            raise ValueError(gettext('User must have a name.'))
        user = self.model(name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(name, password, **extra_fields)
    
    def create_superuser(self, name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(name, password, **extra_fields)
