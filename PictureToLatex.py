from pix2tex import cli as pix2tex
from PIL import Image
import re

model = pix2tex.LatexOCR()

def remove_tex_sym_format(tex_str, format):
    #this function identify and remove speical latex fonts symtax 
    # print(format)
    pattern = r"\\" + format + r"{(.*?)}"
    
    pattern1 = "\\" + format + "{"
    # print(pattern)
    # print(pattern1)
    matches = re.findall(pattern, tex_str)
    # print(matches)
    matches = set(matches)

    tex_str = tex_str.replace(pattern1, "")
    # print(tex_str)
    for letter in matches:
        tex_str = tex_str.replace(letter+"}",letter)
    # print(tex_str)
    return tex_str

def simplify_latex(tex_str):
    #sometimes latex will have special fonts for maths symbols, remove them to avoid complications.
    format_to_remove = ['mathbf','mathrm',"mathit",'mathnormal','mathcal','mathscr','mathbb','varmathbb','mathbbm','mathbbmss','mathbbmtt','mathds','mathbbb','mathfrak']
    
    for format in format_to_remove:
        tex_str = remove_tex_sym_format(tex_str, format)

    tex_str = tex_str.replace("\\bf", "")
    tex_str = tex_str.replace("\\bigr", "")
    tex_str = tex_str.replace("\\bigl", "")
    tex_str = tex_str.replace("\\big", "")
    return tex_str

img = Image.open('test.png')
str_formula = model(img)
str_formula = simplify_latex(str_formula)

print(str_formula)