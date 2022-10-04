import numpy as np
from PySide2.QtCore import QRect, Qt, Signal
from PySide2.QtGui import QIcon, QScreen
from PySide2.QtWidgets import QApplication
import qtawesome as qta

from src.controller.ControllerContent import ControllerContent
from src.controller.ControllerNavbar import ControllerNavbar
from src.controller.ControllerSettings import ControllerSettings
from src.controller.ControllerSidebar import ControllerSidebar
from src.controller.ControllerTitle import ControllerTitle
from src.controller.ControllerView import ControllerView
from src.model.State import State
from src.thread.Thread import Thread
from src.view.View import View


class EdgeDetector(QApplication):
    ICON_STRING = 'ph.dice-four-bold'
    ICON_COLOR = 'red'

    view: View
    thread: Thread

    controllerTitle: ControllerTitle
    controllerView: ControllerView
    controllerSettings: ControllerSettings
    controllerSidebar: ControllerSidebar
    controllerContent: ControllerContent
    controllerNavbar: ControllerNavbar

    state = Signal(State)
    param = Signal(np.ndarray)
    play = Signal(bool)
    terminate = Signal()

    def __init__(self):
        super().__init__()

        self.state.emit(State.fourier)
        self.param.emit([])
        self.play.emit(False)

        self.view = View(self.calculateSize())
        self.initializeController()
        self.initializeThread()
        self.setTaskbarIcon()

        self.run()

    def initializeController(self):
        self.controllerTitle = ControllerTitle(self.view.titleBar, self, self.view)
        self.controllerView = ControllerView(self.view)
        self.controllerSettings = ControllerSettings(self.view.sideBar.settings, self.param)
        self.controllerSidebar = ControllerSidebar(self.view.sideBar, self)
        self.controllerContent = ControllerContent(self.view.content)
        self.controllerNavbar = ControllerNavbar(self.view.navBar, self.play, [])

    def initializeThread(self):
        self.thread = Thread(self.controllerContent,self.controllerNavbar,self.view.content)
        self.thread.startThread()

        self.state.connect(self.updateState)
        self.param.connect(self.updateParam)
        self.play.connect(self.updatePlay)
        self.terminate.connect(self.terminateThreads)

    def run(self):
        self.view.show()
        self.exec_()

    def setTaskbarIcon(self):
        icon = QIcon(qta.icon(self.ICON_STRING, color=self.ICON_COLOR))
        self.setWindowIcon(icon)

    def calculateSize(self):
        screen: QScreen = self.screens()[0]
        rect = screen.availableGeometry()
        x = rect.width() * 0.025
        y = rect.height() * 0.025
        width = rect.width() * 0.95
        height = rect.height() * 0.95
        return QRect(x, y, width, height)

    def setState(self, newState: State):
        self.state.emit(newState)

    def setParam(self, newParam: []):
        self.param.emit(newParam)

    def updateState(self, state):
        self.thread.captureWorker.state = state

    def updateParam(self, param):
        self.thread.captureWorker.param = param

    def updatePlay(selfs, play):
        selfs.thread.renderWorker.play = play

    def terminateThreads(self):
        self.thread.captureWorker.terminate = True
        self.thread.renderWorker.terminate = True
