import json
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializer


# Create your views here.
@api_view(["GET", "POST"])
def api_nyumbani(request, *args, **kwargs):
    body_data = request.data
    if request.method == "GET":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
    
    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            print(instance)
            return Response(serializer.data)
    """try:
        # turning json loads into python dicts
        data = {}
        data = json.loads(body)
        print(data)
    except:
        pass
    print(data)
    
    data["headers"] = dict(request.headers)
    return JsonResponse(data)"""