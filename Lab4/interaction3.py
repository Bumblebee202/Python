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

# Define fonts
font = pg.font.SysFont(None, 48)

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Draw static text
text_surf = font.render("Hello Surface!", True, BLACK)


class Dot:

    def __init__(self):
        x = random.uniform(0, SURFACE_RECT[0])
        y = random.uniform(0, SURFACE_RECT[1])
        self.pos = vec2(x, y)
        self.size = 10
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


dots = [Dot() for _ in range(10)]

display_menu = False

# Event-Render loop
run_loop = True
while run_loop:
    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_loop = False
            continue
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                dots.append(Dot())
            if event.key == pg.K_r:
                if dots:
                    dots.pop()
            if event.key == pg.K_h:
                display_menu = not display_menu

    mouse_pos = vec2(pg.mouse.get_pos())

    # Draw
    surface.fill(WHITE)

    target_pos = mouse_pos
    for dot in dots:
        diff = (target_pos - dot.pos)
        dist = math.dist(dot.pos, target_pos)
        dot.pos += diff * 0.001
        target_pos = dot.pos
        pg.draw.circle(surface, dot.color, dot.pos, dot.size)

    if display_menu:
        surface.blit(text_surf, (0, 0))

    # Update display
    pg.display.flip()

pg.quit()
