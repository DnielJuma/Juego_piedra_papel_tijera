# Sistema interactivo  de Piedra, Papel o Tijera

## Información del Proyecto
* **Asignatura:** Lógica de Programación
* **Institución:** Universidad Internacional del Ecuador (UIDE)
* **Autor:** Daniel Alexander Juma Iguago
* **Entorno:** Python ejecutable por consola

---

## Descripción del Sistema y Objetivo
Este proyecto consiste en un programa desarrollado en Python que permite a un usuario jugar al clásico Piedra, Papel o Tijera contra la computadora en rondas consecutivas. 

El objetivo del sistema es aplicar conceptos fundamentales de programación, con condicionales y bucles, y arquitectura de software en tres capas, manteniendo la sesión activa y un marcador acumulado durante toda la partida.

---

## Funcionalidades Principales

1. **Menú por consola:** Muestra las opciones de juego: piedra, papel, tijera y la opción para salir.
2. **Generación aleatoria de la computadora:** Utiliza el módulo `random` para seleccionar la jugada de la máquina de forma aleatoria.
3. **Evaluación de reglas:**
   * Comparación de selecciones para identificar empates.
   * Evaluación de condiciones de victoria del jugador mediante `or`.
   * Victoria automática de la computadora en caso de no cumplirse las condiciones del usuario.
4. **Validación de entradas:** Control para errores que evita fallos si el usuario ingresa textos o números inválidos, solicitándole nuevamente el dato.
5. **Marcador acumulado:** Seguimiento de la partida mostrando victorias, derrotas y empates actualizados tras cada ronda.
6. **Continuidad:** Bucle de validación al final de cada ronda que pregunta si se desea continuar, aceptando únicamente las respuestas "sí" o "no".

---

## Estructura y Arquitectura del Código

El sistema está organizado en **tres capas**:

* **Capa de Presentación:** Manejo de consola a través de `print()` e `input()`, aplicando `.strip()` y `.lower()` para corregir textos
* **Capa de Lógica:** Uso de `random.choice()` para la jugada aleatoria de la computadora y evaluación mediante `if, elif, else` para aplicar las reglas del juego.
* **Capa de Datos y Estado:** Contadores para almacenar el número de victorias, derrotas y empates durante la sesión activa.

---

## Diagramas del Sistema

### Diagrama de Flujo
![Diagrama de Flujo](./Diagrama_flujo.png)

### Arquitectura de Software
![Arquitectura de Software](./Diagrama2.png)

---

## Instrucciones de Ejecución

1. Clonar el repositorio o descargar el archivo `juego.py`.
2. Abrir una terminal o consola de PowerShell en la carpeta del archivo.
3. Ejecutar el siguiente comando:
   ```bash
   python juego.py
