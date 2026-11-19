
# ============================================
# SOFTWARE FJ
# Modulo de gestion de reservas
# ============================================

from datetime import datetime
from entidades import Cliente
from servicios import Servicio
from excepciones import ErrorReserva, ErrorCliente, ErrorServicio


class Reserva:

    # Estados posibles de una reserva
    ESTADOS = ("Pendiente", "Confirmada", "Cancelada")

    def __init__(self, codigo, cliente, servicio, duracion):

        # Validar el codigo de la reserva
        if not isinstance(codigo, str) or not codigo.strip():
            raise ErrorReserva("El codigo de la reserva es obligatorio.")

        # Validar el cliente
        if not isinstance(cliente, Cliente):
            raise ErrorCliente("Debe seleccionar un cliente valido.")

        # Validar el servicio
        if not isinstance(servicio, Servicio):
            raise ErrorServicio("Debe seleccionar un servicio valido.")

        # Validar la duracion
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

    def calcular_costo(self, impuesto=0, descuento=0):
        """
        Calcula el costo de la reserva.
        Permite utilizar impuestos y descuentos opcionales.
        """

        if not isinstance(impuesto, (int, float)) or isinstance(impuesto, bool) or not 0 <= impuesto <= 100:
            raise ErrorReserva("El impuesto debe estar entre 0 y 100.")

        if not isinstance(descuento, (int, float)) or isinstance(descuento, bool) or not 0 <= descuento <= 100:
            raise ErrorReserva("El descuento debe estar entre 0 y 100.")

        costo_base = self.__servicio.calcular_costo(self.__duracion)

        costo_con_descuento = costo_base * (1 - descuento / 100)

        costo_final = costo_con_descuento * (1 + impuesto / 100)

        return round(costo_final, 2)

    def confirmar(self):
        """Confirma una reserva pendiente."""

        if self.__estado != "Pendiente":
            raise ErrorReserva(
                "Solo se pueden confirmar reservas pendientes."
            )

        self.__estado = "Confirmada"
        return "Reserva confirmada correctamente."

    def cancelar(self):
        """Cancela una reserva que no haya sido cancelada."""

        if self.__estado == "Cancelada":
            raise ErrorReserva("La reserva ya se encuentra cancelada.")

        self.__estado = "Cancelada"
        return "Reserva cancelada correctamente."

    def procesar(self):
        """Procesa la reserva y controla posibles excepciones."""

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

    def describir(self):
        """Muestra la informacion completa de la reserva."""

        return (
            f"Reserva: {self.__codigo}\n"
            f"Cliente: {self.__cliente.nombre}\n"
            f"Servicio: {self.__servicio.describir()}\n"
            f"Duracion: {self.__duracion}\n"
            f"Estado: {self.__estado}\n"
            f"Costo: ${self.calcular_costo():,.2f}\n"
            f"Fecha: {self.__fecha.strftime('%d/%m/%Y %H:%M')}"
        )
