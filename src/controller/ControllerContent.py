import numpy as np
from PySide2.QtCore import QPoint, QRect, Signal
from PySide2.QtGui import QPainter, QImage

from src.view.Content import Content

import cv2 as cv

class ControllerContent:

    content: Content
    ready: bool

    def __init__(self,content: Content):
        self.content = content
        self.setPaintEvent()
        self.ready = True


    def setPaintEvent(self):
        self.content.paintEvent = self.paintEvent

    def updateContent(self,content):
        self.content = content
        self.setPaintEvent()

    def paintEvent(self, paintEvent):
        if self.ready and hasattr(self.content, 'image') and not (self.content.image is None):
            rect = self.calculateSize()
            painter = QPainter(self.content)
            print('IMG', self.content.image,rect)
            image = cv.resize(self.content.image, (rect.width(), rect.height()), cv.INTER_NEAREST)

            if len(self.content.image.shape) == 3:
                imageQ = QImage(image, image.shape[1], image.shape[0], QImage.Format_BGR888)
                self.content.imageQ = imageQ
                painter.drawImage(QPoint(rect.x(), rect.y()), imageQ)
                painter.end()
            else:
                imageQ = QImage(image, image.shape[1], image.shape[0], QImage.Format_Grayscale8)
                self.content.imageQ = imageQ
                painter.drawImage(QPoint(rect.x(), rect.y()), imageQ)
                painter.end()

            self.ready = False


    def calculateSize(self):
        # print(  self.content.geometry().getRect(),       self.content.frameGeometry().getRect(),         self.content.rect() , self.content.normalGeometry().getRect())
        # rec = self.content.geometry().getRect()
        # return QRect(rec[0], rec[1], rec[2]-rec[0], rec[3]-rec[1])
        rect = self.content.rect()
        x = 110
        y = 10
        width = rect.width() * 0.90
        height = rect.height() * 0.90
        return QRect(x, y, width, height)

        # rect = self.content.rect()
        # x = rect.width() * 0.020
        # y = rect.height() * 0.025
        # width = rect.width() * 0.95
        # height = rect.height()  * 0.95
        # return QRect(x, y, width, height)
