from rest_framework import serializers
from .models import Imagee,Eimage

# create a serializer
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagee
        fields = "__all__"

class ISerializer(serializers.ModelSerializer):
    class Meta:
        model = Eimage
        fields = ['gray','thumbnail','medium','large']