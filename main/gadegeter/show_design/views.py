from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,ImageTag,Tag
from .form import FindForm

def index(request):
    data = Image.objects.all()
    params = {
        'data':data,
    }
    return render(request,'showdesign/index.html',params)

def find(request):
    if (request.method == "POST"):
        form = FindForm(request.POST)
        find = request.POST['find']
        msg = str(find)
        title = "検索結果"
        data = Image.objects.raw((f"select * from  show_design_imagetag inner join show_design_image on show_design_imagetag.imageid = show_design_image.imageid inner join show_design_tag on show_design_imagetag.tagid = show_design_tag.tagid where show_design_tag.tagname = '{msg}'"))
    else:
        msg = "search words"
        form = FindForm()
        #data = Image.objects.all()
        data = Image.objects.raw("select * from show_design_image")
        title = "一覧"
    params = {
        'title' : title,
        'message': msg,
        'form':form,
        'data':data,
    }
    return render(request,'showdesign/index.html',params)

# Create your views here.
