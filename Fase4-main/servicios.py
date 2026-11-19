
# ==================================================
# FJ RESERVALAB
# Empresa: Software FJ
# Estudiante: Emmily Daniela Vega Rincon
# Curso: Programacion
# Actividad: Fase 4
# ==================================================

from abc import ABC, abstractmethod
from excepciones import ErrorServicio


# Esta clase establece las caracteristicas generales
# que deben tener los servicios del sistema.
class Servicio(ABC):

    def __init__(self, nombre, precio_base):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ErrorServicio("El nombre del servicio es obligatorio.")

        if (not isinstance(precio_base, (int, float))
                or isinstance(precio_base, bool) or precio_base <= 0):
            raise ErrorServicio("El precio debe ser mayor que cero.")

        self._nombre = nombre
        self._precio_base = precio_base

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @abstractmethod
    def calcular_costo(self, duracion):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self, duracion):
        pass


# Servicio para reservar espacios de reuniones.
class ReservaSala(Servicio):

    def validar_parametros(self, duracion):
        if (not isinstance(duracion, (int, float))
                or isinstance(duracion, bool) or duracion <= 0):
            raise ErrorServicio("La duracion de la sala debe ser positiva.")

    def calcular_costo(self, duracion):
        self.validar_parametros(duracion)
        return self.precio_base * duracion

    def describir(self):
        return f"Reserva de sala: {self.nombre}"


# Servicio para alquilar equipos tecnologicos.
class AlquilerEquipo(Servicio):

    def validar_parametros(self, duracion):
        if (not isinstance(duracion, int)
                or isinstance(duracion, bool) or duracion <= 0):
            raise ErrorServicio("Las horas de alquiler deben ser enteros positivos.")

    def calcular_costo(self, duracion):
        self.validar_parametros(duracion)
        return self.precio_base * duracion

    def describir(self):
        return f"Alquiler de equipos: {self.nombre}"


# Servicio para recibir orientacion y apoyo especializado.
class Asesoria(Servicio):

    def validar_parametros(self, duracion):
        if (not isinstance(duracion, int)
                or isinstance(duracion, bool) or duracion <= 0):
            raise ErrorServicio("La cantidad de horas de asesoria debe ser positiva.")

    def calcular_costo(self, duracion):
        self.validar_parametros(duracion)
        return self.precio_base * duracion

    def describir(self):
        return f"Asesoria especializada: {self.nombre}"
