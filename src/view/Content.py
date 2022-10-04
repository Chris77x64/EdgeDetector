from PySide2.QtCore import Qt, QRect, QSize, QPoint, Signal
from PySide2.QtGui import QPalette, QImage, qRgb, QPainter, QFont
from PySide2.QtWidgets import QWidget, QSizePolicy, QGridLayout
import numpy as np
import cv2 as cv

from src.model.Convolution2D import differenceOfGaussians, laplaceEdgeDetector
from src.model.Frame import Frame


class Content(QWidget):

    image2 = Signal(np.ndarray)

    image: np.ndarray
    imageQ: QImage

    def __init__(self):

        super().__init__()

        self.initializePalette()
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
#        self.resizeEvent = self.onResize

    def initializePalette(self):
        design = QPalette()
        design.setColor(QPalette.Background,Qt.black)
        self.setAutoFillBackground(True)
        self.setPalette(design)

    # def onResize(self,e):
    #     pass
    #     #print(self.rect())
