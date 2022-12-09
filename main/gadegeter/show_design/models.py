from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageFidld(upload_to='images/')



class Tag(models.Model):
    tagname = models.ChairField(max_length=100)


#class ImageTag(models.Model):
