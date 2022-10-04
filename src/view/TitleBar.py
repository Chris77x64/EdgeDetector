from PySide2.QtCore import QSize, QEvent, Qt, QPoint
from PySide2.QtGui import QPalette, QFont, QColor
from PySide2.QtWidgets import QApplication, QLabel, QPushButton, QSizePolicy, QHBoxLayout, QWidget, QSpacerItem
import qtawesome as qta

from src.view import View


class Titlebar(QWidget):

    FONT = 'Courier'
    FONT_SIZE = '35'
    ICON_SIZE = 35

    ICON_MINIMIZE = 'msc.chrome-minimize'
    ICON_MAXIMIZE = 'msc.chrome-maximize'
    ICON_CLOSE = 'msc.chrome-close'

    COLOR_LABEl = 'white'

    def __init__(self):
        super().__init__()
        self.initializePalette()

        self.minimizeBTN = self.createButton(self.ICON_MINIMIZE,'green')
        self.maximizeBTN = self.createButton(self.ICON_MAXIMIZE,'yellow')
        self.closeBTN = self.createButton(self.ICON_CLOSE,'red')
        self.label = self.createLabel('Edge Detector')

        self.createLayout()

    def initializePalette(self):
        design = QPalette()
        design.setColor(QPalette.Background,Qt.black)
        self.setAutoFillBackground(True)
        self.setPalette(design)

    def createButton(self, iconString,color):
        button = QPushButton()
        button.setIcon(qta.icon(iconString, color=color))
        button.setIconSize(QSize(self.ICON_SIZE, self.ICON_SIZE))
        button.setStyleSheet('QPushButton {background-color: black}')
        return button

    def createLayout(self):
        layout = QHBoxLayout(self)
        spacer = QSpacerItem(1, 1, QSizePolicy.Expanding)
        layout.insertWidget(0, self.closeBTN)
        layout.insertWidget(1, self.maximizeBTN)
        layout.insertWidget(2, self.minimizeBTN)
        layout.addSpacerItem(spacer)
        layout.insertWidget(4, self.label)
        layout.addSpacerItem(spacer)

    def createLabel(self, text):
        label = QLabel(text)
        #label.setFont(QFont(self.FONT, self.FONT_SIZE,QFont.Bold))
        label.setStyleSheet('font-family: Courier '+self.FONT_SIZE+'px; font-size: '+self.FONT_SIZE+'px')
        labelPalette = QPalette()
        labelPalette.setColor(QPalette.Foreground, QColor(self.COLOR_LABEl))
        label.setPalette(labelPalette)
        return label