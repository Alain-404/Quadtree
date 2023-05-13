import random
import time

RECTANGLES = []
POINTS = []


class Point:
    """INICIALIZAMOS EL ESTADO DEL OBJETO"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # DEFINIMOS LA ESTRUCTURA DE REPRESENTACION DE NUESTRO OBJETO PARA LA FUNCION PRINT
    def __repr__(self):
        return f'{{"x": {self.x}, "y": {self.y}}}'


class Rectangulo:
    """INICIALIZAMOS EL ESTADO DEL OBJETO"""
    def __init__(self, x, y, w, h):
        """Propiedades de nuestro cuadrante"""
        self.x = x  # cordenada X de la esquina
        self.y = y  # cordenada Y de la esquina
        self.w = w  # ancho
        self.h = h  # alto
        self.puntos = []  # Lista para almacenar los puntos dentro del area

    # DEFINIMOS LA ESTRUCTURA DE REPRESENTACION DE NUESTRO OBJETO PARA LA FUNCION PRINT (area)
    def __repr__(self):
        return f'({self.x}, {self.y}, {self.w}, {self.h})'

    def contains(self, point): # Evaluamos su un punto esta entre los limites de espacio X y Y
        check_x = self.x < point.x <= self.x + self.w
        check_y = self.y < point.y <= self.y + self.h
        return check_x and check_y

    def insert(self, point):
        if not self.contains(point):
            return False

        self.puntos.append(point) # si esta contenido se agrega a la lista de puntos
        return True


class Quadtree:
    """CLASE QUADTREE"""

    def __init__(self, limite, capacidad):
        """CONSTRUCTOR PARA EL OBJETO QUADTREE"""
        self.limite = limite  # limite del Rectangulo
        self.capacidad = capacidad  # 4 por defecto en el espacio o subespacio
        self.dividido = False  # Para revisar si se ha dividido
        """Cuadrantes"""
        self.norte_este = None
        self.sur_este = None
        self.norte_oeste = None
        self.sur_oeste = None

    def subdivide(self):
        """DIVISION DEL ESPACIO"""
        x, y, w, h = self.limite.x, self.limite.y, self.limite.w, self.limite.h

        north_east = Rectangulo(x + w / 2, y, w / 2, h / 2)
        self.norte_este = Quadtree(north_east, self.capacidad)

        south_east = Rectangulo(x + w / 2, y + h / 2, w / 2, h / 2)
        self.sur_este = Quadtree(south_east, self.capacidad)

        south_west = Rectangulo(x, y + h / 2, w / 2, h / 2)
        self.sur_oeste = Quadtree(south_west, self.capacidad)

        north_west = Rectangulo(x, y, w / 2, h / 2)
        self.norte_oeste = Quadtree(north_west, self.capacidad)

        self.dividido = True

        for i in self.limite.puntos:
            self.norte_este.insert(i)
            self.sur_este.insert(i)
            self.norte_oeste.insert(i)
            self.sur_oeste.insert(i)

    def insert(self, point):
        """FUNCION DE INSERSION"""
        # Si este rectángulo principal no contiene el punto, no es necesario verificar el rectángulo subdividido
        if not self.limite.contains(point):
            return

        if len(self.limite.puntos) < self.capacidad:
            self.limite.insert(point)  # Siempre que no exeda su limite se agrega el punto, sino se subdivide
        else:
            if not self.dividido:
                self.subdivide()

            self.norte_este.insert(point)
            self.sur_este.insert(point)
            self.sur_oeste.insert(point)
            self.norte_oeste.insert(point)

    def printsub(self):
        global RECTANGLES, POINTS
        if self.dividido is False and len(self.limite.puntos):
            print(self.limite)
            print(self.limite.puntos)
            RECTANGLES.append(self.limite)
            POINTS.append(self.limite.puntos)
        else:
            if self.norte_este is not None:
                self.norte_este.printsub()
            if self.sur_este is not None:
                self.sur_este.printsub()
            if self.norte_oeste is not None:
                self.norte_oeste.printsub()
            if self.sur_oeste is not None:
                self.sur_oeste.printsub()


if __name__ == '__main__':
    root = Rectangulo(0, 0, 200, 200)
    qt = Quadtree(root, 4)
    random.seed(time.time())
    for i in range(10):
        p = Point(random.randint(0, 200), random.randint(0, 200))
        qt.insert(p)

    qt.printsub()