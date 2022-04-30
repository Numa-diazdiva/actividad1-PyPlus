import csv
from collections import Counter

#  Abro el archivo con la ruta relativa, asumiendo que está en la misma carpeta
arch = open('TOTAL_nuevo.csv', 'r')
#  Instancio el lector csv y remuevo el encabezado del archivo, guardándolo en caso de que sea necesario.
lector = csv.reader(arch)
encabezado = lector.__next__()


def obtener_usuarios_frecuentes(lect):
    # Utilizo la sintaxis de lista por comprensión para guardar únicamente el string de cada nombre de usuario en una nueva lista
    lista_usuarios_reducida = [usuario[1] for usuario in lect]
    # Creo un contador y llamo al método que me retorna una tupla con los ítems que más veces aparecen y cuántas veces aparecen
    contador = Counter(lista_usuarios_reducida)
    usuarios_mas_frecuentes = contador.most_common(3)
    return usuarios_mas_frecuentes


mas_frecuentes = obtener_usuarios_frecuentes(lector)

# Imprimo los usuarios más frecuentes y la cantidad de apariciones que tuvo cada uno
print('Los usuarios más frecuentes son: ')
for usuario in mas_frecuentes:
    print(f'Usuario: {usuario[0]}, con {usuario[1]} registros de actividad.')


arch.close()
