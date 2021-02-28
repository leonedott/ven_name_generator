import nombre_completo_cedula as nombre
from PIL import Image, ImageDraw, ImageFont
import foto_para_la_cedula as foto

# EN: The ID card image is produced here.
# ES: La imagen de la cédula es creada aquí.
ced = Image.open(r"cedula_vacia.jpg")
foto = foto.foto_para_cedula()

# EN: In order: Two surnames + name + middle name + ID number
# ES: En orden: Dos apellidos + dos nombres + número de cédula
ap_inic = nombre.primer_apellido + ' ' + nombre.segundo_apellido
nom_inic = nombre.primer_nombre + ' ' + nombre.segundo_nombre
nc_inic = nombre.numero_de_cedula

font = ImageFont.truetype("arial.ttf", 30)

ap_fin = ImageDraw.Draw(ced)
ap_fin.text((278, 210), ap_inic, font=font, fill='black')

nom_fin = ImageDraw.Draw(ced)
nom_fin.text((278, 255), nom_inic, font= font, fill='black')

nc_fin = ImageDraw.Draw(ced)
nc_fin.text((516, 155), nc_inic, font=font, fill='black')

tweet = nombre.tweet
ced.paste(foto, (767, 303))

# ced.show()
# print(tweet)