﻿#channel_title = information_videos
#
"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as mgs
from DISClib.DataStructures import arraylistiterator as it
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos


def newCatalog(tipo_lista):
    tipo = ""
    if tipo_lista == 1:
        tipo = "ARRAY_LIST"
    elif tipo_lista == 2:
        tipo = "SINGLE_LINKED"
    catalog = {'ListCompleteVidAll': None,
               'categories': None}

    catalog['ListCompleteVidAll'] = lt.newList(tipo)
    catalog['categories'] = lt.newList(tipo)
    
    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, videos):
    lt.addLast(catalog['ListCompleteVidAll'], videos)



def addCat(catalog, cat):
    lt.addLast(catalog["categories"],cat)

def translateCategory(name,catalog):
    categories = newCategory(catalog)
    iterator = it.newIterator(categories)
    
    while it.hasNext(iterator):
        element = it.next(iterator)
        print("element:::::", element)
      #  if element["Categoria"].lower() == name.lower():
       #     return element["Category number"]
        #else:
        #    pass

def req1(catalog,name,country,size):
    videos = newVideo(catalog)
    idd = translateCategory(name,catalog)
    nl = lt.newList(datastructure="ARRAY_LIST")
    iterator = it.newIterator(videos)
    while it.hasNext(iterator):
        element = it.next(iterator)
        if element["country"].lower() == country.lower() and element["category_id"] == idd:
            newdict = {"trending_date": element['trending_date'],
            'title': element['title'],
            "channel_title": element['channel_title'],
            "publish_time": element["publish_time"],
            'views': element['views'],
            "likes": element['likes'], 
            "dislikes": element['dislikes']}
            lt.addLast(nl,newdict)
    return nl

def newVideo(catalog):
    """
    Crea una nueva estructura para modelar los libros de
    un autor y su promedio de ratings
    """
    lvid = lt.newList(datastructure="ARRAY_LIST")
    iterator = it.newIterator(catalog["ListCompleteVidAll"])
    while it.hasNext(iterator):
        vid = it.next(iterator)
        video = {'title': vid['title'], 
        "channel_title": vid['channel_title'], 
        "trending_date": vid['trending_date'], 
        "country": vid['country'], 
        'views': vid['views'], 
        "likes": vid['likes'], 
        "dislikes": vid['dislikes'], 
        "category_id": vid['category_id'], 
        "publish_time": vid["publish_time"], 
        "tags": vid['tags']} 
        lt.addLast(lvid, video)
    return lvid

def newCategory(catalog):
    lc = lt.newList(datastructure="ARRAY_LIST")
    iterator = it.newIterator(catalog["categories"])
    while it.hasNext(iterator):
        numbs = it.next(iterator)
        """isp = lt.isPresent(lc,numbs)
        if isp > 0:
            pass
        else:"""
        cat = {"Category number": numbs["id"], "Categoria" : numbs["name"]}
        lt.addLast(lc,cat)
    return lc


def first(lst):
    element = lt.firstElement(lst)
    return element

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista




def cmpVideosByViews(video1, video2): 
    """ Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2 
    Args: 
        video1: informacion del primer video que incluye su valor 'views' 
        video2: informacion del segundo video que incluye su valor 'views' """
    return (float(video1['views']) < float(video2['views']))

# Funciones de ordenamiento

def sortVideos(catalog,size,orden):
    nueva = lt.subList(catalog["ListCompleteVidAll"],0,size)
    copia_lista = nueva.copy()
    start_time = time.process_time()
    list_orden = orden
    if orden == 1:
        list_orden = sa.sort(copia_lista, cmpVideosByViews)
    elif orden == 2:
        list_orden = ss.sort(copia_lista, cmpVideosByViews)
    elif orden == 3:
        list_orden = ins.sort(copia_lista, cmpVideosByViews)
    elif orden == 4:
        list_orden = qs.sort(copia_lista, cmpVideosByViews)
    elif orden == 5:
        list_orden = mgs.sort(copia_lista, cmpVideosByViews)
    else:
        return "Ha seleccionado una opcion invalida"
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    resul = (elapsed_time_mseg, list_orden)
    return resul


