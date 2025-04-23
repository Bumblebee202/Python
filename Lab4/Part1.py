import random
import math

import pygame as pg

# Init pygame
pg.init()

# Setup Surface
SURFACE_RECT = (800, 600)
surface = pg.display.set_mode(SURFACE_RECT)
pg.display.set_caption("Moving Points System (Mouse Controlled - Fixed Speed)")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class MovingPointsSystem:
    def __init__(self, initial_center, num_points=5, min_radius=50, max_radius=100, rotation_speed_per_second=1.0):
        self.center = pg.Vector2(initial_center)
        self.num_points = num_points
        self.points = []
        self.min_radius = min_radius
        self.max_radius = max_radius
        self.rotation_speed_per_second = rotation_speed_per_second  
        self._initialize_points()

    def _initialize_points(self):
        for _ in range(self.num_points):
            radius = random.uniform(self.min_radius, self.max_radius)
            angle = random.uniform(0, 2 * math.pi)
            pos_offset = pg.Vector2(radius * math.cos(angle), radius * math.sin(angle))
            position = self.center + pos_offset
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.points.append({"position": position, "radius": radius, "angle": angle, "color": color})

    def update(self, new_center, delta_time):
        self.center = pg.Vector2(new_center)
        angle_change = self.rotation_speed_per_second * delta_time
        for point_data in self.points:
            point_data["angle"] += angle_change
            pos_offset = pg.Vector2(point_data["radius"] * math.cos(point_data["angle"]), point_data["radius"] * math.sin(point_data["angle"]))
            point_data["position"] = self.center + pos_offset

    def draw(self, surface):
        for point_data in self.points:
            pg.draw.circle(surface, point_data["color"], point_data["position"], 10)
        pg.draw.circle(surface, RED, self.center, 15)


# Event-Render loop
run_loop = True
points_system = MovingPointsSystem(initial_center=(SURFACE_RECT[0] // 2, SURFACE_RECT[1] // 2), num_points=10, rotation_speed_per_second=5.0)
clock = pg.time.Clock()
FPS = 60  

while run_loop:
    delta_time = clock.tick(FPS) / 1000.0  

    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run_loop = False
            continue

    mouse_pos = pg.mouse.get_pos()

    # Update
    points_system.update(mouse_pos, delta_time)

    # Draw
    surface.fill(WHITE)
    points_system.draw(surface)

    # Update display
    pg.display.flip()

pg.quit()