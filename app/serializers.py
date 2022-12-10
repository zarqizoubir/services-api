from rest_framework import serializers
from django.core.files.base import ContentFile

from . import models


class TextSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Text
        # exclude = ["file"]
        fields = "__all__"
