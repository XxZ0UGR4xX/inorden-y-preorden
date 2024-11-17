class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def agregar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(self.raiz, valor)

    def _agregar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._agregar_recursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._agregar_recursivo(nodo.derecho, valor)

    def recorrido_inorden(self, nodo):
        if nodo:
            self.recorrido_inorden(nodo.izquierdo)
            print(nodo.valor, end=' ')
            self.recorrido_inorden(nodo.derecho)

    def recorrido_postorden(self, nodo):
        if nodo:
            self.recorrido_postorden(nodo.izquierdo)
            self.recorrido_postorden(nodo.derecho)
            print(nodo.valor, end=' ')

# Ejemplo de uso
if __name__ == "__main__":
    arbol = ArbolBinario()
    arbol.agregar(10)
    arbol.agregar(5)
    arbol.agregar(15)
    arbol.agregar(3)
    arbol.agregar(7)
    arbol.agregar(12)
    arbol.agregar(18)

    print("Recorrido InOrden:")
    arbol.recorrido_inorden(arbol.raiz)
    print("\nRecorrido PostOrden:")
    arbol.recorrido_postorden(arbol.raiz)