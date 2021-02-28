from PIL import Image
import random, glob

def foto_para_cedula():
    '''
    EN: A new ID picture is generated. from .png files
    ES: Se crea una foto para la cédula, usando .png
    '''
    base = Image.open('profiles/base.png').convert('RGBA')
    camisa = Image.open(random.choice(sorted(glob.glob('profiles/camisas/*')))).convert('RGBA')
    gorra = Image.open(random.choice(sorted(glob.glob('profiles/gorras/*')))).convert('RGBA')


    base.paste(camisa, (0, 0), camisa)
    base.paste(gorra, (0, 0), gorra)
    return base