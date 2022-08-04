from itertools import product
from django.db.models import fields
from rest_framework import serializers
from products.models import ProductDetails

class pdSerializer (serializers.ModelSerializer):
    class Meta :
        model = ProductDetails

        fields = ('productName','productDescription','productImage','productPrice','productKeyword','productId')
        many = True
