from django.shortcuts import render

# Create your views here.


def video_feed(request):
    pass


def video_stream(request):
    return render(request, "streaming/stream.html")
