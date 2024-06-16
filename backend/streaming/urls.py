from django.urls import path

from . import views

urlpatterns = [
    path("stream/", views.video_stream, name="stream"),
    path("video_feed/", views.video_feed, name="video_feed"),
    path("upload_frame", views.upload_frame, name="upload_frame"),
]
