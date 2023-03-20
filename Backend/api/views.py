import json
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def api_nyumbani(request, *args, **kwargs):
    body = request.body
    try:
        data = json.loads
    except:
        pass
    print(data.keys)
    return JsonResponse({"message": "Hi there!"})