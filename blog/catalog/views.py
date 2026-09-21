from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def my_view(request):
    return JsonResponse({'message': 'Hello!'})

def get_by_id(request, id: int):
    return JsonResponse({'data': 'id'})

def hello(request, name: str):
    return HttpResponse({f'<h5>hello, {name}</h5>'})

def hello2(request):
    return HttpResponse('Привет из hello2!')

def get_catalog(request):
    return render(request, 'catalog/catlist.html') 