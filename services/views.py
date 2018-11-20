from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Product,Customer
from services.serializers import ProductSerializers,CustomorSerializers


@api_view(['GET', 'POST'])
def product_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        product_obj = Product.objects.all()
        serializer = ProductSerializers(product_obj,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    elif request.method == 'POST':
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            kwargs = {
            		 "name":request.data['name'],
            		 "code":request.data['code']
            		 }
            Product.objects.create(**kwargs)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomourList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        custmour = Customer.objects.all()
        serializer = CustomorSerializers(custmour, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # request.data handles form data 'POST', 'PUT' and 'PATCH' 
        serializer = CustomorSerializers(data=request.data)
        if serializer.is_valid():
            kwargs = {
                      "name":request.data['name'],
                      "code":request.data['code']
                      }
            Customer.objects.create(**kwargs)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)