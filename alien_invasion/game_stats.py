class GameStats():
    """Отслеживание статистики игры."""
    
    def __init__(self, ai_settings):
        """Инициализирует статистику."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False
        # Рекорд не должен сбрасываться.
        with open('F:\\Program\\pygame\\alien_invasion\\high_score.txt', 'r') as file:
            self.high_score = int(file.readline())

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0