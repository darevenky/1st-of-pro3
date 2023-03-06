from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def venkydare(request):
    return HttpResponse('<h1>venkydare</h1>')

def vinot(request):
    return HttpResponse('sambar daa...')