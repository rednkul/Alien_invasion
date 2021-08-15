import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс управления кораблем."""

    def __init__(self, ai_game, lives = False):
        """Инициализирует корабль и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/sprite_ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

        # Определяет, является ли экземпляр обозначением оставшихся кораблей или игровым
        self.lives = lives
        # Уменьшает изображение, если экземпляр - иконка оставшейся жизни
        self._min_size()

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Обновляется атрибут x, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Размещает корабль в центре нижней стороны"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def _min_size(self):
        """Уменьшает изображение корабля, если экземпляр используется"""
        """для обозначения оставшихся жизней."""
        if self.lives == True:
            self.min_image = pygame.transform.scale(self.image,
                            (self.rect.width // 4, self.rect.height // 4))
            self.image = self.min_image
            self.rect = self.image.get_rect()
