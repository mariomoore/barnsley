import pygame
import random

WIDTH = 600
HEIGHT = 600
COLOR = (0, 0, 0)

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

for s in [1000, 10000, 50000, 100000, 500000]:
    x = 0.0
    y = 0.0
    screen.fill((255, 255, 255))
    for _ in range(s):
        r = random.random()
        if r <= 0.01:
            x_new = 0
            y_new = 0.16*y
        elif r <= 0.08:
            x_new = 0.2*x - 0.26*y
            y_new = 0.23*x + 0.22*y + 1.6
        elif r <= 0.15:
            x_new = -0.15*x + 0.28*y
            y_new = 0.26*x + 0.24*y + 0.44
        else:
            x_new = 0.85*x + 0.04*y
            y_new = -0.04*x + 0.85*y + 1.6
        x = x_new
        y = y_new
        screen.set_at((int(WIDTH/6*x + WIDTH/2),
                        HEIGHT - int(HEIGHT/10*y)),
                        COLOR)
        pygame.display.flip()
    pygame.image.save(screen, str(s)+'.'+'png')