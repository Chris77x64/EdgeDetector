from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtGui import QPalette, QColor
from PySide2.QtWidgets import QWidget, QVBoxLayout, QSlider, QLabel, QSizePolicy, QSpacerItem, QHBoxLayout

from src.model.State import State


class Settings(QWidget):

    FONT = 'Courier'
    FONT_SIZE = '20'

    variables : []
    variablesString : []
    label : []
    sliders : []

    def __init__(self,state: State):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.setSizePolicy(QSizePolicy.Maximum,QSizePolicy.Maximum)

        self.initializeVariables(state)
        self.initializeSettings()


    def initializeSettings(self):

        # labelSettings = self.createLabel('Parameter','white')
        # labelSettings.setAlignment(Qt.AlignHCenter)
        # labelSettings.setStyleSheet('font-size: 20px')
        # self.layout.insertWidget(0,labelSettings)

        for i in range(len(self.variables)):

            widget = QWidget()
            widget.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Minimum)
            layoutWidget = QVBoxLayout(widget)

            labelText = self.createLabel(self.variablesString[i],'white')

            slider = QSlider(Qt.Horizontal)
            slider.setRange(1, 255)
            slider.setValue(self.variables[i])
            slider.setStyleSheet("QSlider::handle:horizontal {background-color: orange;}")
            self.sliders.append(slider)


            widgetLabelValue = QWidget()
            layoutWidgetLabelValue = QHBoxLayout(widgetLabelValue)
            labelValueText = self.createLabel('Value: ','white')
            labelValueValue = self.createLabel(format(self.variables[i]),'GreenYellow')
            self.label.append(labelValueValue)

            spacer = QSpacerItem(1, 1, QSizePolicy.Expanding, QSizePolicy.Expanding)
            layoutWidgetLabelValue.insertWidget(0,labelValueText)
            layoutWidgetLabelValue.insertWidget(1,labelValueValue)
            layoutWidgetLabelValue.addSpacerItem(spacer)


                #(slider, QtCore.SIGNAL("valueChanged(int)"),labelValueValue,QtCore.SLOT("display(int)"))

            layoutWidget.insertWidget(0,labelText)
            layoutWidget.insertWidget(1,slider)
            layoutWidget.insertWidget(2,widgetLabelValue)

            self.layout.insertWidget(i,widget)


    def initializeVariables(self,state: State):

        self.variables = []
        self.variablesString = []

        self.label = []
        self.sliders = []

        if state == state.fourier:
            pass
        elif state == state.laplace:
            self.variables.append(10)
            self.variablesString.append('Scaling')
        elif state == state.sobel:
            pass
        elif state == state.canny:
            self.variables.append(90)
            self.variables.append(100)
            self.variablesString.append('Minimum Value')
            self.variablesString.append('Maximum Value')
        elif state == state.dog:
            self.variables.append(25)
            self.variables.append(10)
            self.variables.append(9)
            self.variablesString.append('Kernel Width')
            self.variablesString.append('Standard Deviation 1')
            self.variablesString.append('Standard Deviation 2')
        elif state == state.log:
            self.variables.append(9)
            self.variables.append(10)
            self.variables.append(9)
            self.variablesString.append('Kernel Width')
            self.variablesString.append('Standard Deviation 1')
            self.variablesString.append('Standard Deviation 2')

    def createLabel(self, text,color):
        label = QLabel(text)
        #label.setFont(QFont(self.FONT, self.FONT_SIZE,QFont.Bold))
        label.setStyleSheet('font-family: Courier '+self.FONT_SIZE+'px; font-size: '+self.FONT_SIZE+'px')
        labelPalette = QPalette()
        labelPalette.setColor(QPalette.Foreground, QColor(color))
        label.setPalette(labelPalette)
        return label

    def clear(self):
        for i in reversed(range(self.layout.count())):
            self.layout.itemAt(i).widget().setParent(None)
        self.setParent(None)
