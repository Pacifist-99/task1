import cv2
import argparse
import numpy as np


# construct the argument parser and parse the arguments

def dataloader(path):
    data = cv2.imread(path)
    return data



def load_image(data):
    """image data is value and it converts image into another size given  
    reference:https://stackoverflow.com/questions/53152665/opencv-python-blur-image-using-trackbar
    filter_reference: https://stackoverflow.com/questions/30331944/finding-red-color-in-image-using-python-opencv """
    img = data.copy()
    img = cv2.resize(img, (0,0), fx=0.15, fy=0.15)
    return img
def colour_filter(img):
    result=img.copy()
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([153,25,0])
    upper = np.array([177,255,255])
    mask = cv2.inRange(frame, lower, upper)
    result = cv2.bitwise_and(result, result, mask=mask)
    return result

def blurr():    
    # cv2.namedWindow('Image')
    # # Creates Trackbar with slider position and callback function
    # low_k = 1 # slider start position
    # high_k = 31  # maximal slider position
    # cv2.createTrackbar('Blur', 'Image', low_k, high_k, on_change)
    ksize = cv2.getTrackbarPos('Blur', 'Image')  # returns trackbar position
    return ksize


def blurr_image(img,i):
        ksize=i
        ksize = 2*ksize-1  # medianBlur allows only odd ksize values
        # Blures input image
        median = cv2.medianBlur(img, ksize)  # source, kernel size
        return median