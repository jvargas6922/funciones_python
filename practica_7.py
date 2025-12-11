"""
Explorando funciones Lambda
➔ Utilizar funciones lambda junto con map() y filter() para procesar datos sobre actividad física y recomendar snacks personalizados.
1. Contexto inicial:
    ● Simulamos que tenemos una lista de calorías quemadas por distintas personas tras hacer ejercicio.(listo)
2. Uso de map() con lambda:
    ● Queremos transformar esa lista a categorías según el gasto energético: (listo)
        ○ Menos de 150 → "Snack liviano"
        ○ Entre 150 y 300 → "Barrita energética"
        ○ Más de 300 → "Smoothie o batido"
    Usamos map() con una lambda que contenga un condicional con if...else. 
3. Uso de filter() con lambda:
    ● Extraer solo los entrenamientos intensos (más de 300 cal).
4.Refuerzo del concepto de expresión única:
    ● Mostrar por qué no podemos tener múltiples líneas o print()s dentro de una lambda.
"""

# Punto 1: Lista de calorías quemadas
calorias = [125, 150, 180, 200, 220, 250, 275, 299, 300, 315, 330, 390]
"""
    Estructura de categorias
    1) < 150 => 125
    2) 150 - 300 => 150, 180, 200, 220, 250, 275, 299, 300
    3) > 300 => 315, 330, 390
"""


# Punto 2: uso de map() con lambda para categorizar snacks
"""
estructura de funcion
    categorias_snacks = list(map(lambda x: "Snack liviano" if x < 150 else 
                                       "Barrita energética" if 150 <= x <= 300 else 
                                       "Smoothie o batido", calorias))

    categorias_snacks => variable que me permite almacenar el resultado de la funcion map
    list() => convierte el objeto map en una lista
    map() => aplica la funcion lambda a cada elemento de la lista calorias
    Condiciones: 
        "Snack liviano" if x < 150 else => si x es menor a 150, devuelve "Snack liviano"
        "Barrita energética" if 150 <= x <= 300 else => si x esta entre 150 y 300, devuelve "Barrita energética"
        "Smoothie o batido" => si x es mayor a 300, devuelve "Smoothie o batido"

"""
categorias_snacks = list(map(lambda x: "Snack liviano" if x < 150 else 
                                       "Barrita energética" if 150 <= x <= 300 else 
                                       "Smoothie o batido", calorias))
print(f"Categorías de snacks según calorías quemadas: {categorias_snacks}")

# Punto 3: uso de filter() con lambda para extraer entrenamientos intensos
entrenamiento_intenso = list(filter(lambda x: x > 300, calorias))
print(f"Entrenamientos intensos (más de 300 cal): {entrenamiento_intenso}") 

# Punto 4: Refuerzo del concepto de expresión única en lambda
# Ejemplo incorrecto (esto generaría un error si se descomenta)
incorrecto = lambda x: print(x)  # No se puede usar print dentro de una lambda