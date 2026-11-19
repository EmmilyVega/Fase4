
# ==================================================
# FJ RESERVALAB
# Empresa: Software FJ
# Estudiante: Emmily Daniela Vega Rincon
# Curso: Programacion
# Actividad: Fase 4
# ==================================================

from abc import ABC, abstractmethod
from excepciones import ErrorCliente


# Esta clase representa los datos generales
# que pueden compartir las diferentes entidades.
class Entidad(ABC):

    def __init__(self, identificacion, nombre):
        self._identificacion = identificacion
        self._nombre = nombre

    @property
    def identificacion(self):
        return self._identificacion

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def validar(self):
        """Cada entidad debe tener su propia validacion."""
        pass


# Esta clase representa a las personas que utilizan
# los servicios disponibles en FJ ReservaLab.
class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):
        super().__init__(identificacion, nombre)

        # Guardamos los datos de contacto como atributos privados.
        self.__correo = correo
        self.__telefono = telefono

        # Antes de aceptar el registro revisamos sus datos.
        self.validar()

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def validar(self):
        """Comprueba que la informacion del cliente sea correcta."""

        if not isinstance(self.identificacion, str) or not self.identificacion.strip():
            raise ErrorCliente("La identificacion es obligatoria.")

        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorCliente("El nombre es obligatorio.")

        if not isinstance(self.correo, str) or "@" not in self.correo:
            raise ErrorCliente("El correo electronico no es valido.")

        if "." not in self.correo.split("@")[-1]:
            raise ErrorCliente("El correo debe tener un dominio valido.")

        if not isinstance(self.telefono, str) or not self.telefono.isdigit():
            raise ErrorCliente("El telefono debe contener solamente numeros.")

        if len(self.telefono) < 7:
            raise ErrorCliente("El telefono debe tener al menos 7 digitos.")

        return True

    def describir(self):
        """Presenta los datos principales del cliente."""

        return (
            f"Cliente: {self.nombre} | "
            f"Identificacion: {self.identificacion} | "
            f"Correo: {self.correo} | "
            f"Telefono: {self.telefono}"
        )

    def __str__(self):
        return self.describir()
