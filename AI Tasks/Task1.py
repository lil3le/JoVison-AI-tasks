import pytesseract
from PIL import Image
from Functions.GetFile import get_image_file


def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text


print(extract_text_from_image(get_image_file()))