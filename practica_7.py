"""
Explorando funciones Lambda
➔ Utilizar funciones lambda junto con map() y filter() para procesar datos sobre actividad física y recomendar snacks personalizados.
1. Contexto inicial:
    ● Simulamos que tenemos una lista de calorías quemadas por distintas personas tras hacer ejercicio.
2. Uso de map() con lambda:
    ● Queremos transformar esa lista a categorías según el gasto energético:
        ○ Menos de 150 → "Snack liviano"
        ○ Entre 150 y 300 → "Barrita energética"
        ○ Más de 300 → "Smoothie o batido"
    Usamos map() con una lambda que contenga un condicional con if...else. 
3. Uso de filter() con lambda:
    ● Extraer solo los entrenamientos intensos (más de 300 cal).
4.Refuerzo del concepto de expresión única:
    ● Mostrar por qué no podemos tener múltiples líneas o print()s dentro de una lambda.
"""

calorias = [125, 150, 180, 200, 220, 250, 275, 299, 300, 315, 330, 390]