import pytesseract as ocr
from PIL import Image
import fitz

class Reader():
    def __init__(self, filename):
        self.filename = filename

    def read(self, file_name):
        self.text = ocr.image_to_string(Image.open(file_name), lang = 'pol')
        print(self.text)
        return self.text

    def load_and_convert(self):
        pdf = self.filename
        temp = fitz.open(pdf)
        for p in range(10):
            try:
                page = temp.loadPage(p)
            except:
                zoom_factor = 2.5
                zoom_matrix = fitz.Matrix(zoom_factor, zoom_factor)
                output = page.getPixmap(matrix = zoom_matrix)
                out = f"{self.filename}.png"
                img = output.writePNG(out)
        return out
        

reader = Reader('test1.pdf')
reader.read(reader.load_and_convert())



