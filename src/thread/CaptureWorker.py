import numpy as np
from PySide2.QtCore import QObject, Signal
import cv2 as cv
from src.model.Convolution2D import laplaceEdgeDetector, sobelEdgeDetector, cannyEdgeDetector, differenceOfGaussians, \
    logEdgeDetector
from src.model.DiscreteFourier2D import powerSpectra
from src.model.Frame import Frame
from src.model.State import State


class CaptureWorker(QObject):

    RENDER_WIDTH = 1024
    RENDER_HEIGHT = 512

    state: State
    param: []
    terminate: bool

    finished = Signal()
    image = Signal(np.ndarray)

    error = Signal(Exception, name="error")

    def __init__(self, state: State, param: []):
        super().__init__()
        self.state = state
        self.param = param
        self.terminate = False

    def run(self):
        try:
            self.videoLoop()
            self.finished.emit()
        except Exception as e:
            self.error_ocurred.emit(e)

    def videoLoop(self):
        vid = cv.VideoCapture(0)

        while vid.isOpened():

            if self.terminate:
                break

            print('video gelesen')
            ret, frame = vid.read()

            if ret:
                data = Frame(frame, self.RENDER_WIDTH, self.RENDER_HEIGHT)
                image = self.calculateResult(data, self.state)
                self.image.emit(image)

        vid.release()
        cv.destroyAllWindows()

    def calculateResult(self, data, state: State):
        print('Test',data.greyScaleImage,data.greyScaleImage.shape)
        image = np.asarray(data.greyScaleImage,np.uint8)
        if not (image is None) and (len(self.param) > 0 or self.state == State.sobel or self.state == State.fourier):
            result : np.ndarray
            if state == State.fourier:
                result = powerSpectra(image)
            elif state == State.laplace:
                result = laplaceEdgeDetector(image, self.param[0])
            elif state == State.sobel:
                result = sobelEdgeDetector(image)
            elif state == State.canny:
                result = cannyEdgeDetector(image, self.param[0], self.param[1])
            elif state == State.dog:
                result = differenceOfGaussians(image, self.param[0], self.param[1], self.param[2])
            elif state == State.log:
                result = logEdgeDetector(image, self.param[0], self.param[1], self.param[2])
            print('result fertig berechnet',result.shape)
            return result
        else:
            return self.image
