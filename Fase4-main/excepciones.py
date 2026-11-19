
# ==================================================
# FJ RESERVALAB
# Empresa: Software FJ
# Estudiante: Emmily Daniela Vega Rincon
# Curso: Programacion
# Actividad: Fase 4
# ==================================================


# Esta excepcion permite identificar problemas
# cuando se intenta registrar un cliente.
class ErrorCliente(Exception):
    """Controla errores en los datos de los clientes."""
    pass


# Se utiliza cuando un servicio tiene datos incorrectos
# o no cumple con las condiciones necesarias.
class ErrorServicio(Exception):
    """Controla errores relacionados con los servicios."""
    pass


# Esta excepcion ayuda a detectar problemas al crear,
# confirmar, cancelar o procesar una reserva.
class ErrorReserva(Exception):
    """Controla errores durante la gestion de reservas."""
    pass


# Se genera cuando alguien intenta realizar
# una accion que no esta permitida en el sistema.
class OperacionNoPermitida(Exception):
    """Controla las operaciones que no estan permitidas."""
    pass


# Nos permite identificar cuando falta algun dato
# necesario para continuar con una operacion.
class DatoFaltante(Exception):
    """Controla la ausencia de datos obligatorios."""
    pass
