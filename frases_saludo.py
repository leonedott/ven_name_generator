import pandas as pd
import toolbox_primer_nombre as tb

# Typical Venezuelan greeting phrases are read from a .csv file and put in a list.
# Frases típicas venezolanas de saludos se leen de un archivo .csv y se pasan a una lista.

frases_raw = pd.read_csv(r'frases_tipicas.csv')
frases_raw_dict = frases_raw.to_dict()
frases_lista = tb.limpia_lista(frases_raw_dict)
frases_lista_clean = frases_lista[0]