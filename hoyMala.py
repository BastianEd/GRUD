El destructor 3000--->

Desafío 1: La granja de animales de Patricio
Contexto:
Patricio tiene una granja en Casablanca y planea dibujar la posición de sus animales con él en el centro de masa. Todos sus animales tienen un dispositivo que transmite su posición GPS en grilla 19H, datum WGS84, junto con su peso un una tupla (Peso, X, Y). En su granja está los siguientes animales con su respectivo rango de pesos

Animal	Mínimo inclusive[kg]	Máximo exclusive [kg]
Gallina	1	2
Ganso	2	5
Oveja	20	80
Cerdo	80	400
Caballo	400	800
Finalmente él quiere ubicarse en el centro de masa de sus animales. Ayuda a Patricio a confeccionar el mapa de su granja (en caso de que utilice bibliotecas externas debe agregarlas en requirements.txt)

Parte 1: Clasificación de animales
Implementa función get_determine_animal en utils.py recibiendo como entrada el peso de un animal y como salida el nombre del animal (Primera letra en mayúscula)

Parte 2: Centro de masas
Implementa función get_center_of_mass en utils.py recibiendo como entrada una lista de tuplas de 3 elementos, donde el primer elemento es peso, el segundo es posición este y el tercer es posición norte. La salida debe ser una tupla de 2 elementos, don . Cada numero de la tupla debe ser redondeado a 2 decimales (en el caso de los .005 se aproxima al par más cercano)

Parte 3: Desplegar mapa
Implementa display_map en utils.py para que despliege el mapa usando las imágenes de resources/ (íconos deben convertirse a formato RGBA para conservar colores). Los bordes del mapa son:

Borde	Magnitud[m]	Dirección
Izquierdo	275461.42	E
Derecho	277554.77	E
Inferior	6312575.79	N
Superior	6314565.59	N
BONUS: Redimensiona cada animal de acuerdo a su peso.

Corre los tests con: python granja.py


https://github.com/python-chile/challenge1-pychallenger2024
