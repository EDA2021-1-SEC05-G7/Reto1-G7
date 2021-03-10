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

def req1(catalog,name,country,size):
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




def first(lst):
    element = lt.firstElement(lst)
    return element


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


def req2(catalog,country):
    videos = catalog["ListCompleteVidAll"]
    dictitles = {}
    dicsave = {}
    iterator = it.newIterator(videos)
    mayor = 0
    nomayor = 0
    while it.hasNext(iterator):
        element = it.next(iterator)
        if element["country"].lower() == country.lower():
            if element['title'] in dictitles:
                dictitles[element["title"]] += 1
            else:
                dictitles[element["title"]] = 1
                dicsave[element["title"]] = element

    (a, b) = max((dictitles[key], key) for key in dictitles)
    
    return {'title': b, 'channel_title': dicsave[b]['channel_title'], 'country': country, 'número de días': a}

def req3(catalog, category):
    idd = translateCategory(category,catalog)
    titles = catalog["ListCompleteVidAll"]
    cats = {}
    dick = {}
    iterator = it.newIterator(titles)
    while it.hasNext(iterator):
        element = it.next(iterator)
        if element["category_id"] == idd:
            if element['title'] in cats:
                cats[element["title"]] += 1
            else:
                cats[element["title"]] = 1
                dick[element["title"]] = element

    (a, b) = max((cats[key], key) for key in cats)
    
    return {'title': b, 'channel_title': dick[b]['channel_title'], 'category_id': dick[b]["category_id"], 'número de días': a}
 
def req4(catalog, tag, pais):
    iterator = it.newIterator(catalog["ListCompleteVidAll"])
    listags = lt.newList(datastructure="ARRAY_LIST") 
    while it.hasNext(iterator):
        element = it.next(iterator) 
        tags = element["tags"].split("|")
        rator = it.newIterator(tags)
        while it.hasNext(terator):
            mento = it.next(rator)
            if element["country"].lower() == pais.lower() and tag.lower() in mento.lower():
                dictags = {'title': element['title'],
                "channel_title": element['channel_title'],
                "publish_time": element["publish_time"],
                'views': element['views'],
                "likes": element['likes'], 
                "dislikes": element['dislikes'],
                "tags": element['tags']}
                lt.addLast(listags,dictags)
    return listags
