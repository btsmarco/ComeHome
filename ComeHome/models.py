from django.db import models
import uuid

def scramble_uploaded_fileName(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)

class Photo(models.Model):
    image = models.ImageField(upload_to=scramble_uploaded_fileName)
    Photographer = models.CharField(max_length=200)
    originalAddress = models.URLField(max_length=200)


# from django.db import models
# import uuid
#
# def scramble_uploaded_fileName(instance, filename):
#     extension = filename.split(".")[-1]
#     return "{}.{}".format(uuid.uuid4(), extension)
#
# class Photo(models.Model):
#     image = models.ImageField(upload_to=scramble_uploaded_fileName)
#     Photographer = models.CharField(max_length=200)
#     originalAddress = models.CharField(max_length=200)
