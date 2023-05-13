class QuadtreeNode:
    def __init__(self, x, y, width, height):
        self.x = x # coordenada x del nodo
        self.y = y # coordenada y del nodo
        self.width = width # ancho del nodo
        self.height = height # altura del nodo
        self.points = [] # lista de puntos dentro del nodo
        self.children = [None, None, None, None] # hijos del nodo

    def insert(self, point):
        # Si el punto está dentro del nodo, lo agregamos a la lista de puntos
        if self.x <= point[0] < self.x + self.width and self.y <= point[1] < self.y + self.height:
            self.points.append(point)
        else:
            # Si no está dentro del nodo, lo agregamos al hijo correspondiente
            x = self.x + self.width/2
            y = self.y + self.height/2
            if point[0] < x:
                if point[1] < y:
                    if not self.children[0]:
                        self.children[0] = QuadtreeNode(self.x, self.y, self.width/2, self.height/2)
                    self.children[0].insert(point)
                else:
                    if not self.children[1]:
                        self.children[1] = QuadtreeNode(self.x, y, self.width/2, self.height/2)
                    self.children[1].insert(point)
            else:
                if point[1] < y:
                    if not self.children[2]:
                        self.children[2] = QuadtreeNode(x, self.y, self.width/2, self.height/2)
                    self.children[2].insert(point)
                else:
                    if not self.children[3]:
                        self.children[3] = QuadtreeNode(x, y, self.width/2, self.height/2)
                    self.children[3].insert(point)

    def query(self, x, y, width, height):
        # Retorna todos los puntos que se encuentren dentro del area especificada
        result = []
        for point in self.points:
            if x <= point[0] < x + width and y <= point[1] < y + height:
                result.append(point)
        if self.children[0]:
            result += self.children[0].query(x, y, width, height)
        if self.children[1]:
            result += self.children[1].query(x, y + self.height/2, width, height)
        if self.children[2]:
            result += self.children[2].query(x + self.width/2, y, width, height)
        if self.children[3]:
            result += self.children[3].query(x + self.width/2, y + self.height/2, width, height)
        return result
    

# Ejemplo de uso
root = QuadtreeNode(0, 0, 100, 100)
points = [(10, 10), (30, 40), (53, 50), (70, 30), (80, 80), (13, 19), (35, 36), (55, 52), (70, 39), (98, 85), (7, 14), (28, 33), (59, 45), (40, 15), (87, 96)]
for point in points:
    root.insert(point)
result = root.query(0, 0, 50, 50)
print(result)