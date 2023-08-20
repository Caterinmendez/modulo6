from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
#logica del usuario
class CustomUser(AbstractUser):
    cumpleanos = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True)
    occupation = models.CharField(max_length=100, blank=True)

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)



