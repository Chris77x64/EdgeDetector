from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QPalette, QFont, QColor
from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QButtonGroup, QSpacerItem, \
    QSizePolicy, QToolTip

import qtawesome as qta


class Navbar(QWidget):

    ICON_SIZE = 45

    ICON_SAVE = 'msc.save'
    ICON_EXTEND = 'fa5s.expand-arrows-alt'
    ICON_GITHUB = 'mdi6.github'

    ICON_PLAY = 'fa.play'  #'fa5.play-circle'
    ICON_PAUSE = 'fa.pause' #'fa.pause-circle'#'ei.pause' #fa5.pause-circle'

    COLOR_BACKGROUND = 'black'
    COLOR_ICON = 'white'

    def __init__(self):
        super().__init__()

        self.play = self.createButton(self.ICON_PLAY)
        self.pause = self.createButton(self.ICON_PAUSE)
        self.save = self.createButton(self.ICON_SAVE)
        self.extend = self.createButton(self.ICON_EXTEND)
        self.github = self.createButton(self.ICON_GITHUB)

        self.createToolTips()
        self.initializeBackground()
        self.createLayout()

    def createLayout(self):
        layout = QHBoxLayout(self)
        spacer = QSpacerItem(1, 1, QSizePolicy.Expanding)
#        layout.insertWidget(0, self.label)
        layout.addSpacerItem(spacer)
        layout.insertWidget(1, self.play)
        layout.insertWidget(2, self.pause)
        layout.insertWidget(3, self.save)
        layout.insertWidget(4, self.extend)
        layout.insertWidget(5, self.github)

    def initializeBackground(self):
        design = QPalette()
        design.setColor(QPalette.Background, QColor(self.COLOR_BACKGROUND))
        self.setAutoFillBackground(True)
        self.setPalette(design)

    def createButton(self, iconString):
        button = QPushButton()
        button.setIcon(qta.icon(iconString, color=self.COLOR_ICON))
        button.setIconSize(QSize(self.ICON_SIZE, self.ICON_SIZE))
        button.setStyleSheet('QPushButton {background-color: ' + self.COLOR_BACKGROUND + '}')
        return button

    def createToolTips(self):
        self.save.setToolTip('Save')
        self.extend.setToolTip('Fullscreen')
        self.github.setToolTip('Visit GitHub')
