import tkinter as tk
from tkinter import ttk
# from changeFormat import format_img
import sys
import os
from changeFormat import convert_to_format
from time import sleep

def to_convert():
    """ Function to execute when the Convert button is clicked """
    selected_format = format_var.get()
    if selected_format :
        format_img(selected_format,message_var)
    else:
        message_var.set(f"No Format Selected {selected_format}...")
   
def format_img(imageFormat, alertText):
    if len(sys.argv) >= 1:
        success_count = 1
        for image_file in sys.argv[1:]:
            _, ext = os.path.splitext(image_file)
            filetype = ext.lstrip('.')
            alertText.set(f"{filetype} {imageFormat} {image_file}")
            if filetype == imageFormat:
                alertText.set(f"Some files contain same filetype")
                return
            alertText.set(f"Converting {success_count} of {len(sys.argv)}!!")
            convert_to_format(image_file, imageFormat)
            success_count += 1
        alertText.set(f"Files are converted !!")
    else:
        alertText.set(f"No image file provided!")


root = tk.Tk()
root.title("Image Converter")
root.geometry("300x150")

label = tk.Label(root, text="Select format:", font=("Arial", 12))
label.pack(pady=10)

# Dropdown menu
format_var = tk.StringVar(value="png")  # Default value
format_dropdown = ttk.Combobox(root, textvariable=format_var, values=[
                               "png", "webp"], state="readonly")
format_dropdown.pack(pady=5)

# Convert button
convert_button = tk.Button(
    root, text="Convert", command=to_convert, font=("Arial", 12))
convert_button.pack(pady=10)

# alert box
message_var = tk.StringVar(value="Press Convert after selecting format...")
message_label = tk.Label(root, textvariable=message_var,
                         font=("Arial", 10), fg="gray")
message_label.pack(pady=5)

# Run the application
root.mainloop()
