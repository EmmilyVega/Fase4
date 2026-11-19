
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

# --------------------------------------------------
# REGISTRO DE CLIENTES
# --------------------------------------------------

# En esta funcion revisamos los datos antes de
# agregar un cliente a la lista del sistema.
def registrar_cliente(identificacion, nombre, correo, telefono):

    try:
        nuevo_cliente = Cliente(
            identificacion,
            nombre,
            correo,
            telefono
        )

        clientes.append(nuevo_cliente)

        print(f"Cliente {nombre} registrado correctamente.")
        registrar_evento(f"Cliente registrado: {nombre}")

        return nuevo_cliente

    except ErrorCliente as error:
        print(f"No se pudo registrar el cliente: {error}")
        registrar_error(f"Error al registrar cliente: {error}")

        return None


# --------------------------------------------------
# CLIENTES DE PRUEBA
# --------------------------------------------------

# Registramos dos clientes con informacion valida.
daniela = registrar_cliente(
    "1020304050",
    "Daniela Vega",
    "daniela.vega@gmail.com",
    "3001234567"
)

miguel = registrar_cliente(
    "1098765432",
    "Miguel Ballén",
    "miguel.ballen@gmail.com",
    "3109876543"
)

# Este registro tiene un correo incorrecto.
# Lo utilizamos para comprobar que la validacion funcione.
valentina = registrar_cliente(
    "1000200030",
    "Valentina Ríos",
    "correo_incorrecto",
    "3204567890"
)
