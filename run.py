from ocrv2 import Reader
import os
import sys
from easygui import *
import pytesseract as ocr

try:
    reader = Reader('test1.pdf')
    reader.read(reader.load_and_convert())
except ocr.pytesseract.TesseractNotFoundError:
    title = "Install Tesseract OCR"
    message = "Tesseract 4.0 is required to run\n\
    this software. Do you want to install it now?"
    yesnobox = ynbox(message, title)
    if yesnobox == True:
        os.system('tessinstall.exe')
    else:
        sys.exit()
