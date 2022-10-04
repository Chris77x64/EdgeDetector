import numpy as np
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QLabel

from src.view import Settings

class ControllerSettings:

    settings: Settings
    param : Signal(np.ndarray)

    def __init__(self,settings: Settings,param: Signal(np.ndarray)):
        self.initializeChangeListener(settings)
        self.settings = settings
        self.param = param

    def initializeChangeListener(self,settings: Settings):
        for i in range(len(settings.label)):
            slider = settings.sliders[i]
            label = settings.label[i]
            slider.valueChanged.connect(lambda newValue, l=label: self.valueChangedSettings(newValue, l))

    def valueChangedSettings(self,newValue,label):
        label.setText(format(newValue))
        updatedParameter = [float(l.text()) for l in self.settings.label]
        self.param.emit(updatedParameter)