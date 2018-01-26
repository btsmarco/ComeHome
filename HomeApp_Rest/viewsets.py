from rest_framework import viewsets
from HomeApp_Rest.serializers import PhotoSerializer
from ComeHome.models import Photo
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control
import random

class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class RandPhotoViewSet(viewsets.ModelViewSet):
    queryset = []
    serializer_class = PhotoSerializer

    def __init__(self, *args, **kwargs):
        ImagePhotosList = Photo.objects.values_list('image', flat=True)
        pkPhotoList = Photo.objects.values_list('pk', flat=True)

        randNum = random.randrange(1, len(pkPhotoList))

        Background = {}
        for index, p in enumerate(pkPhotoList):
            if index == randNum:
                Background = Photo.objects.get(pk=p)
                break

        self.queryset = [Background]
        queryset = self.queryset
        serializer_class = PhotoSerializer
