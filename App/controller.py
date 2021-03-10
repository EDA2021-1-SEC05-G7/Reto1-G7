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
 """

import config as cf
import model
import csv
 

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de videos

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()

    return catalog

    

def loadData(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)
    catfile = cf.data_dir + 'category-id.csv'
    input_cat_file = csv.DictReader(open(catfile, encoding="utf-8"),  delimiter='\t')
    for cat in input_cat_file:
        model.addCat(catalog, cat)



#catalog = initCatalog()
#loadData(catalog)
#print(newCategory(catalog))
#print(model.translateCategory("music",catalog))
#print(model.req1(catalog,"Music","canada",0))
#print(req3(catalog,"music"))
#print(firstVideo(catalog))





def firstVideo(catalog):
    Pvideo = model.first(catalog['ListCompleteVidAll'])
    return Pvideo


# Funciones de ordenamiento

def sortVideos(catalog,size,name,country):
    """
    Ordena los libros por average_rating
    """
    return model.sortVideos(catalog,size,name,country)
    


def req2(catalog, country):
    return model.req2(catalog, country)

def req3(catalog,category):
    result = model.req3(catalog,category)
    return result

