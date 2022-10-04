from PySide2.QtCore import QThread

from src.controller import EdgeDetector
from src.thread.CaptureWorker import CaptureWorker
from src.model.State import State
from src.view.Content import Content
from src.view.Settings import Settings
from src.view.Sidebar import Sidebar


class ControllerSidebar:

    sideBar: Sidebar
    app: EdgeDetector

    def __init__(self,sideBar: Sidebar,app: EdgeDetector):

        self.sideBar = sideBar
        self.app = app
        self.sideBar.fourier.clicked.connect(self.fourierState)
        self.sideBar.sobel.clicked.connect(self.sobelState)
        self.sideBar.laplace.clicked.connect( self.laplaceState)
        self.sideBar.canny.clicked.connect(self.cannyState)
        self.sideBar.dog.clicked.connect(self.dogState)
        self.sideBar.log.clicked.connect(self.logState)

    def fourierState(self):
        self.update(State.fourier)

    def sobelState(self):
        self.update(State.sobel)

    def laplaceState(self):
        self.update(State.laplace)

    def cannyState(self):
        self.update(State.canny)

    def dogState(self):
        self.update(State.dog)

    def logState(self):
        self.update(State.log)

    def update(self,newState):
        self.app.play.emit(False)
        self.app.view.content.setParent(None)
        self.app.setState(newState)
        self.updateSetting(newState)
        self.updateParameter()
        self.updateContent()
        self.app.play.emit(True)

    def updateSetting(self,newState):
        self.sideBar.settings.clear()
        newSettings = Settings(newState)
        self.sideBar.settings = newSettings
        self.sideBar.updateLayout()
        self.app.controllerSettings.settings = newSettings
        self.app.controllerSettings.initializeChangeListener(self.sideBar.settings)

    def updateContent(self):
        newContent = Content()
        self.app.view.content = newContent
        self.app.controllerContent.updateContent(newContent)
        self.app.view.layout.addWidget(newContent, 1, 1, 20, 10)

    def updateParameter(self):
        initialParameter = [float(l.text()) for l in self.app.view.sideBar.settings.label]
        self.app.setParam(initialParameter)