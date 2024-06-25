#LIBRERIAS
import json

# import funciones
def leer_json():
    #Arreglo pal Profe
    arregloPalProfe=[]
    with open('biblioteca.json', mode="r") as file:
        lectura = json.load(file)
        for libros in lectura["Libro"]:
            arregloPalProfe.append(libros)
            # print(arregloPalProfe)
        return arregloPalProfe
# leer_json()


def agregar_libro():
    with open('biblioteca.json', mode="r") as file:
        lectura = json.load(file)
    #crear nuevo libro
        nuevo_libro = {
            "LibroID": len(lectura["Libro"]) + 1,
            "Titulo": input('Ingresa el Titulo del libro: '),
            "AutorID": len(lectura["Autor"])+1,
            "CategoriaID": len(lectura["Categoria"])+1,
            "AnoPublicacion": int(input('Ingrese el año del libro: ')),
            "ISBN": input('Ingrese el ISBN: ')
        }
    # Agregar el nuevo libro a la lista de libros
        lectura["Libro"].append(nuevo_libro)
    # Escribir de nuevo en el archivo JSON ------> SOBREESCRIBIR LOS NUEVOS CAMBIOS
    with open('biblioteca.json', mode="w") as file:
        json.dump(lectura, file, indent=4)
    #agregar nuevo libro a la lista de libro
# agregar_libro()

# • Editar libro
# Al listado de libros en el Json, editamos la información (Título, AutorID, CategorialD, AnoPublicacion).



# • Eliminar libro
# Al listado de libros en el Json, eliminamos un libro por su ID.
def eliminador_inador():
    with open("biblioteca.json", mode="r") as file:
        datos= json.load(file)
        id_buscada=input("Ingresa la id a buscar: ")
        if id_buscada in datos["Libro"]:
            del(datos[id_buscada])
    with open("biblioteca.json","w") as file:
        json.dump(datos, file, indent = 4)

# eliminador_inador()



def eliminar_libro():
    #Buscar el ID del Libro
    id_libro = int(input("Ingresa el ID a eliminar: "))#numero guardado en el espacio imaginario
    #Abrir el archivo
    with open('biblioteca.json', mode="r") as file:
        lectura = json.load(file)
        
    with open('biblioteca.json', mode="r") as files:
        for libros in lectura["Libro"]:
            if id_libro == libros["LibroID"]:
                print(libros)
                # lectura["Libro"].remove(["Libro"][libros])
                # lectura = json.dump(lectura,files, indent=4)


# Buscar el ID del Libro


eliminar_libro()
