
# ============================================
# SOFTWARE FJ
# Modulo de entidades y gestion de clientes
# ============================================

from abc import ABC, abstractmethod
from excepciones import ErrorCliente


# Clase abstracta que representa una entidad
# general del sistema.
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
        """Metodo abstracto para validar los datos."""
        pass


# Clase Cliente que hereda de Entidad.
class Cliente(Entidad):

    def __init__(self, identificacion, nombre, correo, telefono):
        super().__init__(identificacion, nombre)

        # Atributos privados para proteger los datos.
        self.__correo = correo
        self.__telefono = telefono

        # Validar los datos al crear el cliente.
        self.validar()

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    def validar(self):
        """Verifica que los datos del cliente sean correctos."""

        if not isinstance(self.identificacion, str) or not self.identificacion.strip():
            raise ErrorCliente("La identificacion es obligatoria.")

        if not isinstance(self.nombre, str) or not self.nombre.strip():
            raise ErrorCliente("El nombre es obligatorio.")

        if not isinstance(self.__correo, str) or "@" not in self.__correo:
            raise ErrorCliente("El correo electronico no es valido.")

        if "." not in self.__correo.split("@")[-1]:
            raise ErrorCliente("El correo debe tener un dominio valido.")

        if not isinstance(self.__telefono, str) or not self.__telefono.isdigit():
            raise ErrorCliente("El telefono debe contener solamente numeros.")

        if len(self.__telefono) < 7:
            raise ErrorCliente("El telefono debe tener al menos 7 digitos.")

        return True

    def describir(self):
        """Devuelve la informacion general del cliente."""
        return (
            f"Cliente: {self.nombre} | "
            f"Identificacion: {self.identificacion} | "
            f"Correo: {self.correo} | "
            f"Telefono: {self.telefono}"
        )

    def __str__(self):
        return self.describir()
