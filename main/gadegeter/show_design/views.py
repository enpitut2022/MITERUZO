from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,ImageTag,Tag

def index(request):
    data = Image.objects.all()
    params = {
        'data':data,
    }
    return render(request,'showdesign/index.html',params)
# Create your views here.
