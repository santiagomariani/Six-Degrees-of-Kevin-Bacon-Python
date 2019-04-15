class _Nodo:
    def __init__(self,dato=None,prox=None):
        self.dato = dato
        self.prox = prox
        
    def __str__(self):
        return str(self.dato)
    
class Cola():
    def __init__(self):
        self.prim = None
        self.ult = None

    def encolar(self,x):
        nodo = _Nodo(x)
        if self.prim is not None:
            self.ult.prox = nodo
        else:
            self.prim = nodo

        self.ult = nodo

    def esta_vacia(self):
        return self.prim is None
    
    def __str__(self):
        
        l = []
        nodo = self.prim
        while nodo is not None:
            l.append(str(nodo))
            nodo =  nodo.prox
        return str(l)

    def ver_primero(self):
        if self.prim is not None:
            return self.prim.dato
        raise ValueError("La cola esta vacia")

    def desencolar(self):
        if self.esta_vacia():
            raise ValueError("La cola esta vacia")
        
        valor = self.prim.dato
        self.prim = self.prim.prox
        return valor




