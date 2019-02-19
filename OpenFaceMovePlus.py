# -*- coding:utf-8 -*-
import cv2
import os
# 导入模块


def generate():
    face_cascade = cv2.CascadeClassifier('D:\Python-OpenCV\cascades\haarcascade_fromtalface_default.xml')
    # 从绝对路径导入面部检测模块
    face_cascade.load('D:\Python-OpenCV\cascades\haarcascade_frontalface_default.xml')

    eye_cascade = cv2.CascadeClassifier('D:\Python-OpenCV\cascades\haarcascade_eye.xml')
    # 从绝对路径导入眼睛检测模块
    eye_cascade.load('D:\Python-OpenCV\cascades\haarcascade_eye.xml')

    camera = cv2.VideoCapture(0)
    # 视频捕获或调用视频，VideoCapture中参数决定，0：调用本机摄像头 路径：调用视频
    count = 0
    # 记录图片序号
    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            f = cv2.resize(gray[y:y+h, x:x+w], (200, 200))
            cv2.imwrite('D:/Python-OpenCV/at/jm/%s.pgm' % str(count), f)
            count += 1
        cv2.imshow("camera", frame)
        if cv2.waitKey(1000 / 12) & 0xff == ord("q"):
            break


# def read_images(path, sz=None):
#
#     c = 0
#     X, y = [], []
#     for dirname, dirnames, filename in os.walk(path):
#         for subdirname in dirnames:
#             subject_path = os.path.join(dirname, subdirname)
#             # subject_path in os.path.join(dirname, subdirname)
#             for filename in os.listdir(subject_path):
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    generate()



