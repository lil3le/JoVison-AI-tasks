from PIL import Image
from Functions.GetFile import get_image_file

def convert_to_grayscale(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size
    
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j][:3]
            gray = int(0.21 * r + 0.72 * g + 0.07 * b)
            pixels[i, j] = (gray, gray, gray)
    
    image.show()
    return image

convert_to_grayscale(get_image_file())
