import PySide2
from PySide2.QtCore import Qt, QPoint, QRect
from PySide2.QtGui import QScreen, QPalette
from PySide2.QtWidgets import *

from src.view.Content import Content
from src.view.Navbar import Navbar
from src.view.Sidebar import Sidebar
from src.view.TitleBar import Titlebar


class View(QWidget):

    GRIP_SIZE = 16

    titleBar: Titlebar
    mainContent: QWidget
    navBar: Navbar
    sideBar: Sidebar
    content: Content

    grips: []
    layout: QGridLayout

    def __init__(self,screen: QRect):
        super().__init__()
        self.initializeWidgets()
        self.initializeMainLayout(screen)
        self.initializeMainContentLayout()

    def initializeWidgets(self):
        self.titleBar = Titlebar()
        self.mainContent = QWidget()
        self.navBar = Navbar()
        self.sideBar = Sidebar()
        self.content = Content()

    def initializeMainContentLayout(self):
        self.layout = QGridLayout(self.mainContent)
        self.sideBar.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.content.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layout.addWidget(self.navBar, 0, 0, 1, 11)
        self.layout.addWidget(self.sideBar, 1, 0, 20, 1)
        self.layout.addWidget(self.content, 1, 1, 20, 10)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

    def initializeMainLayout(self,screen: QRect):
        self.setGeometry(screen)
        self.titleBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.mainContent.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layoutMain = QVBoxLayout(self)
        layoutMain.addWidget(self.titleBar)
        layoutMain.addWidget(self.mainContent)
        layoutMain.setContentsMargins(0, 0, 0, 0)
        layoutMain.setSpacing(0)
        self.setWindowFlag(Qt.FramelessWindowHint)
        #self.initializeResizeGrips()

    def initializeResizeGrips(self):
        self.grips = []
        for i in range(4):
            grip = QSizeGrip(self)
            grip.resize(self.GRIP_SIZE, self.GRIP_SIZE)
            grip.setStyleSheet("""
                        background-color: transparent; 
                """)
            self.grips.append(grip)
