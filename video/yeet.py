import pytesseract as tess
from PIL import Image


img =Image.open('th.png')

tess.pytesseract.tesseract_cmd = r'C:\Users\SIMPLON\AppData\Local\Tesseract-OCR\tesseract.exe'

text = tess.image_to_string(img)


print(text)
