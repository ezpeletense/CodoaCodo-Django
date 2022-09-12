import io

# Escribir un programa que reciba una cadena de caracteres
# y devuelva un diccionario con cada palabra que contiene
# y la cantidad de veces que aparece (frecuencia).


def contador(cadena: str) -> dict:
    """Recibe una cadena de caracteres y devuelve
    un diccionario con cada palabra[key] que contiene 
    y la frecuencia[value] con que aparece.

    Args:
        cadena (str): la cadena de caracteres.

    Returns:
        contador (dict): un diccionario donde palabra[key]: frecuencia[value].
    """

    # Remover caracteres especiales, puntuación y mayúsculas de la cadena
    chars = "¿?¡!#$%^&*()"
    for ch in chars:
        cadena = cadena.replace(ch, '')
    cadena = cadena.replace(',', '').replace('.', '').replace('\n', ' ')
    cadena = cadena.lower()

    # Inicializar el diccionario vacio
    contador = {}

    for palabra in cadena.split(' '):
        if palabra not in contador:
            contador.update({palabra: 1})
        else:
            contador[palabra] += 1

    if __name__ == '__main__':
        return print(contador)
    else:
        return contador


# contador("Uno, dos, tres.")
# contador('¿Uno? ¡Dos! dos, tres, UNO. ')
# contador(io.open('prueba.txt', 'r', encoding='utf8').read())
