#Librerias
import csv


"""
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
def Lectura_csv_persona():
    # Diccionario de persona
    personas_diccionario = []
    # Lectura de archivo
    with open("Agencia/personas.csv", "r") as archivoCSV:
        leerCSV = csv.reader(archivoCSV, delimiter=",")
        for fila in leerCSV:
            #aqui ordenas el orden de la fformacion 
            fila = {
                "rut": fila[0],
                "nombre": fila[1],
                "edad": int(fila[2])  # Convertir la edad a entero
            }
            personas_diccionario.append(fila)
            print(fila)
    return personas_diccionario

# Función para buscar la persona más joven
def buscar_menor(personas_diccionario):
    el_menor = personas_diccionario[0]
    for persona in personas_diccionario:
        if el_menor["edad"] > persona["edad"]:
            el_menor = persona
    return el_menor
    
# Función para buscar la persona más vieja
def buscar_mayor(personas_diccionario):
    el_mayor = personas_diccionario[0]
    for persona in personas_diccionario:
        if el_mayor["edad"] < persona["edad"]:
            el_mayor = persona
    return el_mayor

# Llamar a la función para cargar los datos
personas_diccionario = Lectura_csv_persona()

# Buscar la persona más joven y más vieja
print("La persona más joven es:", buscar_menor(personas_diccionario))
print("La persona más vieja es:", buscar_mayor(personas_diccionario))



# #1) Total de delitos registrados por tipo (estafa, robo, soborno a carabinero).
# def total_delitos_tipo():
#     estafa = 0
#     robo = 0
#     soborno = 0
#     with open("historial_delictivo.csv", "r") as archivoCSV:
#         leerCSV = csv.reader(archivoCSV, delimiter=":")
#         for fila in leerCSV:
#             if fila[1] == "estafa":
#                 estafa += 1
#             elif fila[1] == "robo":
#                 robo += 1
#             elif fila[1] == "soborno":
#                 soborno += 1
#     print("Estafa: ", estafa)
#     print("Robo: ", robo)
#     print("Soborno: ", soborno)