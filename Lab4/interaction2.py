import random

import pygame as pg
from pygame.math import Vector2 as vec2
import math

# Init pygame
pg.init()

# Setup Surface
SURFACE_RECT = (800, 600)
surface = pg.display.set_mode(SURFACE_RECT)
pg.display.set_caption("Pygame Interaction")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pos = vec2(SURFACE_RECT[0]/2, SURFACE_RECT[1]/2)

# Event-Render loop
run_loop = True
while run_loop:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_loop = False
            continue

    mouse_pos = vec2(pg.mouse.get_pos())

    # Draw
    surface.fill(WHITE)

    diff = (mouse_pos - pos)
    pos += diff * 0.001

    # dist = math.dist(pos, mouse_pos)
    size = 20 #5 + dist * 0.1
    pg.draw.circle(surface, RED, pos, size)

    # Update display
    pg.display.flip()

pg.quit()
