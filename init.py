import pygame
from constants import *

pygame.mixer.init()

pygame.init()
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("River Raid")