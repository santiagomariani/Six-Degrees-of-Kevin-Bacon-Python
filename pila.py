class Pila:
    def __init__(self):
        """Crea pila vacia"""
        self.items = []
    def esta_vacia(self):
        """Devuelve True si la lista esta vacia"""
        return len(self.items) == 0
    def apilar(self,x):
        """apila elemento x"""
        self.items.append(x)
    def __str__(self):
        return str(self.items)
    def desapilar(self):
        """Devuelve el elemento tope y lo elimina de la pila. Si la pila esta
vacia levanta una excepcion"""
        if self.esta_vacia():
            raise ValueError("La pila esta vacia")
        return self.items.pop()
    def ver_tope(self):
        if self.esta_vacia():
            raise ValueError("La pila esta vacia")
        return self.items[-1]
