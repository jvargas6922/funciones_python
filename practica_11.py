from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from datetime import datetime

"""
crear un programa en python que me permita simular las funcionalidades de la aplicacion UBER.
    - Funcionalidades:
    Calcular la distancia (KM) (listo)
    Registro de cliente
        Tarifa punta => lunes a jueves 6am a 8am y fines de semana 6pm hasta el domingo a las 00:00 
        Tarifa normal => el resto del tiempo tarifa normal
        valor punta = 700 por km
        valor normal = 500 por km
    Calcular el valor del viaje segun tarifa y distancia (listo)
"""
TARIFA_PUNTA = 700
TARIFA_NORMAL = 500
datos_usuario = {}

def obtener_coordenadas(direccion):
    """
    Obtener las coordenadas (latitud y longitud) de una dirección dada.
        Args:
            direccion (str): La dirección a geocodificar.
        Returns:
            tuple: Una tupla con la latitud y longitud, o un mensaje de error si no se encuentra.
    """
    try:
        geolocator = Nominatim(user_agent="mi_aplicacion_geopy")
        location = geolocator.geocode(direccion)
        if location:
            return (location.latitude, location.longitude)
        else:
            return "Dato no encontrado"
    except Exception as e:
        return f"Error al obtener coordenadas: {e}"
    
def distancia_km(coordenadas_origen, coordenadas_destino):
    """
    Calcular la distancia en kilómetros entre dos puntos dados sus coordenadas.
        Args:
            coordenadas_origen (tuple): Tupla con la latitud y longitud del punto de origen.
            coordenadas_destino (tuple): Tupla con la latitud y longitud del punto de destino.
        Returns:
            float: La distancia en kilómetros entre los dos puntos.
    """
    try:
        return geodesic(coordenadas_origen, coordenadas_destino).km
    except Exception as e:
        return f"Error al calcular la distancia: {e}"
    
def calcular_valor_viaje(distancia):
    try:
        hora_actual = datetime.now().hour
        if hora_actual >= 6 and hora_actual < 8:
            tarifa = TARIFA_PUNTA
        elif hora_actual >= 18 and hora_actual <= 23:
            tarifa = TARIFA_PUNTA
        else:
            tarifa = TARIFA_NORMAL 
    
        return distancia * tarifa
    except Exception as e:
        return f"Error al calcular el valor del viaje: {e}" 
    
def guardar_datos_usuario(nombre,telefono):
    """
    Guardar los datos del usuario en un diccionario.
        Args:
            nombre (str): Nombre del usuario.
            telefono (str): Teléfono del usuario.
        Returns:
            None
    """
    datos_usuario['nombre'] = nombre
    datos_usuario['telefono'] = telefono
    return datos_usuario
"""
Origen (-33.4446507, -70.656077)
destino: (-33.4374154, -70.6512777)
"""    


# solicion del problema con parametros fijos
punto_origen = obtener_coordenadas("Torre Entel, santiago, Chile")
print(f"Coordenadas de origen: {punto_origen}")
punto_destino = obtener_coordenadas("Plaza de Armas, santiago, Chile")
print(f"Coordenadas de destino: {punto_destino}")
distancia = distancia_km(punto_origen, punto_destino)
print(f"La distancia entre el punto de origen y destino es: {distancia} km")
distancia = float(distancia)
print(type(distancia))
valor_viaje = calcular_valor_viaje(distancia)
print(f"El valor del viaje es: {valor_viaje} CLP")




