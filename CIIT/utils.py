# from PIL import Image

#Tupla
Peso_Animales = [
    (1, 'Gallina'),
    (1.5, 'Gallina'),
    (2, 'Ganso'),
    (3.5, 'Ganso'),
    (20, 'Oveja'),
    (50, 'Oveja'),
    (80, 'Cerdo'),
    (240, 'Cerdo'),
    (400, 'Caballo'),
    (600, 'Caballo'),
]

def get_determine_animal():
    pesoAnimal = float(input("Ingrese el peso del animal: "))
    if pesoAnimal >= 1 and pesoAnimal<2:
        print("Tu animal es un:",Peso_Animales[0][1])
    elif pesoAnimal >= 2 and pesoAnimal<5:
        print("Tu animal es un:",Peso_Animales[2][1])
    elif pesoAnimal >= 20 and pesoAnimal<80:
        print("Tu animal es un:",Peso_Animales[4][1])
    elif pesoAnimal >= 80 and pesoAnimal<400:
        print("Tu animal es un:",Peso_Animales[6][1])
    elif pesoAnimal >= 400 and pesoAnimal<800:
        print("Tu animal es un:",Peso_Animales[8][1])
    pass

get_determine_animal()
def get_center_of_mass(positions):
    pass

def display_map(positions):
    image = Image.open('resources/mapa.png').convert("RGBA")
    return image
