import cv2
import numpy as np

def convert_image_to_grayscale(img): # returns a greyscale img
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

def threshold_image(grayscale_image):
    return cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def invert_image(thresholded_image):
    return cv2.bitwise_not(thresholded_image)

def dilate_image(inverted_image):
    return cv2.dilate(inverted_image, None, iterations=5)

# draws green lines
def find_contours(dilated_image,original_image):
    contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image_with_all_contours = original_image.copy()
    cv2.drawContours(image_with_all_contours,contours, -1, (0, 255, 0), 3)
    cv2.imshow('image_with_all_contours', image_with_all_contours) 
    cv2.waitKey(0)     
    return contours

def filter_contours_and_leave_only_rectangles(contours,image):
    rectangular_contours = []
    for contour in contours:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
        if len(approx) == 4:
            rectangular_contours.append(approx)
    image_with_only_rectangular_contours = image.copy()
    cv2.drawContours(image_with_only_rectangular_contours, rectangular_contours, -1, (0, 255, 0), 3)
    cv2.imshow('image_with_only_rectangular_contours', image_with_only_rectangular_contours) 
    cv2.waitKey(0)


def find_largest_contour(dilated_image, original_image):
    contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Find the largest contour by area
    largest_contour = max(contours, key=cv2.contourArea)
        
    # Create a copy of the original image to draw the largest contour
    image_with_largest_contour = original_image.copy()
        
     # Draw the largest contour in green with a thickness of 3
    cv2.drawContours(image_with_largest_contour, [largest_contour], -1, (0, 255, 0), 3)
    cv2.imshow('image_with_largest_contour', image_with_largest_contour) 
    cv2.waitKey(0) 
    
    
def find_largest_contour_with_rectangle(dilated_image, original_image):
    contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Find the largest contour by area
    largest_contour = max(contours, key=cv2.contourArea)
        
    # Create a copy of the original image
    image_with_rectangle = original_image.copy()
        
    # Get the bounding rectangle for the largest contour
    x, y, w, h = cv2.boundingRect(largest_contour)
        
    # Draw the rectangle on the image (in green with thickness 3)
    cv2.rectangle(image_with_rectangle, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv2.imshow('image_with_rectangle', image_with_rectangle) 
    cv2.waitKey(0) 
        
    return largest_contour, image_with_rectangle, (x, y, w, h)





















def erode_vertical_lines(inverted_image):
    hor = np.array([[1,1,1,1,1,1]])
    vertical_lines_eroded_image = cv2.erode(inverted_image, hor, iterations=10)
    vertical_lines_eroded_image = cv2.dilate(vertical_lines_eroded_image, hor, iterations=10)
    # cv2.imshow('vertical_lines_eroded_image', vertical_lines_eroded_image) 
    # cv2.waitKey(0)
    return vertical_lines_eroded_image
    
    
    
def erode_horizontal_lines(inverted_image):
    ver = np.array([[1],
            [1],
            [1],
            [1],
            [1],
            [1],
            [1]])
    horizontal_lines_eroded_image = cv2.erode(inverted_image, ver, iterations=10)
    horizontal_lines_eroded_image = cv2.dilate(horizontal_lines_eroded_image, ver, iterations=10) 
    # cv2.imshow('vertical_lines_eroded_image', horizontal_lines_eroded_image) 
    # cv2.waitKey(0)
    return horizontal_lines_eroded_image    
    
    
def combine_eroded_images(vertical_lines_eroded_image,horizontal_lines_eroded_image):
    combined_image = cv2.add(vertical_lines_eroded_image, horizontal_lines_eroded_image)   
    # cv2.imshow('combined_image', combined_image) 
    # cv2.waitKey(0)  
    return combined_image
    
    
    
def dilate_combined_image_to_make_lines_thicker(combined_image):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    combined_image_dilated = cv2.dilate(combined_image, kernel, iterations=5)
    # cv2.imshow('combined_image_dilated', combined_image_dilated) 
    # cv2.waitKey(0)    
    return combined_image_dilated


def subtract_combined_and_dilated_image_from_original_image(inverted_image,combined_image_dilated):
    image_without_lines = cv2.subtract(inverted_image,combined_image_dilated)
    # cv2.imshow('image_without_lines', image_without_lines) 
    # cv2.waitKey(0) 
    return image_without_lines


def remove_noise_with_erode_and_dilate(image_without_lines):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    image_without_lines_noise_removed = cv2.erode(image_without_lines, kernel, iterations=1)
    image_without_lines_noise_removed = cv2.dilate(image_without_lines_noise_removed, kernel, iterations=1)
    cv2.imshow('image_without_lines_noise_removed', image_without_lines_noise_removed) 
    cv2.waitKey(0) 
    return image_without_lines_noise_removed













def dilate_imagec(thresholded_image):
    kernel_to_remove_gaps_between_words = np.array([
            [1,1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1,1]
    ])
    dilated_image = cv2.dilate(thresholded_image, kernel_to_remove_gaps_between_words, iterations=5)
    simple_kernel = np.ones((5,5), np.uint8)
    dilated_image = cv2.dilate(dilated_image, simple_kernel, iterations=2)
    cv2.imshow('dilated_imagfffe', dilated_image) 
    cv2.waitKey(0) 
    return dilated_image



def find_contoursc(dilated_image,original_image):
    result = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = result[0]
    # The code below is for visualization purposes only.
    # It is not necessary for the OCR to work.
    image_with_contours_drawn = original_image.copy()
    cv2.drawContours(image_with_contours_drawn, contours, -1, (0, 255, 0), 3)
    cv2.imshow('image_with_contours_drawn', image_with_contours_drawn) 
    cv2.waitKey(0) 

