
# ==================================================
# FJ RESERVALAB
# Empresa: Software FJ
# Estudiante: Emmily Daniela Vega Rincón
# Curso: Programación
# Actividad: Fase 4
# ==================================================

from datetime import datetime
from entidades import Cliente
from servicios import Servicio
from excepciones import ErrorReserva, ErrorCliente, ErrorServicio


# Esta clase permite relacionar un cliente con el
# servicio que desea utilizar.
class Reserva:

    ESTADOS = ("Pendiente", "Confirmada", "Cancelada")

    def __init__(self, codigo, cliente, servicio, duracion):

        # Revisamos que el codigo de la reserva sea correcto.
        if not isinstance(codigo, str) or not codigo.strip():
            raise ErrorReserva("El codigo de la reserva es obligatorio.")

        # Comprobamos que exista un cliente valido.
        if not isinstance(cliente, Cliente):
            raise ErrorCliente("Debe seleccionar un cliente valido.")

        # Verificamos que el servicio pertenezca al sistema.
        if not isinstance(servicio, Servicio):
            raise ErrorServicio("Debe seleccionar un servicio valido.")

        # Cada servicio revisa sus propias condiciones.
        servicio.validar_parametros(duracion)

        self.__codigo = codigo
        self.__cliente = cliente
        self.__servicio = servicio
        self.__duracion = duracion
        self.__estado = "Pendiente"
        self.__fecha = datetime.now()

    @property
    def codigo(self):
        return self.__codigo

    @property
    def cliente(self):
        return self.__cliente

    @property
    def servicio(self):
        return self.__servicio

    @property
    def duracion(self):
        return self.__duracion

    @property
    def estado(self):
        return self.__estado

    # Calculamos el valor de la reserva con opciones
    # de impuesto y descuento.
    def calcular_costo(self, impuesto=0, descuento=0):

        if (not isinstance(impuesto, (int, float))
                or isinstance(impuesto, bool) or not 0 <= impuesto <= 100):
            raise ErrorReserva("El impuesto debe estar entre 0 y 100.")

        if (not isinstance(descuento, (int, float))
                or isinstance(descuento, bool) or not 0 <= descuento <= 100):
            raise ErrorReserva("El descuento debe estar entre 0 y 100.")

        costo_base = self.__servicio.calcular_costo(self.__duracion)

        costo_con_descuento = costo_base * (1 - descuento / 100)
        costo_final = costo_con_descuento * (1 + impuesto / 100)

        return round(costo_final, 2)

    # Cambiamos el estado cuando una reserva es confirmada.
    def confirmar(self):

        if self.__estado != "Pendiente":
            raise ErrorReserva(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__estado = "Confirmada"
        return "Reserva confirmada correctamente."

    # Permitimos cancelar una reserva que no este cancelada.
    def cancelar(self):

        if self.__estado == "Cancelada":
            raise ErrorReserva("La reserva ya se encuentra cancelada.")

        self.__estado = "Cancelada"
        return "Reserva cancelada correctamente."

    # Procesamos la reserva y controlamos los errores
    # que puedan presentarse durante la operacion.
    def procesar(self):

        try:
            costo = self.calcular_costo()
            mensaje = self.confirmar()

        except (ErrorReserva, ErrorServicio, ErrorCliente) as error:
            raise ErrorReserva(
                f"No fue posible procesar la reserva: {error}"
            ) from error

        else:
            return {
                "mensaje": mensaje,
                "codigo": self.__codigo,
                "costo": costo,
                "estado": self.__estado
            }

        finally:
            print(
                f"Proceso de reserva {self.__codigo} finalizado."
            )

    # Mostramos los datos principales para consultar
    # la informacion de una reserva.
    def describir(self):

        return (
            f"Reserva: {self.__codigo}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.describir()}\n"
            f"Duracion: {self.__duracion}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.calcular_costo():,.2f}\n"
            f"Fecha: {self.__fecha.strftime('%d/%m/%Y %H:%M')}"
        )
