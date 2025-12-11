"""
funciones lambda
"""
"""
Estructura
    suma = lambda a,b: a + b 
    suma = variable donde vamos a guardar el valor resultante de la funcion
    lambda = palabra reservada para definir una funcion anonima
    a,b = parametros de la funcion
    a + b = cuerpo de la funcion, operacion que realiza la funcion
"""
# estructura basica de una funcion lambda
# suma = lambda a,b: a + b
# print(f"el resulatdo de la suma es: {suma(5,3)}") 

# multiplicacion = lambda a,b: a * b
# print(f"el resultado de la multiplicacion es: {multiplicacion(5,3)}")

# uso de la funcion nativa map con funciones lambda
"""
estructura:
    numeros = [1,2,3,4,5]
    cuadrados = list(map(lambda x: x**2, numeros))
    numeros = lista de numeros a los que se les va a aplicar la funcion lambda
    cuadrados = variable donde se guarda el resultado de la operacion
    map = funcion nativa de python que aplica una funcion a cada elemento de una lista
    lambda x: x**2 = funcion lambda que eleva al cuadrado cada elemento de la lista
"""

# numeros = [1,2,3,4,5]
# cuadrados = list(map(lambda x: x**2, numeros))
# print(f"los cuadrados de los numeros son: {cuadrados}")

# uso de la funcion nativa filter con funciones lambda
"""
estructura:
    numeros = [1,2,3,4,5]
    pares = list(filter(lambda x: x%2 == 0, numeros))
    numeros = lista de numeros a los que se les va a aplicar la funcion lambda
    pares = variable donde se guarda el resultado de la operacion
    filter = funcion nativa de python que filtra los elementos de una lista segun una condicion
    lambda x: x%2 == 0 = funcion lambda que filtra los numeros pares

"""

numeros = [1,2,3,4,5]
pares = list(filter(lambda x: x%2 == 0, numeros))
print(f"los numeros pares son: {pares}")

# ejemplo de lambda con varias validaciones
"""
    estructura:
    prueba = lambda x: x**2  if x > 0 else -x
    prueba = variable donde se guarda el resultado de la funcion
    lambda x: x**2  if x > 0 else -x = funcion lambda que eleva al cuadrado el numero si es mayor a 0, de lo contrario devuelve el valor negativo del numero



"""
prueba = lambda x: x**3  if x > 0 else -x
print(prueba(-5))