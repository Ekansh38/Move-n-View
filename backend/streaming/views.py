import cv2
from django.core.files.storage import default_storage
from django.http import JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

latest_frame_path = "latest_frame.jpg"


def upload_frame(request):
    if request.method == "POST":
        frame = request.FILES["frame"]
        with default_storage.open(latest_frame_path, "wb+") as destination:
            for chunk in frame.chunks():
                destination.write(chunk)
        return JsonResponse({"status": "frame received"})
    return JsonResponse({"status": "bad request"}, status=400)


def gen_frames():
    while True:
        with default_storage.open(latest_frame_path, "rb") as frame_file:
            frame = frame_file.read()
        yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


def video_feed(request):
    return StreamingHttpResponse(
        gen_frames(), content_type="multipart/x-mixed-replace; boundary=frame"
    )


def video_stream(request):
    return render(request, "streaming/stream.html")
