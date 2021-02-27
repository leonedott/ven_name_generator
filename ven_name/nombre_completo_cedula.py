import pandas as pd
import random
import toolbox_primer_nombre as tb
import frases_saludo as frase
import nombre_ven as nv

# EN: The name that was created in nombre_ven is combined with a middle name and two surnames.
# ES: El nombre que fue creado en nombre_ven se combina con un segundo nombre y dos apellidos.

silabas_raw = pd.read_csv(r'venezuelan_name_database.csv')
silabas_raw_dict = silabas_raw.to_dict()
silabas_lista = tb.limpia_lista(silabas_raw_dict)

nom_final = nv.nombre_ven(silabas_lista)

nom_ap_raw = pd.read_csv(r'rep_clean.csv')
nom_ap_raw_dict = nom_ap_raw.to_dict()
nom_ap_list = tb.limpia_lista(nom_ap_raw_dict)

primer_nombre = nom_final.upper()
segundo_nombre = random.choice(nom_ap_list[1])
primer_apellido = random.choice(nom_ap_list[2])
segundo_apellido = random.choice(nom_ap_list[2])
numero_de_cedula = str(random.randrange(1,999)) + '.' + str(random.randrange(100,999)) + '.' + str(random.randrange(100,999))

frase_inic = random.choice(frase.frases_lista_clean)
tweet = frase_inic.replace('fulano', primer_nombre.capitalize())