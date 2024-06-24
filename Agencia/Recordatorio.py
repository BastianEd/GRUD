# LIBRERIS
import csv


"""
VIDEO DEL TALLER DE PROGRAMACION https://videosduoc.duoc.cl/media/t/1_xtbhwqtt
"""

"""
1) Total de delitos registrados por tipo (estafa, robo, soborno a carabinero).
2) Cantidad de delitos pendientes de juicio.
3) Cantidad de delitos con sujetos en libertad bajo fianza.
4) Listado de delincuentes considerados como 'Sujeto peligroso'.
5) Cantidad de delincuentes con antecedentes previos.
6) Distribución de delitos por edad.
7) Número de delitos cometidos por menores de edad.
8) Número de delitos cometidos por adultos.
9) Delitos por persona – Detalle de todos los delitos cometidos por cada individuo.
10) Frecuencia de delitos por rango de edad (menores de 18, 18-40, 41-60, mayores de 60)

"""

# Cargar CSV Persona
def lectura_csv_persona():
    personas_arreglo = []
    persona_diccionario = []
    with open("Agencia/personas.csv", "r") as archivoCSV:
        leerCSV = csv.reader(archivoCSV, delimiter=":")
        for fila in leerCSV:
            print(fila)
            personas_arreglo.append(fila)

            persona = {
                "rut":fila[0],
                "nombre":fila[1],
                "edad":fila[2]
            }
            persona_diccionario.append(persona)
return personas_arreglo



contador = 0
#Cuantas personas existentes
for persona in personas_arreglo:
    if persona:
        contador += 1
print(contador)

#Cuantas personas existentes menores
for persona in personas_arreglo:
    if int(persona[2]<18):
        contador += 1
print(contador)
#Cuantas personas existentes mayores
for persona in personas_arreglo:
    if int(persona[2]>=18):
        contador += 1
print(contador)

#suma de la edad
#promedio de las edades
#quien es mayor
def buscar_menor():
    el_menor = personas_arreglo[0]
    for persona in personas_arreglo:
        if el_menor[2] > persona[2]:
            el_menor = persona
    return el_menor
print("el menor",buscar_menor())

def buscar_mayor():
    el_mayor = personas_arreglo[0]
    for persona in personas_arreglo:
        if el_mayor[2] < persona[2]:
            el_mayor = persona
    return el_mayor
print("el menor",buscar_menor())



# # Cargar CSV historial delictivo
# def lectura_csv_historial_delitos():
#     historial_delictivo_arreglo = []
#     with open("Agencia/historial_delictivo.csv", "r") as archivoCSV:
#         leerCSV = csv.reader(archivoCSV, delimiter=":")
#         for fila in leerCSV:
#             print(fila)
#             historial_delictivo_arreglo.append(fila)
#     return historial_delictivo_arreglo

# lectura_csv_historial_delitos()

# # lectura_csv_persona()

# def CRUD_Personas():
#     print()














