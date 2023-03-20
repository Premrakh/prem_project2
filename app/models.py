from django.db import models

# Create your models here.
class Buyer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(unique=True,max_length=254)
    password=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    gender=models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.email