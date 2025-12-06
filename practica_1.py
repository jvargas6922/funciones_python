"""
Vamos a crear nuestras primeras funciones personalizadas en Python, paso a paso. El objetivo es entender la estructura
de una función (def), cómo se escribe su cuerpo indentado, cómo se invoca, y cómo puede o no recibir parámetros.
Parte 1 – Crear una función básica sin parámetros(listo)
    ● Mostramos cómo usar def
    ● Escribimos una función saludar() que imprima un mensaje
    ● Ejecutamos varias veces su invocación
    ● Discutimos por qué es útil reutilizar funciones

Parte 2 – Función que retorna un valor(listo)
    ● Creamos una función multiplicar(a, b) que retorne el resultado
    ● Leemos dos números con input()
    ● Mostramos el resultado llamando a la función
    ● Explicamos la diferencia entre mostrar y retornar

Parte 3 – Crear una función con parámetros
    ● Definimos una función bienvenida(nombre)
    ● Le pedimos al usuario su nombre
    ● Llamamos a la función pasándole ese valor
    ● Mostramos cómo el mensaje cambia dinámicamente
"""

#1 funcion sin parametros
# def saludar():
#     print("¡Hola! Bienvenido a la práctica de funciones en Python.")

# #invocar la funcion que tiene un print interno
# saludar()

# #2 funcion con parametros
# def multiplicar_1(valor_1, valor_2):
#     return valor_1 * valor_2

# def multiplicar_2(valor_1, valor_2):
#     print(valor_1 * valor_2)

# dato_1 = int(input("Ingrese el primer número a multiplicar: "))
# dato_2 = int(input("Ingrese el segundo número a multiplicar: "))
# print(f"El resultado de la multiplicación es: {multiplicar_1(dato_1, dato_2)}")
# # Caso 2:
# print("Segundo Caso sin retorno:")
# multiplicar_2(dato_1, dato_2)


# print("Caso con el retunn:")
# resultado = multiplicar_1(dato_1, dato_2)
# operacion = resultado + 10
# print(f"El resultado de la operación (multiplicación + 10) es: {operacion}")

# print("Caso sin el retunn:")
# print("Caso con el retunn:")
# resultado_2 = multiplicar_2(dato_1, dato_2)
# operacion = resultado_2 + 10
# print(f"El resultado de la operación (multiplicación + 10) es: {operacion}")


# 3 funcion parametrizada
def bienvenida(nombre):
    # return f"¡Bienvenido/a, {nombre}, a la práctica de funciones en Python!"
    print(f"¡Bienvenido/a, {nombre}, a la práctica de funciones en Python!")

nombre_usuario = input("Por favor, ingresa tu nombre: ")
bienvenida(nombre_usuario)