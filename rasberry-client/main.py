import time

import cv2
import requests
from picamera2 import Picamera2

cloud_server_url = "http://192.168.10.117:8000/upload_frame/"

picam2 = Picamera2()
picam2.start()

while True:
    frame = picam2.capture_array()
    _, buffer = cv2.imencode(".jpg", frame)
    response = requests.post(cloud_server_url, files={"frame": buffer.tobytes()})
    time.sleep(0.1)  # 10 FPS
