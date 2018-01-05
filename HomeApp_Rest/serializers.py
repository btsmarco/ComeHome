from rest_framework import serializers
from ComeHome.models import Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('pk', 'image', 'Photographer', 'originalAddress')
