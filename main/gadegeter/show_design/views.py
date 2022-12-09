from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = Friend
    return HttpResponse("Hello Django!!")

# Create your views here.
