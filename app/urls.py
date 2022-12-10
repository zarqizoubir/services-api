from django.urls import path

from . import views

urlpatterns = [
    path("gtts/add/", views.GttsCreate.as_view())
]
