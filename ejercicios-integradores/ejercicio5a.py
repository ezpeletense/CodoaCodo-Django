# Sabiendo que ValueError es la excepción que se lanza cuando
# no podemos convertir una cadena de texto en su valor numérico,
# escriba una función get_int() que lea un valor entero del usuario
# y lo devuelva, iterando mientras el valor no sea correcto.
# Intente resolver el ejercicio tanto de manera *iterativa (5a)*
# como *recursiva (5b)*.

def get_int_i(num: str) -> int:
    """Recibe un string con un número entero y lo devuelve como integer.
    Si el valor ingresado no se puede pasar a int, pide otro valor.

    Args:
        num (str): el string que se convertirá a integer

    Returns:
        int: el integer que ingresó el usuario
    """

    aux = True
    while aux:
        try:
            num = int(num)
            aux = False
        except ValueError:
            print(f'"{num}" no es un valor numérico.')
            num = input("Por favor, ingrese un valor numérico entero: ")

    if __name__ == '__main__':
        return print(f'El número ingresado es: {num}')
    else:
        return num


get_int_i('51')
get_int_i(input('Ingrese un valor numérico: '))
get_int_i('cuarenta')
