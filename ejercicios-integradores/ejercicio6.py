from excepciones_ejercicios import PersonaDatoInvalidoError


class Persona:

    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    # Setters para nombre, edad, dni
    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__validar_nombre(nuevo_nombre)
        self.__nombre = nuevo_nombre

    @edad.setter
    def edad(self, nueva_edad: int):
        self.__validar_edad(nueva_edad)
        self.__edad = nueva_edad

    @dni.setter
    def dni(self, nuevo_dni: str):
        self.__validar_dni(nuevo_dni)
        self.__dni = int(nuevo_dni)

    # Validación de las entradas
    def __validar_nombre(self, nombre: str) -> None:
        if nombre == " ":
            mensaje = "El campo nombre no puede estar vacío"
            print(mensaje)
            raise PersonaDatoInvalidoError(mensaje)

    def __validar_edad(self, edad: int) -> None:
        if edad < 0:
            mensaje = f"La edad ingresada es incorrecta: {edad}"
            print(mensaje)
            raise PersonaDatoInvalidoError(mensaje)

    def __validar_dni(self, numero_dni: str) -> None:
        try:
            dni = int(numero_dni)
        except ValueError:
            mensaje = f"El dato ingresado es incorrecto: {dni}"
            print(mensaje)
            raise PersonaDatoInvalidoError(mensaje)

        if len(str(dni)) < 6:
            mensaje = f"El dato ingresado es incorrecto: {dni}"
            raise PersonaDatoInvalidoError(mensaje)

    def mostrar(self):
        return f"Nombre: {self.nombre}. Edad: {self.edad}. DNI: {self.dni}."

    def es_mayor_de_edad(self):
        return self.edad >= 18


# Prueba de la clase Persona

pablo = Persona("Pablo", 32, "35000000")
print(pablo.mostrar())

pablo.nombre = "Cloe"
print(pablo.mostrar())

# pablo.nombre = " "
# print(pablo.mostrar())

print(pablo.es_mayor_de_edad())

pablo.edad = 17
print(pablo.es_mayor_de_edad())
