"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import time
import sys
import controller


from DISClib.ADT import list as lt
assert cf

default_limit = 1000 
sys.setrecursionlimit(default_limit*10)


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar buenos videos por categoría y país")
    print("3- Encontrar video tendencia por categoría")
    print("4- Encontrar video tendencia por país")
    print("5- Buscar los videos con más Likes")
    print("0- Salir")
    
catalog = None


    


def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def printFirstVideo(catalog):
    pvid = controller.firstVideo(catalog)
    infoprim = {"Title": pvid['title'], "channel_title": pvid['channel_title'], 
    "trending_date": pvid['trending_date'], 
    "country": pvid['country'], 
    "views": pvid['views'], 
    "likes": pvid['likes'], 
    "dislikes": pvid['dislikes']}
    return infoprim




"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n(recuerde que antes de escoger cualquier opción tiene que cargar primero la información del catálogo)\n')
    if int(inputs[0]) == 1:
        catalog = controller.initCatalog()
        category = catalog["categories"]
        loadData(catalog)
        pvideo = printFirstVideo(catalog)
        print("Cargando información de los archivos... Esto puede tardar un poco.")
        if catalog == None:
            print("No ha seleccionado una opcion valida")
        else:
            print('Videos cargados: ' + str(lt.size(catalog['ListCompleteVidAll'])))
            print("Información del Primer video: ", pvideo)
            print(category)
            

    elif int(inputs[0]) == 2:
        print ("Encontrar buenos videos por categoría y país")
        size = int(input("¿De que tamaño quiere la lista?: "))
        name = input("¿De que categoría desea saber los videos?: ")
        country = input("¿De que pais desea saber los videos?: ")
        if size > lt.size(catalog['ListCompleteVidAll']):
            print("El numero de muestra seleccionado, excede el tamaño de la cantidad total de elementos que hay")
        else:
            resul = controller.sortVideos(catalog,size,name,country)
            print(resul)


    elif int(inputs[0]) == 3:
        print ("Encontrar video tendencia por categoría")
        controller.newCategory(catalog)
        
    elif int(inputs[0]) == 4:
        print('Encontrar videos tendencias por pais')
    
    elif int(inputs[0]) == 5:
        print('Buscar los videos con mas likes')

    else:
        sys.exit(0)
        
sys.exit(0)

