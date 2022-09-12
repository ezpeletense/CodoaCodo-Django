from ejercicio1 import calcula_mcd

# Escribir una función que calcule el mínimo común múltiplo entre dos números.


def calcula_mcm(a: int, b: int) -> int:
    """Calcula el mínimo común múltiplo entre dos números
    enteros a partir del máximo común divisor.
    MCM(a, b) = a * b / MCD(a, b)

    Args:
        a (int): entero distinto de cero.
        b (int): entero distinto de cero.

    Returns:
        int: mínimo común múltiplo entre a y b.
    """

    mcm = int((a * b) / calcula_mcd(a, b))

    if __name__ == "__main__":
        return f"El MCM entre {a} y {b} es: {mcm}"
    else:
        return mcm


# print(calcula_mcm(72, 50))
# print(calcula_mcm(6, 33))
# print(calcula_mcd(42, 56))
