from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    
    def create_user(self, username, email, name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an Email Address'))

        email=self.normalize_email(email)
        user = self.model(username=username, email=email,name=name, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, name, password, **other_fields):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff')is not True:
            raise ValueError('superuser must be set to is_staff=True')
        
        if other_fields.get('is_superuser')is not True:
            raise ValueError('superuser must be set to is_superuser=True')


        user = self.create_user(username, email, name, password, **other_fields)
        
        return user