# FJ ReservaLab

### Sistema Integral de Gestión de Clientes, Servicios y Reservas

**Empresa:** Software FJ  
**Estudiante:** Emmily Daniela Vega Rincón  
**Programa:** Ingeniería de Sistemas  
**Curso:** Programación  
**Actividad:** Fase 4

## Descripción del proyecto

FJ ReservaLab es un sistema desarrollado en Python que permite gestionar clientes, servicios y reservas para la empresa Software FJ.

El proyecto aplica conceptos de programación orientada a objetos, validación de datos, manejo de excepciones y registro de eventos y errores.

## Funcionalidades principales

- Registro y validación de clientes.
- Gestión de servicios especializados.
- Creación, confirmación y cancelación de reservas.
- Cálculo de costos con impuestos y descuentos.
- Control de errores mediante excepciones personalizadas.
- Registro de eventos y errores en un archivo de logs.

## Servicios disponibles

1. **Sala Horizonte:** reserva de salas.
2. **Kit Conecta:** alquiler de equipos tecnológicos.
3. **Código Claro:** asesorías especializadas.

## Organización de los archivos

| Archivo | Descripción |
|---|---|
| `entidades.py` | Clases de entidades y clientes. |
| `excepciones.py` | Excepciones personalizadas. |
| `servicios.py` | Clases de servicios especializados. |
| `reservas.py` | Gestión y procesamiento de reservas. |
| `main.py` | Programa principal y pruebas del sistema. |
| `logs.log` | Registro de eventos y errores. |

## Requisitos

- Python 3 instalado.
- Editor de código, como Visual Studio Code.

## Ejecución del programa

1. Descargar o clonar el repositorio.
2. Abrir la carpeta del proyecto en Visual Studio Code.
3. Abrir una terminal en la carpeta.
4. Ejecutar el siguiente comando:

```bash
python main.py
```

El sistema mostrará los resultados de las operaciones y generará el archivo `logs.log` para registrar los eventos y errores.

## Pruebas realizadas

Se simularon operaciones correctas e incorrectas, entre ellas:

- Registro de clientes válidos e inválidos.
- Creación de servicios válidos e inválidos.
- Creación de reservas exitosas y fallidas.
- Confirmación y cancelación de reservas.
- Cálculo de costos con impuestos y descuentos.
- Control de errores y registro de eventos.

## Repositorio

[Consultar el código fuente en GitHub](https://github.com/EmmilyVega/Fase4)
