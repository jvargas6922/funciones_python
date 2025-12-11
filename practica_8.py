"""
    Uso de funciones creadas por el usuario
"""

"""
funcion de calcular el area de una figura geometrica.
    rectangulo:
        area = base * altura
"""

def area_rectangulo(base, altura):
    return base * altura # directo
    # area = base * altura # en variable
    # area = lambda base, altura: base * altura
    # return area

# invocar la funcion
# forma 1: datos estaticos.
# resultado = area_rectangulo(100, 200) # de forma harcodeada
# print(f"Area del rectangulo: {resultado}")

# forma 2: datos dinamicos
# base = input("Ingrese la base del rectangulo: ")
# altura = input("Ingrese la altura del rectangulo: ")
# validar los datos.
# Validar que sean datos numericos, que los datos sean positivos y al final que los datos sean float, que los 2 datos siempre vengan
# resultado_2 = area_rectangulo(base, altura)
# print(f"Area del rectangulo_2: {resultado_2}")


#------------------------------------------------------------------------------------------------
"""
    crear una funcion que me permita poder devolver la informacion de un vehiculo por su nombre.
        Puntos importantes:
        - crear diccionario que tengas por lo menos 10 vehiculos.
        - crear la funcion que me permita filtrar por el nombre del vehiculo.
        - retornar la informacion del vehiculo.
"""
vehiculos = {
    "toyota": {"modelo": "corolla", "año": 2020, "color": "rojo"},
    "honda": {"modelo": "civic", "año": 2019, "color": "azul"},
    "ford": {"modelo": "focus", "año": 2018, "color": "negro"},
    "chevrolet": {"modelo": "malibu", "año": 2021, "color": "blanco"},
    "nissan": {"modelo": "sentra", "año": 2022, "color": "gris"},
    "bmw": {"modelo": "serie 3", "año": 2020, "color": "azul"},
    "audi": {"modelo": "a4", "año": 2019, "color": "rojo"},
    "mercedes": {"modelo": "c300", "año": 2021, "color": "negro"},
    "volkswagen": {"modelo": "jetta", "año": 2018, "color": "blanco"},
    "hyundai": {"modelo": "elantra", "año": 2022, "color": "gris"},
}

def obtener_informacion_vehiculo(nombre):
    informacion = vehiculos.get(nombre.lower())
    if informacion:
        return informacion
    else:
        return "Vehiculo no encontrado."
    
nombre_vehiculo = input("ingrese el nombre del vehiculo: ")
info = obtener_informacion_vehiculo(nombre_vehiculo)
print(f"Informacion del vehiculo: {info}")

#------------------------------------------------------------------------------------------------
"""
    La funciones declaradas por el usuario reciben parametros que son obligatorios o opcionales.
"""
# funcion con parametros opciones
def obtener_informacion_vehiculo_2(nombre="Toyota"):
    informacion = vehiculos.get(nombre.lower())
    if informacion:
        return informacion
    else:
        return "Vehiculo no encontrado."