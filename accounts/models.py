from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):   
    PATIENT = 'patient'
    DOCTOR = 'doctor'
    USER_TYPE_CHOICES = [
        (PATIENT, 'Patient'),
        (DOCTOR, 'Doctor'),
    ]
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    name =  models.CharField(max_length=300, blank=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default=PATIENT)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','name']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.username
    


