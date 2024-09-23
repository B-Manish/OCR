import cv2

def convert_image_to_grayscale(img): # returns a greyscale img
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

def threshold_image(grayscale_image):
    return cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def invert_image(thresholded_image):
    return cv2.bitwise_not(thresholded_image)

def dilate_image(inverted_image):
    return cv2.dilate(inverted_image, None, iterations=5)