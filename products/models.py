from distutils.command.upload import upload
from django.db import models

# Create your models here.
class ProductDetails (models.Model):
    productName = models.CharField(max_length=255, blank=True)
    productDescription = models.TextField(max_length=255, blank=True)
    productType = models.CharField(max_length=255, blank=True)
    productPrice = models.IntegerField()
    productImage = models.ImageField(upload_to = "image")    
    productKeyword = models.CharField(max_length=255, blank=True)
    productId = models.IntegerField(null=True, blank=True)
    

