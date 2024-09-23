from PIL import Image
import pytesseract

# Load the image
image_path = 'pb.jpg'
img = Image.open(image_path)

# Convert the image to grayscale
gray_img = img.convert('L')

# Optional: Save the grayscale image (for debugging)
gray_img.save('grayscale_image.jpg')

# Perform OCR on the grayscale image
extracted_text = pytesseract.image_to_string(gray_img)

# Print the extracted text
print(extracted_text)
