from grafo import Grafo
import time
from cola import *
from pila import *
from random import randint
from heapq import *
import csv

NOMBRE_ACTOR = 0
N_PASOS = 15
N_RECORRIDOS = 20


def grafo_crear(nombre_archivo):
    """
    Crea un grafo de conexiones de actores a partir de un archivo de datos.

    PRE: Recibe el nombre de un archivo separado por comas que contenga de lineas:
        actor,pelicula,pelicula,pelicula
        que equivalen a: vertice,arista,arista,arista
    POST: Devuelve un grafo creado a partir de estos datos.
    """

    grafo_peliculas = Grafo()

    with open(nombre_archivo) as archivo:

        archivo_reader = csv.reader(archivo, delimiter = ",")

        for linea in archivo_reader:

            nombre_actor = linea[NOMBRE_ACTOR]

            for i in range(1,len(linea)):
                if not grafo_peliculas.esta_arista(linea[i]):
                    grafo_peliculas.agregar_arista(linea[i])
                grafo_peliculas.agregar_vertice(nombre_actor,linea[i])

    return grafo_peliculas 

def actores_a_distancia(grafo, origen, n):
    """
    Devuelve los actores a distancia n del recibido.

    PRE: Recibe el grafo, el actor de origen y el número deseado.
    POST: Devuelve la lista de cadenas (actores) a n pasos del recibido.
    """

    if(not grafo.esta_vertice(origen)):
        return False
        
    resul = []
        
    if(n == 0):
        resul.append(origen)
        return resul

    visitados = {}
    orden = {}

    q = Cola()
    q.encolar(origen)

    visitados[origen] = True
    orden[origen] = 0

    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            w = w[0]
            if w not in visitados:
                visitados[w] = True
                orden[w] = orden[v] + 1
                if(orden[w] == n):
                    resul.append(w)
                    continue
                q.encolar(w)
    return resul

def popularidad(grafo, actor):
        """
        Calcula la popularidad del actor recibido.

        PRE: Recibe el grafo y un actor de origen
        POST: Devuelve un entero que simboliza la popularidad: todos los adyacentes
                de los adyacentes del actor, multiplicado por su cantidad de peliculas
        """

        if(not grafo.esta_vertice(actor)):
            return False
        actores_dist2 = actores_a_distancia(grafo,actor,2)
        cant_actores_dist2 = len(actores_dist2)
        
        peliculas_actor = grafo.obtener_vertice_conexiones(actor)
        cant_peliculas_actor = len(peliculas_actor)

        return cant_actores_dist2 * cant_peliculas_actor

def distancia_a_actor(grafo,origen):
    """
    Devuelve la distancia de todos los actores al origen.

    PRE: Recibe el grafo y un actor de origen.
    POST: Devuelve un diccionario con los actores (clave) y las distancias al origen (valor).
    """

    visitados = {}
    orden = {}

    q = Cola()
    q.encolar(origen)

    visitados[origen] = True
    orden[origen] = 0

    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            actor = w[0]
            if not(actor in visitados):
                visitados[actor] = True
                orden[actor] = orden[v] + 1;
                q.encolar(actor)
    return orden;

def camino(grafo, origen, llegada):
    """
    Devuelve el camino entre un actor de origen y uno de llegada.

    PRE: Recibe el grafo, un actor de origen y un actor de llegada.
    POST: Devuelve una lista ordenada de cadenas (películas) para llegar desde
        el origen hasta el final.
    """
    resul = []

    if(origen == llegada):
        return resul
        
    if(not grafo.esta_vertice(origen) or not grafo.esta_vertice(llegada)):
        return False

    visitados = {}
    padres = {}

    q = Cola()
    q.encolar(origen)

    visitados[origen] = True
    padres[origen] = None

    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            actor = w[0]
            arista = w[1]
            if not(actor in visitados):
                visitados[actor] = True
                padres[actor] = (v,arista)
                if(actor == llegada):
                    break
                q.encolar(actor)

    if(llegada not in visitados):
        return resul

    actor = llegada
    while(True):
        
        padre_actor = padres[actor]
        resul.append((padre_actor[0],actor,padre_actor[1]))
        actor = padre_actor[0]
        if(actor == origen): break      

    pila_aux = Pila()

    for elem in resul:
        pila_aux.apilar(elem)

    for i in range(len(resul)):
        resul[i] = pila_aux.desapilar()

    return resul

def cantidad_peliculas(grafo):
    return len(grafo.aristas())

def cantidad_actores(grafo):
    return len(grafo.vertices())

def adyacente_aleatorio(grafo, vertice):
    adyacentes = grafo.adyacentes(vertice)
    n_random = randint(0, len(adyacentes) - 1)

    return adyacentes[n_random][0]

def recorrer_grafo_aleatoriamente(grafo, origen, contador_visitados):
    """
    Recorre el grafo aleatoriamente una cantidad N_PASOS. Devuelve el diccionario contador_visitados
    modificado, se aumenta el contador de aquellos vertices visitados.
    PRE: Recibe el grafo, el origen y un diccionario contador_visitados.
    POST: Devuelve el diccionario contador_visitados modificado.
    """

    actor_actual = adyacente_aleatorio(grafo, origen)

    for i in range(0, N_PASOS):

        actor_actual = adyacente_aleatorio(grafo, actor_actual)

        if origen == actor_actual or grafo.es_adyacente(origen, actor_actual) == True:
            i = i-1
            continue
        if actor_actual not in contador_visitados:
            aux = 1
        else:
            aux = contador_visitados[actor_actual]
            aux = aux + 1

        contador_visitados[actor_actual] = aux

    return contador_visitados


# Siendo Origen el actor que se buscan los similares y n la cantidad de similares
def similares(grafo, origen, n):
    """
    Calcula los n actores más similares al actor de origen y los devuelve en una
    lista ordenada de mayor similitud a menor.

    PRE: Recibe el grafo, el actor de origen, y el n deseado
    POST: Devuelve una lista de los n actores no adyacentes más similares al
        pedido. La lista no debe contener al actor de origen.
    """
    if(not grafo.esta_vertice(origen)):
            return False

    contador_visitados = {}
    actores_mas_visitados = []

    if(n == 0):
        return actores_mas_visitados

    for i in range(0, N_RECORRIDOS):
        contador_visitados = recorrer_grafo_aleatoriamente(grafo, origen, contador_visitados)

    veces = 0
    heap_actores_mas_visitados = []

    for actor in contador_visitados:
        if veces < n:
            heappush(heap_actores_mas_visitados,(contador_visitados[actor],actor))
            veces += 1

        else:    
            if(contador_visitados[actor] > heap_actores_mas_visitados[0][0]):
                heappop(heap_actores_mas_visitados)
                heappush(heap_actores_mas_visitados,(contador_visitados[actor],actor))

    for elem in heap_actores_mas_visitados:
        actores_mas_visitados.append(elem[1]) 

    return actores_mas_visitados
