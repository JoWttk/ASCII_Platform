import pygame

def player_idle():
    return [
        " O ",
        "/|\\",
        "/ \\"
    ]

def player_walk1():
    return [
        " O ",
        "/|>",
        "/ >"
    ]

def player_walk2():
    return [
        " O ",
        "<|\\",
        "< \\"
    ]

def player_walk_frames():
    return [player_walk1(), player_walk2()]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((30, 54))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 300
        self.velocity_x = 0
        self.velocity_y = 0
        self.speed = 5
        self.jump_force = -12
        self.gravity = 0.6
        self.on_ground = False
        self.walk_frames = player_walk_frames()
        self.idle_frames = player_idle()
        self.frame_index = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_cooldown = 200
        self.is_walking = False

    def update(self, keys, platforms):
        self.handle_movement(keys)
        self.apply_gravity()
        self.check_collisions(platforms)
        self.update_animation()

    def handle_movement(self, keys):
        self.velocity_x = 0
        walking = False
        if keys[pygame.K_a]:
            self.velocity_x = -self.speed
            walking = True
        if keys[pygame.K_d]:
            self.velocity_x = self.speed
            walking = True
        if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and self.on_ground:
            self.velocity_y = self.jump_force
        
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        
        self.is_walking = walking

    def apply_gravity(self):
        self.velocity_y += self.gravity

    def check_collisions(self, platforms):
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.velocity_y > 0:
                    self.rect.bottom = platform.top
                    self.velocity_y = 0
                    self.on_ground = True

    def update_animation(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_cooldown:
            self.last_update = now
            if self.is_walking:
                self.frame_index = (self.frame_index + 1) % len(self.walk_frames)
            else:
                self.frame_index = 0

    def draw(self, screen, camera_x, camera_y):
        if self.is_walking:
            player_art = self.walk_frames[self.frame_index]
        else:
            player_art = self.idle_frames

        font = pygame.font.SysFont("Courier", 18)

        for i, line in enumerate(player_art):
            text = font.render(line, True, (0, 255, 0))
            screen.blit(text, (self.rect.x - camera_x, self.rect.y - camera_y + i * 18))
