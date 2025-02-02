import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os

# Path to the certificate template image
TEMPLATE_PATH = "E:/Python projects/certificate automation/certificate_template.png"
# Path to the font file
FONT_PATH = "ARIAL.TTF"  # Update with your font file path
FONT_SIZE = 60  # Size of the font for the recipient's name
OUTPUT_DIR = "certificates"  # Directory where generated certificates will be saved

# Create the output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load the Excel file containing participant names
EXCEL_FILE = "Names.xlsx"  # Update with your Excel file path
df = pd.read_excel(EXCEL_FILE)  # Reading Excel file into a DataFrame


def generate_certificate(name):
    """
    Generates a certificate for the given name and saves it as a PDF.

    Parameters:
    name (str): Name of the participant to be printed on the certificate.
    """
    # Open the certificate template image
    img = Image.open(TEMPLATE_PATH)
    draw = ImageDraw.Draw(img)

    # Load the font to be used for the name text
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    # Calculate the text size and position for the name
    bbox = draw.textbbox((0, 0), name, font=font)  # Bounding box for the text
    text_width = bbox[2] - bbox[0]  # Width of the text
    text_height = bbox[3] - bbox[1]  # Height of the text

    img_width, img_height = img.size  # Dimensions of the certificate template

    # Assume the title is positioned around 30% of the image height
    title_y_position = img_height * 0.3
    # Position the name slightly below the title with a gap of 65 pixels
    name_y_position = title_y_position + 65

    # Center the text horizontally
    text_x = (img_width - text_width) / 2

    # Draw the participant's name on the certificate
    draw.text((text_x, name_y_position), name, fill="black", font=font)

    # Save the certificate as a PDF file in the output directory
    output_path = f"{OUTPUT_DIR}/{name}.pdf"
    img.save(output_path, "PDF")

    print(f"✅ Certificate saved: {output_path}")


# Generate certificates for all participants in the Excel file
for index, row in df.iterrows():
    name = row["Name"]  # Adjust column name based on your Excel file structure
    generate_certificate(name)

print("✅ All certificates generated successfully!")
