# Escribir una función que calcule el máximo común divisor entre dos números.

def calcula_mcd(a: int, b: int) -> int:
    """Calcula máximo común divisor entre dos números
    enteros utilizando el algoritmo de Euclides.

    Args:
        a (int): entero distinto de cero.
        b (int): entero distinto de cero.

    Returns:
        int: máximo común divisor entre a y b.
    """

    ap, bp = a, b

    if b > a:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b

    mcd = b

    if __name__ == "__main__":
        return f"El MCD entre {ap} y {bp} es: {mcd}"
    else:
        return mcd


# print(calcula_mcd(17, 23))
# print(calcula_mcd(60, 48))
# print(calcula_mcd(55, 89))
# print(calcula_mcd(15, 25))
# print(calcula_mcd(42, 56))
