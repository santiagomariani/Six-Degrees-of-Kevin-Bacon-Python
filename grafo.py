class Grafo:

    def __init__(self):
        self.aristas_conexiones = {}
        self.vertice_conexiones = {}

    def agregar_vertice(self,vertice,arista):

        self.aristas_conexiones[arista][vertice] = None

        if(not vertice in self.vertice_conexiones): 
            self.vertice_conexiones[vertice] = {}
        self.vertice_conexiones[vertice][arista] = None
        
    def agregar_arista(self,arista):

        self.aristas_conexiones[arista] = {}

    def adyacentes(self,vertice):

        adyacentes = []
        procesados = {}
        procesados[vertice] = None

        for arista in self.vertice_conexiones[vertice].keys():
            for vertice in self.aristas_conexiones[arista].keys():
                if(not vertice in procesados):
                    procesados[vertice] = None
                    adyacentes.append((vertice,arista))
        return adyacentes

    def aristas(self):
        
        aristas = []

        for arista in self.aristas_conexiones.keys():
            aristas.append(arista)

        return aristas

    def esta_arista(self,arista):
        return arista in self.aristas_conexiones

    def esta_vertice(self,vertice):
        return vertice in self.vertice_conexiones

    def vertices(self):

        vertices = []

        for vertice in self.vertice_conexiones.keys():
            vertices.append(vertice)

        return vertices

    def es_adyacente(self,vertice1,vertice2):

        for arista in self.vertice_conexiones[vertice1].keys():
            if arista in self.vertice_conexiones[vertice2]:
                return True
        return False

    def obtener_vertice_conexiones(self,vertice):

        resul = []

        for arista in self.vertice_conexiones[vertice].keys():
            resul.append(arista)

        return resul
