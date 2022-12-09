from django.contrib import admin
from .models import Image,ImageTag,Tag

# Register your models here.
admin.site.register(Image)
admin.site.register(ImageTag)
admin.site.register(Tag)

