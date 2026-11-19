
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

# --------------------------------------------------
# REGISTRO DE SERVICIOS
# --------------------------------------------------

# Creamos una funcion para agregar servicios
# y comprobar que sus datos sean correctos.
def registrar_servicio(servicio):

    try:
        servicios.append(servicio)

    except ErrorServicio as error:
        print(f"No se pudo registrar el servicio: {error}")
        registrar_error(f"Error al registrar servicio: {error}")

    else:
        print(f"Servicio {servicio.nombre} registrado correctamente.")
        registrar_evento(f"Servicio registrado: {servicio.nombre}")


# --------------------------------------------------
# SERVICIOS DISPONIBLES EN FJ RESERVALAB
# --------------------------------------------------

# Servicio destinado a reuniones y encuentros.
sala_horizonte = ReservaSala("Sala Horizonte", 50000)

# Servicio para el alquiler de equipos tecnologicos.
kit_conecta = AlquilerEquipo("Kit Conecta", 25000)

# Servicio de orientacion y apoyo en tecnologia.
codigo_claro = Asesoria("Codigo Claro", 80000)


# Agregamos los servicios a la lista del sistema.
registrar_servicio(sala_horizonte)
registrar_servicio(kit_conecta)
registrar_servicio(codigo_claro)

# --------------------------------------------------
# GESTION DE RESERVAS
# --------------------------------------------------

# Esta funcion permite crear una reserva y comprobar
# que los datos enviados sean correctos.
def crear_reserva(codigo, cliente, servicio, duracion):

    try:
        nueva_reserva = Reserva(
            codigo,
            cliente,
            servicio,
            duracion
        )

        reservas.append(nueva_reserva)

    except (ErrorReserva, ErrorCliente, ErrorServicio) as error:
        print(f"No fue posible crear la reserva: {error}")
        registrar_error(f"Error al crear reserva {codigo}: {error}")

        return None

    else:
        print(f"Reserva {codigo} creada correctamente.")
        registrar_evento(f"Reserva creada: {codigo}")

        return nueva_reserva


# --------------------------------------------------
# PRIMERAS RESERVAS DEL SISTEMA
# --------------------------------------------------

# Daniela solicita reservar la Sala Horizonte.
reserva_daniela = crear_reserva(
    "FJR-001",
    daniela,
    sala_horizonte,
    3
)

# Miguel solicita el servicio Kit Conecta.
reserva_miguel = crear_reserva(
    "FJR-002",
    miguel,
    kit_conecta,
    4
)


# --------------------------------------------------
# PRUEBA DE UNA RESERVA INCORRECTA
# --------------------------------------------------

# Intentamos crear una reserva con una duracion negativa.
# El sistema debe detectar el error y continuar funcionando.
reserva_invalida = crear_reserva(
    "FJR-003",
    daniela,
    codigo_claro,
    -2
)


# --------------------------------------------------
# CONFIRMACION DE RESERVAS
# --------------------------------------------------

for reserva in (reserva_daniela, reserva_miguel):

    if reserva is not None:

        try:
            mensaje = reserva.confirmar()
            print(mensaje)

            registrar_evento(
                f"Reserva {reserva.codigo} confirmada."
            )

        except ErrorReserva as error:
            print(f"No se pudo confirmar: {error}")
            registrar_error(str(error))
