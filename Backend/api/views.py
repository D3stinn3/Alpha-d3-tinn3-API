from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def api_nyumbani(request, *args, **kwargs):
    return JsonResponse({"message": "Hi there!"})