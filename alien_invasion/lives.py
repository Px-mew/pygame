import pygame
from pygame.sprite import Sprite

class Life(Sprite):
    """ Класс 'Жизни'."""
    def __init__(self, ai_settings, screen):
        super(Life, self).__init__()

        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения сердца и получение прямоугольника.
        self.image = pygame.image.load('F:\\Program\\pygame\\alien_invasion\\images\\heart.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
