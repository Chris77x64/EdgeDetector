from time import sleep

from PySide2.QtCore import QObject, Signal


class RenderWorker(QObject):

    RENDER_RATE = 0.01

    finished = Signal()
    progress = Signal()
    terminate: bool
    play: bool

    error = Signal(Exception, name="error")

    def __init__(self):
        super().__init__()
        self.play = True
        self.terminate = False

    def run(self):
        try:
            while True:
                sleep(self.RENDER_RATE)
                if self.terminate:
                    break
                if self.play:
                    self.progress.emit()
            self.finished.emit()
        except Exception as e:
            self.error.emit(e)

    def setPlay(self,playPause: bool):
        self.play = playPause

