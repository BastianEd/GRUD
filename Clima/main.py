#Librerias
import json

#crear en archivos json 
def crear_Json():
    with open('reportes.json', mode='a') as archivoJson:
        json.dump(archivoJson)
    reporte={}

        #Escribir de nuevo en el archivo JSON
    with open("compras.json", mode="w") as file:# Es CON 'W' para SobreEscribrir CTM no la 'a'
        json.dump(datos, file, indent=4)

#Arreglar los precios en JSON
with open("compras.json", "r") as patito:
    datos=json.load(patito)

unitario={
    productos["id"]:productos["precio"] 
    for productos in datos["productos"]
    }

for detalle in datos["detalle_boletas"]:
    for total in detalle:
        id_producto = detalle["id_producto"]
        cantidad = detalle["cantidad"]
        precio_producto = unitario.get(id_producto,0)
        total_producto = cantidad * precio_producto
        detalle["total"] = total_producto

totales_finales={}

for detalle in datos["detalle_boletas"]:
    id_boleta=detalle["id_boleta"]
    if id_boleta not in totales_finales:
        totales_finales[id_boleta]=0
    totales_finales[id_boleta]+=detalle["total"]

for boleta in datos["boletas"]:
    id_boleta=boleta["id_boleta"]
    total_boleta=totales_finales.get(id_boleta,0)
    boleta["total"]=total_boleta

with open("compras.json", "w") as patito:
    json.dump(datos, patito, indent=4)


# #agregar datos en archivo json
def agregar_a_json():
    with open("compras.json",mode="r") as file:
        datos =json.load(file)
    #Crear nuevo producto
        nuevo_producto = {
            "id":len(datos["productos"])+1,
            "nombre": input('Ingrese el nombre del Producto: '),
            "precio": int(input('Precio del producto: '))
        }    
        #Agregar el nuevo producto a l json Compras
        datos["productos"].append(nuevo_producto)
        #Escribir de nuevo en el archivo JSON
    with open("compras.json", mode="w") as file:# Es CON 'W' para SobreEscribrir CTM no la 'a'
        json.dump(datos, file, indent=4)
agregar_a_json()

#EDITAR EN EL JSON PRODUCTOS
def editar_Json():
    with open('compras.json', mode="r") as file:
        lectura = json.load(file)
        idInput = int(input("ingrese la id del producto que desee modificar :"))
        for producto in lectura["productos"]: 
            if producto["id"] == idInput:
                #Variables que almacenen los nuevos valores para el nombre y el precio
                nombre = str(input("Ingresa el nuevo nombre: "))
                precio = int(input("Ingresa el nuevo precio: "))
                #indicar los nuevos parametros en el json
                producto["nombre"]=nombre
                producto["precio"]=precio
        #Escribir de nuevo en el archivo JSON
    with open("compras.json", mode="w") as file:# Es CON 'W' para SobreEscribrir CTM no la 'a'
        json.dump(lectura, file, indent=4) 
# editar_Json()

#leer en archivos json
def lectura_json():
    with open('compras.json', mode='r') as archivoJson:
        lectura = json.load(archivoJson)
        for fila in lectura["productos"]:
            print("Producto:")
            print(fila)
# lectura_json()

#borrar en archivos json
def borrar_producto():
    with open("compras.json",mode="r") as file:
        lector=json.load(file)
        id_input=int(input("Ingresa el id del producto a eliminar: "))
        producto_a_eliminar = None
        for producto in lector["productos"]:
            if producto["id"] == id_input:
                producto_a_eliminar = producto
                lector["productos"].remove(producto_a_eliminar)
        #Escribir de nuevo en el archivo JSON
    with open("compras.json", mode="w") as file:# Es CON 'W' para SobreEscribrir CTM no la 'a'
        json.dump(lector, file, indent=4) 

# borrar_producto()

'''
def borrar_producto():
    with open("compras.json", mode="r") as file:
        lector = json.load(file)

        id_input = int(input("Ingresa el id del producto a eliminar: "))

        producto_a_eliminar = None

        for producto in lector["productos"]:
            if producto["id"] == id_input:
                producto_a_eliminar = producto
                break
        if producto_a_eliminar:
            lector["productos"].remove(producto_a_eliminar)
        else:
            print("Producto no encontrado.")

    with open("compras.json", mode="w") as file:
        json.dump(lector, file, indent=4)

borrar_producto()
'''




'''
def editar_producto(idPar:int,nombrePAr:str,precioPar:int):
    with open("compras.json", mode="r") as lecturaJson:
        leerJson = json.load(lecturaJson)
        # print(leerJson["productos"])#se le puede pedir al usuario 
        contador = 0
        for i in leerJson["productos"]:
            # print(i["precio"],i["nombre"])
            if i["id"] == idPar:
                print("el Producto esta en --------->", contador)
                break
            contador += 1
            editar_producto(1,"",1)

        leerJson["productos"][contador]["nombre"]=nombrePAr
        leerJson["productos"][contador]["precio"]=precioPar
    with open ("compras.json",mode="w") as escribirJson:
        json.dump(leerJson,escribirJson,indent=4)

'''