import numpy as np

def meanKernel(w):
    dim = (2 * w) + 1
    return 1 / (dim ** 2) * np.ones((dim, dim))


def zeroPadding(kernel, img):
    res = np.zeros_like(img)
    res[0:kernel.shape[0], 0:kernel.shape[1]] = kernel
    return res


def sobelY():
    return np.asarray([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])


def sobelX():
    return sobelY().T


def laplace(scaling):
    return scaling * np.asarray([[0, 1, 0], [1, -4, 1], [0, 1, 0]])


def gaussian(w, sigma):
    x, y = np.meshgrid(np.arange(-w, w + 1), np.arange(-w, w + 1))
    result = (1 / 2 * np.pi * sigma) * np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))
    return result / np.sum(result)

def laplacianOfGaussian(w,sigma):
    x, y = np.meshgrid(np.arange(-w, w + 1), np.arange(-w, w + 1))
    result = -(1 / (np.pi * (sigma**4))) * np.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))
    result *= 1 - ((x**2 + y**2) / (2 * (sigma**2)))
    return result / np.sum(result)
