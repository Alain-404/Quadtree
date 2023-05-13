"""QUADTREE"""

import pygame
import quadtree

# Inicializamos la libreria pygame
pygame.init()

# Definimos un ancho y alto de la pantalla de la ventana principal
width, height = 1200, 600

# Creamos el espacio (ventana)
ventana = pygame.display.set_mode((width, height))
fuente = pygame.font.Font(None, 25)
superficie_texto = fuente.render('Coordenadas: (0, 0)', True, (255, 255, 255))


# Title of the window:
pygame.display.set_caption('Ejemplo de codificacion de un Quadtree')

# creamos el quadtree
arbol = quadtree.Rectangulo(0, 0, width, height)
qt = quadtree.Quadtree(arbol, 4)
points = []  # lista para los puntos

color = (77, 0, 0)  # color de ventana
color_rect = (51, 255, 51)  # color de lineas
color_point = (255, 255, 255)  # color de los puntos

ventana.fill(color)  # asignando color a la ventana

running = True
while running:
    # Se dibuja un rectangulo inicial
    pygame.draw.rect(ventana, color_rect, pygame.Rect(0, 0, width, height), 1)

    pos = pygame.mouse.get_pos()
    coord_text = f'Coordenadas: {pos}'
    superficie_texto = fuente.render(coord_text, True, (255, 255, 255))
    ventana.blit(superficie_texto, (10, 10))

    eventos = pygame.event.get()  # Se registra los eventos

    for event in eventos:
        # Sala del bucle si se salio de la ventana
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # se obtiene las cordenadas del click
            if pos not in points:
                points.append(pos)
                pygame.draw.circle(ventana, color_point, pos, 4)
                qt.insert(quadtree.Point(*pos))
                qt.printsub()

            # Se grafican los nuevos rectangulos
            for r in quadtree.RECTANGLES:
                pygame.draw.rect(ventana, color_rect, pygame.Rect(*eval(str(r))), 1)

    # se continua actualizando el espacio
    pygame.display.flip()

# cierra pygame
pygame.quit()
