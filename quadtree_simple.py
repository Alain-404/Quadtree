class QuadtreeNode:
    #CONSTRUCTOR
    def __init__(self, x, y, ancho, alto):
        self.x = x # coordenada x del nodo
        self.y = y # coordenada y del nodo
        self.ancho = ancho # ancho del nodo
        self.alto = alto # altura del nodo
        self.puntos = [] # lista de puntos dentro del nodo
        self.hijos = [None, None, None, None] # hijos del nodo

    def insert(self, punto):
        # Si el punto está dentro del nodo, lo agregamos a la lista de puntos
        if self.x <= punto[0] < self.x + self.ancho and self.y <= punto[1] < self.y + self.alto:
            self.puntos.append(punto)
        else:
            # Si no está dentro del nodo, lo agregamos al hijo correspondiente
            x = self.x + self.ancho/2
            y = self.y + self.alto/2
            if punto[0] < x:
                if punto[1] < y:
                    if not self.hijos[0]:
                        self.hijos[0] = QuadtreeNode(self.x, self.y, self.ancho/2, self.alto/2)
                    self.hijos[0].insert(punto)
                else:
                    if not self.hijos[1]:
                        self.hijos[1] = QuadtreeNode(self.x, y, self.ancho/2, self.alto/2)
                    self.hijos[1].insert(punto)
            else:
                if punto[1] < y:
                    if not self.hijos[2]:
                        self.hijos[2] = QuadtreeNode(x, self.y, self.ancho/2, self.alto/2)
                    self.hijos[2].insert(punto)
                else:
                    if not self.hijos[3]:
                        self.hijos[3] = QuadtreeNode(x, y, self.ancho/2, self.alto/2)
                    self.hijos[3].insert(punto)

    def query(self, x, y, ancho, alto):
        # Retorna todos los puntos que se encuentren dentro del area especificada
        result = []
        for punto in self.puntos:
            if x <= punto[0] < x + ancho and y <= punto[1] < y + alto:
                result.append(punto)
        if self.hijos[0]:
            result += self.hijos[0].query(x, y, ancho, alto)
        if self.hijos[1]:
            result += self.hijos[1].query(x, y + self.alto/2, ancho, alto)
        if self.hijos[2]:
            result += self.hijos[2].query(x + self.ancho/2, y, ancho, alto)
        if self.hijos[3]:
            result += self.hijos[3].query(x + self.ancho/2, y + self.alto/2, ancho, alto)
        return result

# Ejemplo de uso
arbol = QuadtreeNode(0, 0, 100, 100)
puntos = [(10, 10), (30, 40), (53, 50), (70, 30), (80, 80), (13, 19), (35, 36), (55, 52), (70, 39), (98, 85), (7, 14), (28, 33), (59, 45), (40, 15), (87, 96)]
for punto in puntos:
    arbol.insert(punto)
result = arbol.query(0, 0, 50, 50)
print("\n Los puntos en el espacio especificdo son: ", result)