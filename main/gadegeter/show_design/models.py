from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='media')



class Tag(models.Model):
    tagname = models.CharField(max_length=100)
    tagname = models.CharField(max_length=100)


class ImageTag(models.Model):
    imageid = models.CharField(max_length=100)
    tagid = models.CharField(max_length=100)


