#channel_title = information_videos
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


def newCatalog():
    catalog = {'ListCompleteVidAll': None,
               'categories': None}

    catalog['ListCompleteVidAll'] = lt.newList("ARRAY_LIST")
    catalog['categories'] = lt.newList("ARRAY_LIST")
    
    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, videos):
    lt.addLast(catalog['ListCompleteVidAll'], videos)



def addCat(catalog, cat):
    lt.addLast(catalog["categories"],cat)


# Funciones Req1    

def translateCategory(name,catalog):
    categories = catalog["categories"]
    iterator = it.newIterator(categories)
    while it.hasNext(iterator):
        element = it.next(iterator)
        if name.lower() in element["name"].lower() :
            return element["id"]
        else:
            pass

def req1(catalog,name,country):
    videos = catalog["ListCompleteVidAll"]
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

    """def newVideo(catalog):
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
        isp = lt.isPresent(lc,numbs)
        if isp > 0:
            pass
        else:
        cat = {"Category number": numbs["id"], "Categoria" : numbs["name"]}
        lt.addLast(lc,cat)
        ""
    return lc"""


def first(lst):
    element = lt.firstElement(lst)
    return element


# Funciones utilizadas para comparar elementos dentro de una lista




def cmpVideosByViews(video1, video2): 
    """ Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2 
    Args: 
        video1: informacion del primer video que incluye su valor 'views' 
        video2: informacion del segundo video que incluye su valor 'views' """
    return (float(video1['views']) > float(video2['views']))



# Funciones de ordenamiento

def sortVideos(catalog,size,name,country):
    nueva = req1(catalog,name,country)
    copia_lista = nueva.copy()
    list_orden = mgs.sort(copia_lista, cmpVideosByViews)
    resul = lt.subList(list_orden, 0, size)
    return resul


