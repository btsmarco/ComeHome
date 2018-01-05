from django.conf.urls import url, include
from rest_framework import routers
from .viewsets import PhotoViewSet, RandPhotoViewSet

# TODO research more about routers in rest_framework
router = routers.DefaultRouter()
router.register('Photos', PhotoViewSet, 'Photos')
router.register('RandPhoto', RandPhotoViewSet, 'RandPhotos')

urlpatterns = [
    url('', include(router.urls)),
]
