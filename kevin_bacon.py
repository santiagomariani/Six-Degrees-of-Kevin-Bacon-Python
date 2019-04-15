
from seis_grados import *
import cmd
import sys

distancia = 1

nombre_dataset = sys.argv[1]
grafo_peliculas = grafo_crear(nombre_dataset)

class Shell(cmd.Cmd):
   
    intro = """
            BIENVENIDO..  
    """
    prompt = "*>> "

    def do_camino_hasta_KB(self,parametros):
        actor = parametros
        lista_camino = camino(grafo_peliculas,actor,"Bacon Kevin")
        if(lista_camino == False):
            print("El actor '{}' no se encuentra en el dataset".format(actor))
            return
        elif(len(lista_camino) == 0):
            print("No hay conexion entre KB y '{}'".format(actor))
            return
        for elem in lista_camino:
            print("'{}' actuó con '{}' en '{}'".format(elem[0],elem[1],elem[2]))

    def do_popularidad_contra_KB(self,parametros):
        actor = parametros
        popularidad_actor = popularidad(grafo_peliculas,actor)
        popularidad_KB = popularidad(grafo_peliculas,"Bacon Kevin")
        popularidad_actor_contra_KB = (popularidad_actor * 100) / popularidad_KB
        percent = "%"

        print("'{}' es un {:.2f}{} de lo popular que es Kevin Bacon".format(actor,popularidad_actor_contra_KB,percent))

    def do_cantidad_peliculas(self,parametros):
        print("El dataset contiene {}".format(cantidad_peliculas(grafo_peliculas)))

    def do_cantidad_actores(self,parametros):
        print("El dataset contiene {}".format(cantidad_actores(grafo_peliculas)))

    def do_bacon_number(self,parametros):
        actor = parametros
        camino_kbn_actor = camino(grafo_peliculas,actor,"Bacon Kevin")
        if(camino_kbn_actor == False):
            print("El actor '{}' no se encuentra en el dataset".format(actor))
            return

        kbn_actor = len(camino_kbn_actor)
        
        if(kbn_actor == 0 and actor != "Bacon Kevin"):
            kbn_actor = -1 
        print("'{}' tiene un Kevin Bacon Number igual a {}".format(actor,kbn_actor))

    def do_bacon_number_infinito(self,parametros):
        dist_a_kbn = distancia_a_actor(grafo_peliculas,"Bacon Kevin")
        cant_actores_alcanzables_por_kbn = len(dist_a_kbn)
        cant_actores_inalcanzables_por_kbn = cantidad_actores(grafo_peliculas) - cant_actores_alcanzables_por_kbn
        print("Los actores con un Bacon Number infinito son {}".format(cant_actores_inalcanzables_por_kbn))
    
    def do_bacon_number_mayor_a_6(self,parametros):
        dist_a_kbn = distancia_a_actor(grafo_peliculas,"Bacon Kevin")
        dist_mayor_a_6 = {}

        for dist in dist_a_kbn.values():
            if(dist >= 6):
                if(not dist in dist_mayor_a_6):
                    dist_mayor_a_6[dist] = 1
                    continue
                dist_mayor_a_6[dist] += 1

        for dist in sorted(dist_mayor_a_6):
            print("Con KBN igual a {}: {} actores".format(dist,dist_mayor_a_6[dist]))

    def do_KBN_promedio(self,parametros):
        dist_a_kbn = distancia_a_actor(grafo_peliculas,"Bacon Kevin")
        cant_actores_alcanzables_por_kbn = len(dist_a_kbn)
        dist_total = 0
        for dist in dist_a_kbn.values():
            dist_total += dist

        print("El Kevin Bacon Number promedio es {:2f}".format(dist_total / cant_actores_alcanzables_por_kbn))

    def do_similares_a_KB(self,parametros):
        n = int(parametros)
        print("Los {} actores más similares KB son {}".format(n,similares(grafo_peliculas,"Bacon Kevin",n)))
    
    def do_exit(self,parametros):
        exit()
        
Shell().cmdloop()        
    
        
