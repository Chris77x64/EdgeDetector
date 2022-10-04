import PySide2
from PySide2.QtCore import Qt, QObject, QEvent, Signal, QRect
from PySide2.QtGui import QMouseEvent
from PySide2.QtWidgets import QMainWindow, QSizeGrip

from src.view.View import View


class ControllerView():

    view: View
    isResizing:bool


    def __init__(self, view: View):
        self.view = view

        #view.resizeEvent = self.resizeEvent
        self.isResizing = False

    # def resizeEvent(self, event):
    #     self.isResizing = True
    #     QMainWindow.resizeEvent(self.view, event)
    #     rect = self.view.rect()
    #     self.view.grips[1].move(rect.right() - self.view.GRIP_SIZE, 0)
    #     self.view.grips[2].move(
    #         rect.right() - self.view.GRIP_SIZE, rect.bottom() - self.view.GRIP_SIZE)
    #     self.view.grips[3].move(0, rect.bottom() - self.view.GRIP_SIZE)
    #     self.view.updateGeometry()
    #     self.view.content.updateGeometry()


    def eventFilter(self,obj: QObject, event: QEvent):
        #print(obj,event)
        # if obj.__class__ == QSizeGrip: #and event.type() == QEvent.MouseButtonRelease:
        #     #t = event.__class__ = QMouseEvent
        #     print('GRIIIPPPP',event.type(),obj)
        # print(obj)
        # if event.type() == QEvent.MouseButtonRelease:
        #     print(event,obj)
        #     #or event.type() == QEvent.NonClientAreaMouseButtonRelease:
        # #if event.type() == QEvent.Resize:
        #  #   print('resize done')
        # return True

       # print(event.type())
        #if(resizeEvent)
        #if event == Qt.Core.QEvent.MouseButtonRelease or event is Qt.Core.QEvent.Non :
           # NonClientAreaMouseButtonRelease)) {
        pass
