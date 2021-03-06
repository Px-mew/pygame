import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf
from scoreboard import Scoreboard


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")
    # Создание корабля.
    ship = Ship(ai_settings, screen)
    # Создание группы для хранения пуль.
    bullets = Group()
    # Создание группы пришельцев. 
    aliens = Group()
    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Создание экземпляра для хранения игровой статистики.
    stats = GameStats(ai_settings) 
    sb = Scoreboard(ai_settings, screen, stats)


    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()