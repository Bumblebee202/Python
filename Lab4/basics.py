import pygame as pg

# Init pygame
pg.init()

# Setup Surface
WIDTH, HEIGHT = 800, 600
surface = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pygame Static")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Draw
surface.fill(WHITE)

pos = (WIDTH/2, HEIGHT/2)
size = 20
pg.draw.circle(surface, RED, pos, size)

# Update display
pg.display.flip()

# pygame loop
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
