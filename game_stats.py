class GameStats():
    """Отслеживание статистики игры Alien Invasion"""
    def __init__(self, ai_game):
        """Инициализирует статистику"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0

        # Игра запускается в неактивном состоянии
        self.game_active = False
        self.difficult_choosen = False

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit
        self.score = 0

