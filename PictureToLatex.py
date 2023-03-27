
from pix2tex import cli as pix2tex
from PIL import Image

model = pix2tex.LatexOCR()

def get_formula(img):
    img = Image.open(img)
    str_formula = model(img)
    return str_formula

