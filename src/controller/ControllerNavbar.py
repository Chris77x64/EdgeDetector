import os

import numpy as np
from PySide2.QtCore import Signal

from src.view.Content import Content
from src.view.Navbar import Navbar

import cv2 as cv

class ControllerNavbar:

    navbar: Navbar
    play : Signal(bool)

    image: np.ndarray

    def __init__(self, navbar: Navbar,play,image):
        self.navbar = navbar
        self.play = play

        self.image = image
        self.navbar.play.clicked.connect(self.start)
        self.navbar.pause.clicked.connect(self.pause)
        self.navbar.save.clicked.connect(self.save)


    def start(self):
        self.play.emit(True)

    def pause(self):
        self.play.emit(False)

    def save(self):
        randomString = format(np.random.rand(1)[0])
        cv.imwrite('assets/Screenshot'+randomString+'.jpg',self.image)


