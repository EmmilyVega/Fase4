
# ==================================================
# FJ RESERVALAB
# Empresa: Software FJ
# Estudiante: Emmily Daniela Vega Rincón
# Curso: Programación
# Actividad: Fase 4
# ==================================================

import logging

from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva
from excepciones import (
    ErrorCliente,
    ErrorServicio,
    ErrorReserva,
    OperacionNoPermitida,
    DatoFaltante
)


# Configuramos el registro de eventos y errores.
# La informacion se guardara en el archivo logs.log.
logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


# Estas listas permiten guardar los datos mientras
# el programa se encuentra en funcionamiento.
clientes = []
servicios = []
reservas = []


# Utilizamos esta funcion para registrar las acciones
# importantes que se realizan dentro del sistema.
def registrar_evento(mensaje):
    logging.info(mensaje)


# Tambien dejamos una funcion para registrar errores.
def registrar_error(mensaje):
    logging.error(mensaje)
