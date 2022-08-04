
from django.shortcuts import render
from products.models import ProductDetails
from products.serialize import pdSerializer
from products import serialize
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class ProductDetailsTables(APIView):
    def get (self, request):
        productDetailsObj = ProductDetails.objects.all()
        pdSerializerObj = pdSerializer(productDetailsObj,many=True) 
        return Response(pdSerializerObj.data)

    def post(self, request):
        pdSerializerObj = pdSerializer(data = request.data)
        if pdSerializerObj.is_valid():
            pdSerializerObj.save()
            return Response(200) 
        return Response(pdSerializerObj.errors)


class ProductsDetailsTablesUpdate (APIView):
    def post(self,request, productId):
        try : 
            productDetailsObj = ProductDetails.objects.get(productId = productId)
        except : 
            return Response('Not Found!')
        pdSerializerObj = pdSerializer (productDetailsObj, data = request.data)

        if pdSerializerObj.is_valid():
            pdSerializerObj.save()
            return Response (200)
        return Response (pdSerializerObj.errors)

class ProductsDetailsTablesDelete  (APIView):
    def post (self,request,productId):
        try : 
            productDetailsObj = ProductDetails.objects.get(productId = productId)

        except :
            return Response('Not Found!')
        productDetailsObj.delete() 
        return Response (200)



    




              

