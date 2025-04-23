import random

import pygame as pg

# Init pygame
pg.init()

# Setup Surface
SURFACE_RECT = (800, 600)
surface = pg.display.set_mode(SURFACE_RECT)
pg.display.set_caption("Pygame Animation")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pos = (SURFACE_RECT[0]/2, SURFACE_RECT[1]/2)

# Event-Render loop
run_loop = True
while run_loop:
    # 1. Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_loop = False
            continue

    # 2. Draw
    surface.fill(WHITE)
    pos = (pos[0] + random.uniform(-1.0, 1.0), pos[1] + random.uniform(-1.0, 1.0))
    size = 20
    pg.draw.circle(surface, RED, pos, size)

    # Update display
    pg.display.flip()

pg.quit()
