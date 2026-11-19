
# ============================================
# SOFTWARE FJ
# Modulo para el manejo de excepciones
# ============================================

# Excepcion para errores relacionados con clientes
class ErrorCliente(Exception):
    """Se genera cuando los datos de un cliente no son validos."""
    pass


# Excepcion para errores relacionados con servicios
class ErrorServicio(Exception):
    """Se genera cuando un servicio no es valido o no esta disponible."""
    pass


# Excepcion para errores relacionados con reservas
class ErrorReserva(Exception):
    """Se genera cuando ocurre un problema con una reserva."""
    pass


# Excepcion para operaciones no permitidas
class OperacionNoPermitida(Exception):
    """Se genera cuando se intenta realizar una operacion incorrecta."""
    pass


# Excepcion para datos faltantes
class DatoFaltante(Exception):
    """Se genera cuando falta informacion obligatoria."""
    pass
