from PySide2.QtCore import Qt
from PySide2.QtGui import QPalette, QFont, QColor
from PySide2.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel

from src.model.State import State
from src.view.Settings import Settings


class Sidebar(QWidget):
    FONT = 'Courier'
    FONT_SIZE = 20
    COLOR_LABEl = 'white'

    fourier: QPushButton
    sobel: QPushButton
    laplace: QPushButton
    canny: QPushButton
    dog: QPushButton
    log: QPushButton

    layout: QVBoxLayout

    buttonGroup: QWidget
    settings: Settings
    spacer: QSpacerItem

    w: QLabel

    def __init__(self):
        super().__init__()
        self.initializePalette()

        self.labelAlgo = self.createLabel('Algorithm')
        self.labelAlgo.setAlignment(Qt.AlignHCenter)
        self.buttonGroup = self.createButtonGroup()
        self.settings = Settings(State.fourier)

        self.initializeLayout()

    def initializeLayout(self):
        self.layout = QVBoxLayout(self)
        self.layout.insertWidget(0, self.labelAlgo)
        self.layout.insertWidget(1, self.buttonGroup)
        self.spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addSpacerItem(self.spacer)
        self.layout.insertWidget(3, self.settings)
        # spacer2 = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # self.layout.addSpacerItem(spacer2)

    def updateLayout(self):
        self.layout.removeWidget(self.settings)
        self.layout.removeItem(self.spacer)
        self.layout.insertWidget(3, self.settings)
        self.layout.addSpacerItem(self.spacer)

    def createButtonGroup(self):
        group = QWidget()

        layout = QVBoxLayout(group)

        self.fourier = self.createButton('Fourier', 'red')
        self.sobel = self.createButton('Sobel', 'orange')
        self.laplace = self.createButton('Laplace', 'limegreen')
        self.canny = self.createButton('Canny', 'aqua')
        self.dog = self.createButton('Difference of Gaussian', 'deepskyblue')
        self.log = self.createButton('Laplacian of Gaussian', 'blue')
        self.w = self.createInvisibleLabel()

        layout.insertWidget(0, self.fourier)
        layout.insertWidget(1, self.sobel)
        layout.insertWidget(2, self.laplace)
        layout.insertWidget(3, self.canny)
        layout.insertWidget(4, self.dog)
        layout.insertWidget(5, self.log)
        layout.insertWidget(6,self.w)

        spacer = QSpacerItem(1, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addSpacerItem(spacer)
        return group

    def createInvisibleLabel(self):
        label = QLabel('Standard Deviation 1')
        label.setStyleSheet('font-family: Courier 20px; font-size: 25px')
        labelPalette = QPalette()
        labelPalette.setColor(QPalette.Foreground, QColor('black'))
        label.setPalette(labelPalette)
        return label

    def createLabel(self, text):
        label = QLabel(text)
        label.setFont(QFont(self.FONT, self.FONT_SIZE))
        labelPalette = QPalette()
        labelPalette.setColor(QPalette.Foreground, QColor(self.COLOR_LABEl))
        label.setPalette(labelPalette)
        return label

    def createButton(self, text, color):
        button = QPushButton(text)
        button.setStyleSheet(
            'background-color: white;color:black;font-size: 14px;font-family: Courier 14px;border-left: 10px outset ' + color + '; border-style: solid;min-height: 50px')
        return button

    def initializePalette(self):
        design = QPalette()
        design.setColor(QPalette.Background, Qt.black)
        self.setAutoFillBackground(True)
        self.setPalette(design)
