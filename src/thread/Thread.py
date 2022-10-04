from PySide2.QtCore import QThread, Qt

from src.controller.ControllerContent import ControllerContent
from src.controller.ControllerNavbar import ControllerNavbar
from src.model.State import State
from src.thread.CaptureWorker import CaptureWorker
from src.thread.RenderWorker import RenderWorker
from src.view.Content import Content


class Thread:
    captureWorker: CaptureWorker
    renderWorker: RenderWorker

    threadCapture: QThread
    threadRender: QThread

    controllerContent: ControllerContent
    controllerNavbar : ControllerNavbar
    content : Content

    def __init__(self, controllerContent: ControllerContent, controllerNavbar: ControllerNavbar, content: Content):
        self.threadCapture = QThread()
        self.threadRender = QThread()

        self.captureWorker = CaptureWorker(State.fourier, [])
        self.renderWorker = RenderWorker()

        self.controllerContent = controllerContent
        self.controllerNavbar = controllerNavbar
        self.content = content

    def startThread(self):
        self.captureWorker.moveToThread(self.threadCapture)
        self.renderWorker.moveToThread(self.threadRender)

        self.threadCapture.started.connect(self.captureWorker.run)
        self.threadRender.started.connect(self.renderWorker.run)

        self.captureWorker.image.connect(self.updateImage, Qt.QueuedConnection)
        self.renderWorker.progress.connect(self.updateContent, Qt.QueuedConnection)

        self.captureWorker.error.connect(self.printError)
        self.renderWorker.error.connect(self.printError)

        self.threadCapture.start()
        self.threadRender.start()

    def updateImage(self, x):
        self.controllerContent.content.image = x
        self.controllerNavbar.image = x
        self.content.image = x

    def updateContent(self):
        self.controllerContent.ready = True
        self.controllerContent.content.repaint()

    def printError(self, exception):
        print(exception)
