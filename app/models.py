from django.db import models

# Create your models here.


class Text(models.Model):
    languages = (
        ('en', "english"),
        ('ar', "arabic"),
        ('fr', "french")
    )
    filename = models.CharField(max_length=1000)
    file = models.FileField(upload_to="files/%Y/%m/%d/%h/%m/", null=True,)
    language = models.CharField(max_length=200, choices=languages)
    text = models.TextField(blank=True)
