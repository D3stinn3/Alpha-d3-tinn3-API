import json
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def api_nyumbani(request, *args, **kwargs):
    body = request.body
    try:
        # turning json loads into python dicts
        data = {}
        data = json.loads(body)
        print(data)
    except:
        pass
    print(data)
    
    data["headers"] = dict(request.headers)
    return JsonResponse(data)