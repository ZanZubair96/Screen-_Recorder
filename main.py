from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
from datetime import datetime

# Get the width and Height of our system using the win32api package
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

# it enables the video recording ability
rec = cv2.VideoWriter_fourcc('m','p','4','v')
captured_video = cv2.VideoWriter('output.mp4', rec, 20.0, (width, height))

# Time Stamp to store the recorded files dynamically
time_stamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'


while True:
    # grap the screen resolution and make it dynamic according to out monitor size
    img = ImageGrab.grab(bbox=(0, 0, width, height))

    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

    # Real work begins here
    cv2.imshow('Screen capture', img_final)
    captured_video.write(img_final)

    print("Please press the q to stop the recording")
    if cv2.waitKey(10) == ord('q'):
        break

