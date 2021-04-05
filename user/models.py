from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254,null=True,blank=True)
    


# Create your models here.
