import os

from django.core.files.base import File

from rest_framework import generics
from rest_framework import status


from rest_framework.views import APIView
from rest_framework.request import HttpRequest
from rest_framework.response import Response

from . import serializers
from . import models

from gtts import gTTS


class GttsCreate(APIView):
    queryset = models.Text.objects.all()
    serializer = serializers.TextSerializer

    def post(self, request: HttpRequest):
        data = request.data
        serializer = self.serializer(data=data)
        if serializer.is_valid(raise_exception=True):
            name = data["filename"]
            text = data["text"]
            language = data["language"]
            file = gTTS(text=text, lang=language, slow=False)
            filepath = f"{name}.mp3"
            file.save(filepath)
            serializer.save()
            obj = self.queryset.filter(text=text).first()
            with open(filepath, "rb") as f:
                obj.file = File(f, name=name+".mp3")
                obj.save()
            os.remove(filepath)

            return Response({"file": f"{request.build_absolute_uri('/')}{obj.file.url}"}, status=status.HTTP_201_CREATED)

        return Response({"message": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)
