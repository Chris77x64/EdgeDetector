import numpy as np
import cv2 as cv

class Frame:

    def __init__(self,img,rows,cols):
        self.originalImage = np.asarray(img,np.uint8)
        self.greyScaleImage = self.calculateGreyscaleImage(img)
        self.resize(rows,cols)


    def calculateGreyscaleImage(self,img):
        return np.asarray(np.mean(img,axis=2),np.uint8)

    def resize(self,rows,cols):
        self.originalImage = cv.resize(self.originalImage,(rows,cols),cv.INTER_NEAREST)
        self.greyScaleImage = cv.resize(self.greyScaleImage, (rows, cols), cv.INTER_NEAREST)

    def channel(self,index):
        return self.originalImage[:,:,index]

    def toString(self):
        print('Original Image Dimensions: ', self.originalImage.shape)
        print('Greyscale Image Dimensions: ', self.greyScaleImage.shape)
