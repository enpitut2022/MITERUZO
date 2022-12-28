from django.db import models

# Create your models here.
class Image(models.Model):
    imageid = models.IntegerField(default = 0)
    image = models.ImageField(upload_to='media')


class Tag(models.Model):
    tagid = models.IntegerField(default = 0)
    tagname = models.CharField(max_length=100)


class ImageTag(models.Model):
    imageid = models.CharField(max_length=100)
    tagid = models.CharField(max_length=100)


class ImageUrl(models.Model):
    imageid = models.CharField(max_length=100)
    tagid = models.CharField(max_length=100)
    url = models.CharField(max_length=1000)

