"""
Cree un codigo que pueda resolver las operaciones para dar la cuenta en un restaurante.
"""
"""
Entrada:
    ingresar los montos de la comida y bebidas
Proceso:
     hacer los calculos necesarios para obtener el total a pagar
Salida:
    mostrar el total a pagar incluyendo impuestos y propina
"""

"""
precios = [comida1, comida2, bebida1, bebida2] # valores numericos
 = suma(precios)

"""
# trabajador que nos entrega el iva indiferente del monto  OJO siempre y cuando el valor sea numérico
def iva(monto):
    return monto * 0.19

# trabajador que nos entrega la propina indiferente del monto OJO siempre y cuando el valor sea numérico
def propina(monto):
    return monto * 0.10

precios =[]
comida_1 = float(input("Ingrese el monto de la comida 1: "))
precios.append(comida_1)
comida_2 = float(input("Ingrese el monto de la comida 2: "))
precios.append(comida_2)
bebida_1 = float(input("Ingrese el monto de la bebida 1: "))
precios.append(bebida_1)
bebida_2 = float(input("Ingrese el monto de la bebida 2: "))
precios.append(bebida_2)

subtotal = sum(precios)
impuesto = iva(subtotal)
propina_total = propina(subtotal)
total_a_pagar = subtotal + impuesto + propina_total

print(f"Subtotal: {subtotal:.2f}")
print(f"Impuesto (IVA): {impuesto:.2f}")
print(f"Propina: {propina_total:.2f}")
print(f"Total a pagar: {total_a_pagar:.2f}")