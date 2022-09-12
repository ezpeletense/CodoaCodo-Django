from ejercicio3 import contador

# Escribir un programa que reciba una cadena de caracteres
# y devuelva un diccionario con cada palabra que contiene
# y la cantidad de veces que aparece (frecuencia).
# Escribir otra función que reciba el diccionario generado
# con la función anterior y devuelva una tupla con la palabra
# más repetida y su frecuencia.


def mas_repetida(dict_palabras: dict) -> tuple:
    """Recibe un diccionario de frecuencias de aparición de
    palabras y devuelve una tupla con la palabra más repetida
    y su frecuencia.

    Args:
        contador (dict): diccionario de palabras[key] y sus
        respectivas frecuencias[value].

    Returns:
        tuple: tupla con la palabra más repetida y su frecuencia.
    """

    mas_freq = ['', 0]
    for k, v in dict_palabras.items():
        if v > mas_freq[1]:
            mas_freq[0], mas_freq[1] = k, v
        elif v == mas_freq[1]:
            mas_freq.append(k)
            mas_freq.append(v)

    mas_freq = tuple(mas_freq)

    print(mas_freq)


mi_dict = contador('uno, uno, dos, tres, tres, tres, tres, tres')
mi_otro_dict = contador(
    'uno, uno, uno, dos, tres, tres, tres, cinco cinco, cinco')

mas_repetida(mi_dict)
mas_repetida(mi_otro_dict)
