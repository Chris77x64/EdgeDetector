from enum import Enum

class State(Enum):

    fourier = 0
    sobel = 1
    laplace = 2
    canny = 3
    dog = 4
    log = 5