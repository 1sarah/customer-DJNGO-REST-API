from django.db import models
import uuid
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, UserManager
from pytz import timezone

# from django.contrib.postgres.fields import ArrayField

# Create your models here.
Code_regex = RegexValidator(
regex=r'^[0-9]{4}$',
message="Code must be an Interger of 4 digits!",
code=""

)

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name  = models.CharField(max_length=80)
    code = models.IntegerField(validators=[Code_regex])

   

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.CharField(max_length=80)
    amount = models.IntegerField()
    datetime = models.DateTimeField(auto_now=True)

class User(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    username=models.CharField(max_length=80,default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    token= models.TextField(default=False)
    objects =  UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return self.email 