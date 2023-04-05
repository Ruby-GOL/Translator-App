from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
#from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

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

class User(AbstractBaseUser, PermissionsMixin):
    # county choices
    KEN_COUNTIES =(
            (1,'Mombasa'),(2,'Kwale'),(3,'Kilifi'),(4,'Tana River'),(5,'Lamu'),(6,'Taita/Taveta'),(7,'Garissa'),(8,'Wajir'),
            (9,'Mandera'),(10,' Marsabit'),(11,'Isiolo'),(12,'Meru'),(13,'Tharaka-Nithi'),(14,'Embu'),
            (15,'Kitui'),(16,'Machakos'),(17,'Makueni'),(18,'Nyandarua'),(19,'Nyeri'),(20,'Kirinyaga'),
            (21,'Murang\'a'),(22,'Kiambu'),(23,'Turkana'),(24,'West Pokot'),(25,'Samburu'),(26,'Trans Nzoia'),(27,'Uasin Gishu'),
            (28,'Elgeyo/Marakwet'),(29,'Nandi'),(30,'Baringo'),(31,'Laikipia'),(32,'Nakuru'),(33,'Narok'),(34,'Kajiado'),
            (35,'Kericho'),(36,'Bomet'),(37,'Kakamega'),(38,'Vihiga'),(39,'Bungoma'),(40,'Busia'),
            (41,'Siaya'),(42,'Kisumu'),(43,'Homa Bay'),(44,'Migori'),(45,'Kisii'),(46,'Nyamira'),(47,'Nairobi City')
            )
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    name =  models.CharField(max_length=300, blank=True)
    county = models.CharField(max_length=3, choices=KEN_COUNTIES, blank=True)
    gender = models.CharField(max_length= 10)
    phone = models.TextField(null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','name']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.username

class Message(models.Model):
    topic =  models.CharField(max_length=50)
    content = models.TextField()
