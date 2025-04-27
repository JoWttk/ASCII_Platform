import pygame

def create_platforms():
    platforms = [
        pygame.Rect(0, 550, 800, 50),
        pygame.Rect(200, 400, 200, 20),
        pygame.Rect(500, 300, 200, 20),
        pygame.Rect(1000, 200, 200, 20),
    ]
    return platforms

def create_map():
    map_width = 2000
    map_height = 2000
    return map_width, map_height
