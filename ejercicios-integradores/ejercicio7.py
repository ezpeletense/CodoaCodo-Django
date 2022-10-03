from ejercicio6 import Persona
from excepciones_ejercicios import CuentaTitularInvalidoError


class Cuenta:

    def __init__(self, titular, cantidad: float = 0):
        self.titular = titular
        self.__cantidad = cantidad

    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    # Setter para titular
    @titular.setter
    def titular(self, titular):
        self.__validar_persona(titular)
        self.__titular = titular

    # Métodos de la clase
    def __validar_persona(self, titular):
        if isinstance(titular, Persona):
            return titular
        else:
            mensaje = f"{titular} no es una persona."
            raise CuentaTitularInvalidoError(mensaje)

    def mostrar(self):
        print(f"""
            Datos de la cuenta - Titular: {self.titular.mostrar()},
            saldo: ${self.cantidad}
            """)

    def ingresar(self, monto):
        if monto > 0:
            self.__cantidad += monto

    def retirar(self, monto):
        if monto > 0:
            self.__cantidad -= monto

# Prueba de la clase Cuenta


pablo = Persona("Pablo", 32, "35000000")
cuenta1 = Cuenta(pablo, 10)
# cuenta2 = Cuenta("Juan", 10000) # -> CuentaTitularInvalidoError: Juan no es una persona.

cuenta1.ingresar(40)
cuenta1.mostrar()  # -> $50
cuenta1.retirar(60)
cuenta1.mostrar()  # -> $-10
