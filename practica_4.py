"""
Explorando funciones nativas de Python
Vamos a realizar un recorrido práctico por varias de las funciones nativas más usadas de Python. En cada paso:
    ➔ Introducimos una función nativa
    ➔ Mostramos un ejemplo simple en código
    ➔ Desafiamos al grupo con una pregunta o prueba rápida

Parte 1 – Funciones de conversión y tipo
    ● int(), float(), str(), bool()
    ● Convertir strings a números y viceversa
    ● ¿Qué devuelve bool(""), bool(0), bool("Hola")?

Parte 2 – Verificación de tipos
    ● type() e isinstance()
    ● Mostrar cómo saber el tipo de una variable
    ● Preguntar: ¿Cuál es la diferencia entre type() e isinstance()?
"""

# Parte 1
# ejemplo funcion int()
# num_1 = input("Ingrese el primer numero: ")
# num_2 = input("Ingrese el segundo numero: ")
# num_3 = input("Ingrese el tercer numero: ") 

# suma = int(num_1) + int(num_2) + int(num_3)
# print(f"El resultado de la suma es: {suma}")

# ejemplo funcion float()
# costo_kilo = 1000

# peso_paquete = input("Ingrese el peso del paquete en kilos: ")
# costo_envio = costo_kilo * float(peso_paquete)
# print(f"El costo de envio es: {costo_envio}")

# ejemplo funcion str()
# nombre = input("Ingrese su nombre: ")
# edad = input("Ingrese su edad: ")
# peso = input("Ingrese su peso: ")
# # mensaje = "Hola " + nombre + ", tienes " + str(edad) + " años."
# mensaje = "Hola " + nombre + ", tienes " + str(edad) + " y pero " + str(peso) +  " años."
# print(mensaje)
# print(f"hola {nombre}, tienes {edad} años y tu peso es de {peso}.")

# ejemplo funcion bool()
# password_correcto = 12345
# password = int(input("Ingrese la contraseña: "))

# if bool(password == password_correcto): # True, False
#     print("Acceso concedido")
# else:
#     print("Acceso denegado")


# if bool(password): # True, False
#     print("Acceso concedido")

# Parte 2
# vamos a llamar a la api de pokemon.
# la url = https://pokeapi.co/api/v2/pokemon
# import requests
# response = requests.get("https://pokeapi.co/api/v2/pokemon")
# data = response.json()
# print(type(data))
# for pokemon in data["results"]:
#     if(pokemon['name'] == 'raticate'):
#         print(pokemon['name'])
#     # print(isinstance(pokemon, dict))

#Parte 3
# len()
# numeros = [10,50,5,20,70,30]
# cantidad_datos = len(numeros)
# print("La cantidad de datos es:", cantidad_datos)

#list()
# saludo = "Hola Mundo"
# lista_saludo = list(saludo)
# print("Lista saludo:", lista_saludo)

# dict()
# estudiante = [("nombre", "Ana"), ("edad", 22), ("carrera", "Ingeniería")]
# print(type(estudiante))
# dict_estudiante = dict(estudiante)
# print("Diccionario estudiante:", dict_estudiante)

# tuple()
# cadena = ["curso", "python"]
# tupla_cadena = tuple(cadena)
# print("Tupla cadena:", tupla_cadena)

# print() y input()
# usuario = input("Ingrese su nombre: ")
# print("Hola", usuario, "¡Bienvenido al curso de Python!")

# round()
# nota = 8.77
# nota_final = round(nota)
# print("La nota final es:", nota_final)

# range()
for i in range(1, 6):
    print("Iteración número:", i)

