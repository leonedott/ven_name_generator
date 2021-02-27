import random

vocales = set('aeiou')

# EN: A list with no non-defined elements.
# ES: Una lista sin elementos no definidos
def eliminador_de_nan(lista):
    lista_clean = []
    for elemento in lista:
        if type(elemento) is str:
            lista_clean.append(elemento)
    return lista_clean


def limpia_lista(un_dicc):
    # Crea una lista de listas con los datos de un diccionario
    for i in un_dicc:
        list_of_lists = []
        for item in un_dicc.values():
            new_list = eliminador_de_nan(list(item.values()))
            list_of_lists.append(new_list)
        return list_of_lists


def si_o_no():
    '''
    EN: Defines a random choice with odds of 3:2
    ES: Define una elección aleatoria con probabilidad de 3:2
    '''
    siono = random.choice([True, True, False, True, False])
    return siono

'''
EN: The next few functions manage the exceptions that are needed when forming a new name.
Each function is used in a different step later on, and respond to different rules.
ES: Las siguientes funciones corresponden a excepciones necesarias para la correcta 
formación del nombre. Cada función corresponde a un paso distinto, con distintas reglas
'''

def exc_01(variable, choice):
    '''
    EN: Exceptions for the first vowel of the first syllable.
    ES: Excepciones para la elección de la primera vocal de la primera sílaba.
    '''
    para_y = ['y', 'ya', 'ye', 'yo', 'yu']
    para_chr =['u', 'a', 'o']
    para_wh = ['iu', 'ia', 'u']
    para_gh = ['iu', 'a']
    if 'w' in variable and 'oa' in choice:
        return False
    elif 'y' in variable and any(x in choice for x in para_y):
        return False
    elif 'gh' in variable and any(x in choice for x in para_gh):
        return False
    elif 'chr' in variable and any(x in choice for x in para_chr):
        return False
    elif 'wh' in variable and any(x in choice for x in para_wh):
        return False
    else:
        return True


def exc_02(variable, choice):
    '''
    EN: Exceptions for the second consonant of the first syllable.
    ES: Excepciones para la elección de la segunda consonante en la primera sílaba.
    '''
    para_s = ['u', 'a', 'o']
    para_ss = ['kl', 'f', 'rr', 'cl', 'y']
    para_z = ['rr', 'kl']
    para_r = ['r', 'rr', 'kl', 'f']
    para_l = ['l', 'll']
    para_ll = ['n', 'nn']

    l_ll = ['l', 'll']
    if 's' in variable and any(x in choice for x in para_s):
        return False
    elif 'ss' in variable and any(x in choice for x in para_ss):
        return False
    elif 'z' in variable and 'rr' in choice:
        return False
    elif 'x' in variable and any(x in choice for x in para_z):
         return False
    elif 'r' in variable and any(x in choice for x in para_r):
        return False
    elif 'n' in variable and 'rr' in choice:
        return False
    elif any(x in variable for x in l_ll) and any(x in choice for x in para_l):
        return False
    elif 'y' in variable and 'nn' in choice:
        return False
    elif 'll' in variable and any(x in choice for x in para_ll):
        return False
    else:
        return True


def exc_03(variable, choice):
    '''
    EN: Exceptions for the first consonant of the second syllable.
    ES: Excepciones para la elección de la primera consonante de la segunda sílaba.
    '''
    para_ll = ['k', 'll', 'l', 'rr', 'f', 'y']
    para_s = ['rr', 'r']
    para_ss = ['rr', 'll']
    para_l = ['l', 'll', 'rr']
    para_z = ['cl', 'l', 'll', 'rr', 'kl']
    para_x = ['k', 'kl', 'rr']
    para_r = ['r', 'rr']

    if 'll' in variable and any(x in choice for x in para_ll):
        return False
    elif 's' in variable and any(x in choice for x in para_s):
        return False
    elif 'ss' in variable and any(x in choice for x in para_ss):
        return False
    elif 'l' in variable and any(x in choice for x in para_l):
        return False
    elif 'z' in variable and any(x in choice for x in para_z):
        return False
    elif 'x' in variable and any(x in choice for x in para_x):
        return False
    elif 'r' in variable and any(x in choice for x in para_r):
        return False
    else:
        return True


def exc_04(variable, choice):
    '''
    EN: Exceptions for the vowel of the second syllable.
    ES: Para la elección de la vocal de la segunda sílaba.
    '''
    para_y = ['iu', 'yu']

    if variable[-1] not in vocales and choice[0] not in vocales:
        return False
    elif 'y' in variable and any(x in choice for x in para_y):
        return False
    elif variable[-1] == choice[0]:
        return False
    else:
        return True


def exc_05(variable, choice):
    '''
    EN: Exceptions for the last syllable.
    ES: Excepciones para la elección de la sílaba final.
    '''
    para_s = ['ngel', 'xon', 'ng']
    para_n= ['kh', 'gh']
    para_l= ['kh', 'gh', 'y']
    para_y = ['y']
    para_cons= ['nkh', 'ngh', 'ng', 'nk']
    if variable[-1] == choice[0]:
        return False
    elif variable[-1] == 's' and any(x in choice for x in para_s):
        return False
    elif variable[-1] == 'n' and any(x in choice for x in para_n):
        return False
    elif variable[-1] == 'l' and any(x in choice for x in para_l):
        return False
    elif variable[-1] == 'y' and any(x in choice for x in para_y):
        return False
    elif variable[-1] not in vocales and any(x in choice for x in para_cons):
        return False
    else:
        return True
    pass