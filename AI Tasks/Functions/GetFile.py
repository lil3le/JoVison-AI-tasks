import tkinter as tk
from tkinter import filedialog
def get_image_file():
    # get file dialog
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )

    if file_path:
        return file_path
    else:
        print("No file selected.")
        exit(0)