import numpy as np
import cv2 as cv
import cv2
import os
import numpy
from scipy import ndimage
from skimage import io
"""randomBA = bytearray(os.urandom(120000))
flatNA = numpy.array(randomBA)

grayImage = flatNA.reshape(300, 400)
cv2.imwrite('Window.png', grayImage)

bgrImage = flatNA.reshape(100, 400, 3)
cv2.imwrite('Window.png', bgrImage)
image = cv2.imread('Window.png')
cv2.imwrite('MyPic.jpg', image)
"""
"""a = open("MyPic.jpg", "rb")
b = a.read()
a.close()
c = open("Windows.png", "wb")
c.write(b)
"""

"""img = cv.imread('Windows.png')
my_roi = img[0:100, 0:100]
img[300:400, 300:400] = my_roi
cv.imshow('Windows.png', img)
cv.waitKey(0)
"""
"""videoCapture = cv2.VideoCapture('MyInputVid.avi')
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter(
    'MyOutputVid.avi', cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'),
    fps, size)

success, frame = videoCapture.read()
while success:
    videoWriter.write(frame)
    success, frame = videoCapture.read()
"""
kernel_3x3 = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1]])

kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1,  1,  2,  1, -1],
                       [-1,  2,  4,  2, -1],
                       [-1,  1,  2,  1, -1],
                       [-1, -1, -1, -1, -1]])

img = io.imread("D:/OpenCv/Windows.png", as_gray=True)
k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5),

blueerd = cv2.GaussianBlur(img, (17, 17), 0)
g_hpf = img - blueerd

cv2.namedWindow('3x3', 0)
cv2.imshow("3x3", k3)
# cv2.namedWindow('5x5', 0)
# cv2.imshow("5x5", k5)
# cv2.namedWindow('g_hpf', g_hpf)
# cv2.imshow("g_hpf", g_hpf)
cv2.waitKey(0)
cv2.destroyAllWindows()







