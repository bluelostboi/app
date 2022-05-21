from math import prod
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import InventorySerializer
from .models import Inventory

# Create your views here.


class InventoryView(APIView):
    def post(self,request):
        serializer  = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def inventory_search(request,product_name=None):
    if product_name:
        prodcuts = Inventory.objects.get(product_name=product_name)
        serializer  = InventorySerializer(prodcuts,many=True)
        return Response(serializer.data)
    prodcuts = Inventory.objects.all()
    serializer  = InventorySerializer(prodcuts,many=True)
    return Response(serializer.data)


class InventorySearchView(APIView):
    ...

    def get(self, request, product_name=None):
        if id:
            item = Inventory.objects.get(product_name=product_name)
            serializer = InventorySerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Inventory.objects.all()
        serializer = InventorySerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


class InventoryEditView(APIView):
    ...    
    def patch(self, request, product_name=None):
        item = Inventory.objects.get(product_name=product_name)
        serializer = InventorySerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

from django.shortcuts import get_object_or_404

class DeleteProductView(APIView):
    ...
    def delete(self, request,product_name=None):
        item = get_object_or_404(Inventory, product_name=product_name)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})