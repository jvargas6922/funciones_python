"""
Practica de ejercicios con funciones Termometro
"""

def celsius_a_fahrenheit(temperatura):
    """
    Convierte una temperatura de Celsius a Fahrenheit.

    Parámetros:
    temperatura (float): Temperatura en grados Celsius.

    Retorna:
    float: Temperatura en grados Fahrenheit.
    """
    return (temperatura * 9/5) + 32

temperatura = input("Ingrese la temperatura en grado Celsius: ")
temperatura = float(temperatura)
termometro = celsius_a_fahrenheit(temperatura)
print(f"La temperatura en grados Fahrenheit es: {termometro}")