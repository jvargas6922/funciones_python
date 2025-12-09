"""
crea un programa que me permita guardar los nombres de los pokemons en un archivo de texto llamado pokemons.txt. El programa debe permitir al usuario agregar nuevos nombres de pokemons, ver la lista completa de pokemons guardados.
"""
"""
libreria os: me permite interactuar con el sistema operativo, como manejar archivos y directorios.

"""
import os # Permite interactuar con el sistema operativo
import requests # Permite hacer solicitudes HTTP

"""
Paso 1: 
    Importar las librerias necesarias para completar el programa.
Paso 2:
    Hacer la peticion a la API de pokemons para obtener los nombres de los pokemons.
Paso 3:
    Crear una funcion para guardar los nombres de los pokemons en un archivo de texto.
Paso 4:
    Crear una funcion para leer y mostrar los nombres de los pokemons guardados en el archivo texto.
"""

"""
with open("pokemons.txt", "a") as archivo: (abre el archivo en modo agregar)
archivo.write(nombre + "\n") (escribe el nombre del pokemon en el archivo seguido de un salto de linea)
"""
def guardar_pokemon(nombre):
    """Guarda el nombre de un pokemon en el archivo pokemons.txt"""
    with open("pokemons.txt", "a") as archivo: # el alias me permite poder referenciar el archivo
        archivo.write(nombre + "\n")
    print(f"Pokemon '{nombre}' guardado exitosamente.")


"""
Peticiones HTTP:
    (GET): para obtener datos de un servidor web.
    (POST): para enviar datos a un servidor web.
    (PUT): para actualizar datos en un servidor web.
    (DELETE): para eliminar datos en un servidor web.
"""
url = 'https://pokeapi.co/api/v2/pokemon'
response = requests.get(url)
# print(response.json())
data = response.json()
for pokemon in data['results']:
    guardar_pokemon(pokemon['name'])# invocar la funcion guardar_pokemon y pasarle por parametro el nombre del pokemon



# Leer el archivo creado y mostrar su contenido
def mostrar_pokemons():
    """Muestra la lista completa de pokemons guardados en el archivo pokemons.txt"""
    if os.path.exists("pokemons.txt"):
        with open("pokemons.txt", "r") as archivo:
            pokemons = archivo.readlines()
            print("Lista de Pokemons guardados:")
            for pokemon in pokemons:
                print(pokemon.strip())
    else:
        print("No hay pokemons guardados aún.")

mostrar_pokemons()

"""
Pasos para crear un entorno virtual en Python:
instalar virtualenv si no lo tienes: pip install virtualenv (comandos  pip install virtualenv)
crear el entorno virtual: virtualenv nombre_del_entorno (comando virtualenv env)
ingresar al entorno virtual:
    en Windows: .\nombre_del_entorno\Scripts\activate
    en Mac/Linux: source nombre_del_entorno/bin/activate
salir del entorno virtual: deactivate
"""