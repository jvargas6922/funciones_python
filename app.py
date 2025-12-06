"""
Funciones en python
estructura
    1- Funciones sin parametros
    def nombre_funcion():
        instrucciones
        return valor_a_devolver

    2- Funciones con parametros
    def nombre_funcion(parametro_1, parametro_2):
        instrucciones
        return valor_a_devolver
"""
# definir la funcion
def saludo():
    print("Hola mundo!!")
    # return "Hola mundo!!"

# llamado de la funcion
print(saludo())


#defino la funcion con parametros
def promedio_1(a, b):
    return(a + b)/2

# funcion aplicable para cualquier tipo de notas
def promedio_2(notas, cantidad):
    # a = sumatoria de notas
    # b = cantidad de notas
    return (notas/cantidad)


# nota_1 = input("Ingrese la primera nota: ")
# nota_2 = input("Ingrese la segunda nota: ")
# nota_1 = 4
# nota_2 = 5
# nota_3 = 6
# nota_4 = 4
# nota_5 = 5
# nota_6 = 7
# notas = [4,5,6,4,5,7,8,1]
# print(f"El promedio_1 de las notas es: {promedio_1(float(nota_1), float(nota_2))}")
# print(f"El promedio_2 de las notas es: {promedio_1(float(nota_3), float(nota_4))}")
# print(f"El promedio_3 de las notas es: {promedio_1(float(nota_5), float(nota_6))}")
# print(f"El promedio_4 de las notas es: {promedio_1(float(nota_1), float(nota_6))}")
# print(f"El promedio de las notas es: {promedio_2(sum(notas), len(notas))}")
#                                                   a             b

def validar_cuenta_correo_electronico(correo):
    """
    Esta funcion valida si una cuenta de correo electronico es valida
    Parametros:
        correo: str -> cuenta de correo electronico
    Retorna:
        bool -> True si es valida, False si no lo es
    """
    if "@" in correo and "." in correo:
        return True
    else:
        return False


# correo = input("Ingrese una cuenta de correo electronico: ")
# if validar_cuenta_correo_electronico(correo):
#     print(f"La cuenta de correo electronico {correo} es valida")
# else:
#     print(f"La cuenta de correo electronico {correo} no es valida")  


def calcular_digito_verificador(rut_cuerpo):
    """Calcula el dígito verificador de un RUT."""
    # Convierte el número a una lista de dígitos en orden inverso
    digitos = [int(d) for d in str(rut_cuerpo)][::-1]
    suma = 0
    multiplicador = 2
    for digito in digitos:
        suma += digito * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    
    resto = suma % 11
    digito_verificador = 11 - resto
    
    if digito_verificador == 11:
        return '0'
    elif digito_verificador == 10:
        return 'K' # verison_1 = 19875653-K version_2 = 19875653-k
    else:
        return str(digito_verificador)

def validar_rut(rut_completo):
    """Valida un RUT completo (número-DV) sin librerías externas."""
    if '-' not in rut_completo or rut_completo.count('-') > 1:
        return False # Formato inválido

    partes = rut_completo.split('-')
    if len(partes) != 2:
        return False # No tiene exactamente una división

    rut_numero_str = partes[0].replace('.', '') # Elimina puntos si existen
    dv_ingresado = partes[1].upper() # Convierte a mayúsculas (para K)

    if not rut_numero_str.isdigit():
        return False # El cuerpo no es solo números

    dv_calculado = calcular_digito_verificador(rut_numero_str)
    
    return dv_calculado == dv_ingresado

# Ejemplos de uso:
print(f"76086428-5 es válido: {validar_rut('76086428-5')}") # Salida: True
print(f"19875653-K es válido: {validar_rut('19875653-K')}") # Salida: True
print(f"12345678-9 es válido: {validar_rut('12345678-9')}") # Salida: False
print(f"1-9 es válido: {validar_rut('1-9')}") # Salida: True (ejemplo simple)
print(f"19875653-k es válido (minúscula): {validar_rut('19875653-k')}") # Salida: True
print(f"19875653-K es válido: {validar_rut('19.875.653-K')}") # Salida: False