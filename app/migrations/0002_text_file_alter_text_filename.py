# Generated by Django 4.0.8 on 2022-12-10 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='file',
            field=models.FileField(null=True, upload_to='files/%Y/%m/%d/%h/%m/'),
        ),
        migrations.AlterField(
            model_name='text',
            name='filename',
            field=models.CharField(max_length=1000),
        ),
    ]