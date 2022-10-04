import numpy as np
import cv2 as cv

def dft2D(img):

    rows,cols = img.shape
    result = np.zeros_like(img, dtype=complex)

    for r in range(rows):
        for c in range(cols):
            sum = 0
            for r1 in range(rows):
                for c1 in range(cols):
                    sum += img[r1, c1] * np.exp(- 2j * np.pi * ((r * r1) / rows + (c * c1) / cols))
            result[r, c] = sum

    return result


def omega(size):
    term = (-2j * np.pi / size)
    indices = np.arange(size)
    return np.exp(term * np.outer(indices, indices))


def dft2DVectorized(img):
    rows, cols = img.shape
    return np.asmatrix(omega(rows)) * img * np.asmatrix(omega(cols))


def omegaInverse(size):
    term = (2j * np.pi / size)
    indices = np.arange(size)
    return np.exp(term * np.outer(indices, indices))


def inverseDft2DVectorized(img):
    rows, cols = img.shape
    result = np.asmatrix(omegaInverse(rows)) * img * np.asmatrix(omegaInverse(cols))
    return result / (rows*cols)

def powerSpectra(img):
    dft = np.fft.fftshift(np.fft.fft2(img))
    dft = np.log(np.abs(dft * dft) + 1)
    dft = np.asarray((dft / np.max(dft)) * 255, np.uint8)
    dft[dft < np.median(dft)] = 0
   # return cv.applyColorMap(dft.astype(np.uint8), cv.COLORMAP_JET)
    #return dft
    return cv.applyColorMap(dft.astype(np.uint8), cv.COLORMAP_JET)