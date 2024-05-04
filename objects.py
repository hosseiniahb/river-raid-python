import pygame
from constants import *
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_LEFT,
    RLEACCEL
)
import random as rnd

pygame.mixer.music.load("./music/game_music.mp3")
pygame.mixer.music.play(loops=-1)


move_up_sound = pygame.mixer.Sound("./music/Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("./music/Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("./music/Collision.ogg")


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("./images/jet.png").convert()
        self.surf.set_colorkey((255,255,255),pygame.RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, keys):
        if keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
        if keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if keys[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("./images/missile.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                rnd.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                rnd.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = rnd.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.surf = pygame.image.load("./images/cloud.png").convert()
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                rnd.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                rnd.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = 5
    
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()