"""
Funciones nativas en python
"""
numeros = [10,50,5,20,70,30]

# funcion nativa min()
valor_minimo = min(numeros)
print("El valor minimo es:", valor_minimo)

# funcion nativa max()
valor_maximo = max(numeros)
print("El valor maximo es:", valor_maximo)

# funcion nativa sum()
sumatoria = sum(numeros)
print("La sumatoria es:", sumatoria)

# funcion nativa len()
longitud = len(numeros)
print("La longitud de la lista es:", longitud)

# funcion nativa sorted()
lista_ordenada = sorted(numeros) # Ordenar de mayor a menor
print("La lista ordenada es:", lista_ordenada)
print("La lista descendente es:", sorted(numeros, reverse=True))

# funcion nativa slice()
rut = "12345678-9"
# quiero cortar la cadena por el '-'
partes = rut.split('-')
print("Las partes del RUT son:", partes)

# otro ejemplo de slice
nombre = "Joffred vargas, edad 25 años, ciudad santiago, pais chile"
datos = nombre.split(',')
edad = datos[1].split(' ') # edad[2]
ciudad = datos[2].split(' ') # ciudad[2]
pais = datos[3].split(' ') # pais[2]
print("La edad es:", edad)
print("Los datos son:", datos)
print("La ciudad es:", ciudad)
print("El pais es:", pais)
print(f"Mi nombre es {datos[0]} mi edad es {edad[2]} años, vivo en la ciudad de {ciudad[2]} y mi pais es {pais[2]}")


# funcion nativa replace()
rut = "15.654.987-5" # 15654987-5
rut_2 = "15654987-5"
# rut 2 contiene puntos?
if '.' in rut_2:
        rut_formato = rut.replace('.','')
else:
        rut_formato = rut_2
print(f" nuevo formato de RUT es: {rut_formato}")

# funcion nativa upper() y lower()

rut_3 = "15.654.987-k"
rut_formato_3 = rut_3.replace('.','').upper()
print(f" nuevo formato de RUT es: {rut_formato_3}")

