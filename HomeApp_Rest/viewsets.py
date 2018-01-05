from rest_framework import viewsets
from HomeApp_Rest.serializers import PhotoSerializer
from ComeHome.models import Photo
import random


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class RandPhotoViewSet(viewsets.ModelViewSet):
    AllPhotos = Photo.objects.all()
    # TODO get the first pk so we don't get a wrong one
    # or do a retry when the pk doesn't exist
    try:
        randNum = random.randrange(1, len(AllPhotos))
        Background = Photo.objects.get(pk=randNum)
    except:
        Background = Photo.objects.get(pk=len(AllPhotos))
    queryset = [Background]
    serializer_class = PhotoSerializer
