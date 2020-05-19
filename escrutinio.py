# Escenario: mundial de marcas de autos realizado en twitter por Miura Mag (@miuramag)

import csv

# Diccionario para guardar los datos
dicc = {}
# Lectura del archivo de datos
with open("candidatos.csv") as datos:
    reader = csv.reader(datos)
    next(reader)  # Se ignora la cabecera
    for marca, votos in reader:
        dicc[marca] = int(votos)
    datos.close()

#print(dicc)

# Determinar el ganador
suma = 0
mayor = 0
ganador = ''
for elemento in dicc:
    if (dicc[elemento] > mayor):
        mayor = dicc[elemento]  #votos
        ganador = elemento      #nombre
    suma += dicc[elemento]

# Impresión de resultados
for elemento in dicc:
    porcentaje = (dicc[elemento]*100)/suma
    print(elemento + ' - ' + str(dicc[elemento]) + ' votos - ' + str(porcentaje) + '%')

print('Ganador del mundial de marcas de autos: ' + ganador + ' con ' + str(mayor) + ' votos.')