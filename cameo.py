# -*- coding:utf-8 -*-
import cv2
from managers import WindowManager, CaptureManager
# 导入模块，从managers中导入窗口管理，捕获管理。
# import time
# 测试时添加


class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo',
                                            self.onKeypress)
        self._captureManager = CaptureManager(
            cv2.VideoCapture(0), self._windowManager, True)

    def run(self):
        self._windowManager.createdWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            if frame is not None:
                pass
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        if keycode == 32:
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9:
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:
            self._windowManager.destoryWindow()


if __name__ == '__main__':
    Cameo().run()




