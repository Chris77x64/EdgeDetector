import numpy as np
import cv2 as cv
from src.model.Kernel import sobelX, sobelY, zeroPadding, laplace, gaussian, laplacianOfGaussian
from src.model.DiscreteFourier2D import dft2DVectorized, inverseDft2DVectorized


def convolution2D(image, kernel):
    paddedKernel = zeroPadding(kernel, image)
    convFT = dft2DVectorized(paddedKernel) * dft2DVectorized(image)
    return inverseDft2DVectorized(convFT)


def sobelEdgeDetector(image):
    gX = cv.filter2D(image, cv.CV_64F, sobelX())
    gY = cv.filter2D(image, cv.CV_64F, sobelY())
    return np.sqrt(gX ** 2 + gY ** 2).astype(np.uint8)


def laplaceEdgeDetector(image, scaling=2):
    return cv.filter2D(image, cv.CV_8U, laplace(scaling))


def cannyEdgeDetector(image, minVal=90, maxVal=100):
    return cv.Canny(image, minVal, maxVal).astype(np.uint8)


def normalize(image):
    return (255*(image - np.min(image))/np.ptp(image)).astype(int)


def differenceOfGaussians(image, sigma0=10, sigma1=9, w=25):
    largeBlur = cv.filter2D(image, cv.CV_64F, gaussian(w, sigma0))
    smallBlur = cv.filter2D(image, cv.CV_64F, gaussian(w, sigma1))
    diff = largeBlur - smallBlur

    diff[diff < -1] = 0
    result = np.zeros_like(image)
    result = cv.normalize(diff,result, 0, 255, cv.NORM_MINMAX)
    result = np.asarray(result,np.uint8)
    #print(type(diff),diff.dtype)
    return result


def logEdgeDetector(image, w,sigma1, sigma2):
    largeBlur = cv.filter2D(image, cv.CV_64F, gaussian(w, sigma1))
    smallBlur = cv.filter2D(image, cv.CV_64F, gaussian(w, sigma2))
    LoG = largeBlur - smallBlur

    minLoG = cv.morphologyEx(LoG, cv.MORPH_ERODE, np.ones((3, 3)))
    maxLoG = cv.morphologyEx(LoG, cv.MORPH_DILATE, np.ones((3, 3)))
    zeroCross = np.logical_or(np.logical_and(minLoG < 0, LoG > 0), np.logical_and(maxLoG > 0, LoG < 0))
    return np.asarray(zeroCross*255,np.uint8)
    # diff = cv.filter2D(image,cv.CV_64F,laplacianOfGaussian(w,sigma))
    # result = np.zeros_like(image)
    # result = cv.normalize(diff,result, 0, 255, cv.NORM_MINMAX)
    # result = np.asarray(result,np.uint8)


def marrHildrethEdgeDetector(image,sigma0=10, sigma1=9, w=25):

    differenceGaussians = differenceOfGaussians(image,sigma0,sigma1,w)

    result = np.zeros_like(image)
    memoization = dict()
    rows, cols = image.shape

    c1, c2 = np.meshgrid(np.arange(-1, 2), np.arange(-1, 2))
    nX, nY = c2.flatten(), c1.flatten()

    for r in range(rows):
        for c in range(cols):
            currentValue = differenceGaussians[r, c]
            for i in range(len(nX)):
                x = r + nX[i]
                y = c + nY[i]
                if not outOfBounds(rows, cols, x, y):
                    comparisonValue = differenceGaussians[x, y]
                    if zeroCrossing(currentValue, comparisonValue):
                        if not crossingMemoized(r, c, x, y, memoization):
                            if np.abs(currentValue) >= abs(comparisonValue):
                                result[x, y] += 1
                            else:
                                result[r, c] += 1
                            memoization[(r, c, x, y)] = True

    return (result*255) / np.max(result)


def crossingMemoized(r, c, x, y, memoization):
    return (r, c, x, y) in memoization or (x, y, r, c) in memoization


def outOfBounds(rows, cols, row2, col2):
    if row2 < 0 or col2 < 0 or row2 >= rows or col2 >= cols:
        return True
    return False

def zeroCrossing(currentValue, comparisonValue):
    return (currentValue > 0 > comparisonValue) or (currentValue < 0 < comparisonValue)
