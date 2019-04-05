from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime



def index(request):
    return render(request, 'index.html')



def about(request):
    return render(request, 'about.html')

def current_time(request):
    return HttpResponse('<h1>{}</h1>'.format(datetime.now()))

def current_time_plus(request, num):
    return HttpResponse('<h1>arg number: {}</h1>'.format(num))

def show_product(request, pk):
    return HttpResponse('<h1>{}</h1>'.format(pk))
