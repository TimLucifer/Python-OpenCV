# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import cv2


def detect():
    face_cascade = cv2.CascadeClassifier('D:\Python-OpenCV\cascades\haarcascade_fromtalface_default.xml')

    face_cascade.load('D:\Python-OpenCV\cascades\haarcascade_frontalface_default.xml')

    eye_cascade = cv2.CascadeClassifier('D:\Python-OpenCV\cascades\haarcascade_eye.xml')

    eye_cascade.load('D:\Python-OpenCV\cascades\haarcascade_eye.xml')

    camera = cv2.VideoCapture(0)

    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_color = frame[y:y+h, x:x+w]
            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, "", (ex + x, ey + y), font, 0.5, (11, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('camera', frame)
        if cv2.waitKey(1000 / 12) & 0xff == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    detect()





