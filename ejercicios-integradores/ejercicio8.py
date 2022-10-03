from excepciones_ejercicios import CuentaJovenTitularInvalidoError

from ejercicio6 import Persona
from ejercicio7 import Cuenta


class CuentaJoven(Cuenta):
    pass

    def __init__(self, titular, cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    # Getter y setter para bonificacion
    @property
    def bonificacion(self):
        return self.__bonificacion

    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    # Métodos de la clase
    def mostrar(self):
        print(f"""
              Cuenta Joven - Titular: {self.titular.mostrar()},
              saldo: ${self.cantidad},
              bonificacion: {self.bonificacion}%
              """)

    def es_titular_valida(self):
        return self.titular.edad < 25 and self.titular.es_mayor_de_edad()

    def retirar(self, monto):
        if not self.es_titular_valida():
            mensaje = f"El titular, {self.titular.nombre}, no puede retirar dinero, porque no es válido."
            print(mensaje)
            raise CuentaJovenTitularInvalidoError(mensaje)
        elif monto > 0:
            super().retirar(monto)


# Prueba de la clase CuentaJoven

cloe = Persona("Cloe", 20, "45001001")
cuenta_cloe = CuentaJoven(cloe, 1000, 25)

cuenta_cloe.mostrar()
cuenta_cloe.retirar(100)
cuenta_cloe.mostrar()
