from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\rjajoo\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\Script\pytesseract.exe"

image = Image.open(r'C:\Users\rjajoo\Desktop\Python\lion.png')

image_to_text = pytesseract.image_to_string(image, lang='eng')

print(image_to_text)
