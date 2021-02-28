import random
import toolbox_primer_nombre as tb01

# What's in a (Venezuelan) name?
# ¿Cómo está formado un nombre (venezolano)?

def nombre_ven(lista):
    nom_final = ''
    # EN: A random first syllable is chosen from a list an added to the string.
    # ES: Se elige aleatoriamente la primera sílaba de una lista.

    pr_sil_pr_cons = random.choice(lista[0])
    nom_final += pr_sil_pr_cons

    # EN: All the exception functions from toolbox_primer_nombre are used to progressively form a name.
    # ES: Las funciones que manejan las excepciones (de toolbox_primer_nombre) son usadas para formar el nombre progresivamente.
    pr_sil_pr_vocal = random.choice(lista[1])
    prueba_01 = tb01.exc_01(nom_final, pr_sil_pr_vocal)
    while prueba_01 is False:
        pr_sil_pr_vocal = random.choice(lista[1])
        prueba_01 = tb01.exc_01(nom_final, pr_sil_pr_vocal)
    else:
        nom_final += pr_sil_pr_vocal

    if not tb01.si_o_no():
        pass
    else:
        pr_sil_seg_cons = random.choice(lista[2])
        prueba_02 = tb01.exc_02(nom_final, pr_sil_seg_cons)
        while prueba_02 is False:
            pr_sil_seg_cons = random.choice((lista[2]))
            prueba_02 = tb01.exc_02(nom_final, pr_sil_seg_cons)
        else:
            nom_final += pr_sil_seg_cons

    if not tb01.si_o_no():
        pass
    else:
        if not tb01.si_o_no():
            pass
        else:
            seg_sil_pr_cons = random.choice(lista[3])
            prueba_03 = tb01.exc_03(nom_final, seg_sil_pr_cons)
            while prueba_03 is False:
                seg_sil_pr_cons = random.choice((lista[3]))
                prueba_03 = tb01.exc_03(nom_final, seg_sil_pr_cons)
            else:
                nom_final += seg_sil_pr_cons

        seg_sil_pr_vo = random.choice(lista[4])
        prueba_04 = tb01.exc_04(nom_final, seg_sil_pr_vo)
        while prueba_04 is False:
            seg_sil_pr_vo = random.choice(lista[4])
            prueba_04 = tb01.exc_04(nom_final, seg_sil_pr_vo)
        else:
            nom_final += seg_sil_pr_vo

    ter_sil = random.choice(lista[5])
    prueba_05 = tb01.exc_05(nom_final, ter_sil)
    while prueba_05 is False:
        ter_sil = random.choice(lista[5])
        prueba_05 = tb01.exc_05(nom_final, ter_sil)
    else:
        nom_final += ter_sil

    return nom_final.upper()