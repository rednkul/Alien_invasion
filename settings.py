class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        #self.screen_width = 1200
        #self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Настройки корабля бля
        #self.ship_speed = 2
        self.ship_limit = 3

        # Параметры снаряда
        #self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (229, 81, 55)

        # Максимальное количество снарядов на экране
        self.bullets_allowed = 3

        # Настройки пришельцев
        #self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        #fleet_direction = 1 - движение вправо; -1 - влево
        self.fleet_direction = 1

        # Темп ускорения игры
        self.speed_up_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed = 2
        self.bullet_speed = 10
        self.alien_speed = 1.0

        # fleet_direction = 1 - движение вправо; -1 - влево
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.ship_speed *= self.speed_up_scale
        self.bullet_speed *= self.speed_up_scale
        self.alien_speed *= self.speed_up_scale


