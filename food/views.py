from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    ctx = {'name': 'FAST FOOD', 'msg':'Django project'}
    return render(request, 'food/index.html',ctx)

def pizza(request):
    return render(request, 'food/pizza.html')
    
