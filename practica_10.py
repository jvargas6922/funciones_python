"""
Calculo del area de un triangulo
"""
def area_triungulo(base, altura):
    """
    Calcula el área de un triángulo.

    Parámetros:
    base (float): La base del triángulo.
    altura (float): La altura del triángulo.

    Retorna:
    float: El área del triángulo.
    """
    return (base * altura) / 2

print("Calculo de area de un triangulo")
base = input("Ingrese la base del triangulo: ")
# validar el tipo de dato
base = float(base)
altura = input("Ingrese la altura del triangulo: ")
# validar el tipo de dato
altura = float(altura)
area = area_triungulo(base, altura)
print(f"El area del triangulo es: {area}")