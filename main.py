import pygame
import sys
from assets.player import Player
from assets.gamemap import create_platforms, create_map

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ascii")

camera_x, camera_y = 0, 0

platforms = create_platforms()
map_width, map_height = create_map()

player = Player()

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player.update(keys, platforms)

    camera_x = player.rect.x - width // 2
    camera_y = player.rect.y - height // 2

    camera_x = max(0, min(camera_x, map_width - width))
    camera_y = max(0, min(camera_y, map_height - height))

    for platform in platforms:
        pygame.draw.rect(screen, (255, 255, 0), (platform.x - camera_x, platform.y - camera_y, platform.width, platform.height))

    player.draw(screen, camera_x, camera_y)

    pygame.display.flip()
    clock.tick(60)
