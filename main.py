import cv2
import time
import glob
import os
import threading
from emailing import send_email

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
status_list = []
count = 1
image_with_object = None

os.makedirs("images", exist_ok=True)

def clean_folder():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)

def send_email_threaded(image_path):
    def task():
        send_email(image_path)
        clean_folder()
    thread = threading.Thread(target=send_email, args=(image_path,))
    thread.daemon = True
    thread.start()

while True:
    status = 0
    check, frame = video.read()

    if not check or frame is None:
        print("ERROR: Lost camera feed.")
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, contour_check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        status = 1

    status_list.append(status)
    status_list = status_list[-2:]

    if len(status_list) == 2 and status_list[0] == 0 and status_list[1] == 1:
        cv2.imwrite(f"images/{count}.png", frame)
        image_with_object = f"images/{count}.png"
        count += 1
        if image_with_object:
            send_email_threaded(image_with_object)


    print(status_list)
    cv2.imshow("Video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()