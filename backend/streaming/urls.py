from django.urls import path

from . import views

urlpatterns = [
    path("stream/", views.video_stream, name="stream"),
]
