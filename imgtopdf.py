from PIL import Image
from fpdf import FPDF

# Load the image
img_path = "pb1.jpg"
image = Image.open(img_path)

# Create a PDF
pdf = FPDF()
pdf.add_page()

# Convert image to PDF dimensions (A4 size)
pdf.image(img_path, 0, 0, 210, 297)  # Adjust width (210) and height (297) as needed

# Save the PDF
pdf.output("table_milk_nutrients.pdf")
