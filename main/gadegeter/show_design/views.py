from django.shortcuts import render
from django.http import HttpResponse
from .models import Image,ImageTag,Tag, ImageUrl
from .form import FindForm, ImageForm
from django.shortcuts import redirect

def index(request):
    msg = "search words"
    form = FindForm()
    data = Image.objects.raw("select * from show_design_image")
    tags = Tag.objects.raw("select * from show_design_tag")
    title = "一覧"
    params = {
        'title' : title,
        'message': msg,
        'form' : form,
        'data' : data,
        'tags' : tags,
    }
    return render(request,'showdesign/index.html',params)

def find(request):
    if (request.method == "POST"):
        form = FindForm(request.POST)
        find = request.POST['find']
        msg = str(find)
        title = "検索結果"
        tags = Tag.objects.raw("select * from show_design_tag")
        urls = Tag.objects.raw("select * from show_design_imageurl inner join show_design_tag on show_design_imageurl.tagid = show_design_tag.tagid")
        # data = Image.objects.raw((f"select * from  show_design_imagetag left join show_design_image on show_design_imagetag.imageid = show_design_image.imageid left join show_design_tag on show_design_imagetag.tagid = show_design_tag.tagid left join show_design_imageurl on show_design_imagetag.imageid = show_design_imageurl.imageid where show_design_tag.tagname = '{msg}'"))
        data = Image.objects.raw((f"select * from  show_design_imagetag inner join show_design_image on show_design_imagetag.imageid = show_design_image.imageid inner join show_design_tag on show_design_imagetag.tagid = show_design_tag.tagid where show_design_tag.tagname = '{msg}'"))
    params = {
        'title' : title,
        'message': msg,
        'form':form,
        'data':data,
        'tags' : tags,
        'urls' : urls,
    }
    return render(request,'showdesign/find.html',params)

def create(request):
    form = ImageForm()
    context = {
        'imageForm': form,
    }

    return render(request,'showdesign/create.html', context)

def addImage(request):
    last_id = Image.objects.order_by('-id').first().id
    register_id = last_id+1
    if request.method == 'POST':
        request.FILES["image"].name = str(register_id) + ".png"
        imageForm = ImageForm(request.POST, request.FILES)
        if imageForm.is_valid():
            imageForm.save()
    return redirect('index')