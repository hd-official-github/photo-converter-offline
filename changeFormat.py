import sys
import os
from PIL import Image


def convert_to_format(image_path, imageFormat):
    """ Converts the given image to PNG format. """
    if not os.path.exists(image_path):
        print("Error: File not found")
        return

    try:
        # Open the image
        img = Image.open(image_path)

        # Create output file path
        output_path = os.path.splitext(image_path)[0] + "."+imageFormat

        # Convert and save as PNG
        img.convert("RGB").save(output_path, imageFormat.upper())
        print(f"Converted to: {output_path}")

    except Exception as e:
        print(f"Error: {e}")

# Check if an image path was provided



