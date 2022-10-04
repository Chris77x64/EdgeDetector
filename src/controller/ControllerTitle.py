from PySide2.QtCore import Qt, QPoint
from PySide2.QtWidgets import QApplication, QWidget

from src.controller import EdgeDetector
from src.view import View, TitleBar
from src.view.View import View


class ControllerTitle:

    expanded: bool
    oldPosition: QPoint
    view: View
    app: EdgeDetector

    def __init__(self, titleBar: TitleBar, app: EdgeDetector, view: View):
        self.expanded = False
        self.view = view
        self.app = app

        titleBar.closeBTN.clicked.connect(self.close)
        titleBar.minimizeBTN.clicked.connect(self.minimize)
        titleBar.maximizeBTN.clicked.connect(self.maximize)
        titleBar.mousePressEvent = self.mousePressEvent
        titleBar.mouseMoveEvent = self.mouseMoveEvent

    def close(self):
        self.app.terminate.emit()
        self.app.exit()

    def minimize(self):
        self.view.showMinimized()

    def maximize(self):
        if self.expanded:
            self.expanded = False
            self.view.showNormal()
        else:
            self.expanded = True
            self.view.showMaximized()

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self,event):
        delta = QPoint(event.globalPos()-self.oldPosition)
        newPosition = QPoint(self.view.x() + delta.x(),self.view.y()+delta.y())
        self.view.move(newPosition)
        self.oldPosition = event.globalPos()
