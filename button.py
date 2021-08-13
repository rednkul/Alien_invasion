import pygame.font

class Button():
    def __init__(self, ai_game, msg):
        """Инициализирует атрибуты кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Назначение размеров и свойств кнопок
        self.width, self.height = 200, 50

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки и выравнивание по центру экрана
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        self.rect.center = self.screen_rect.center
        self.msg = msg
        # Сообшение кнопки создается только один раз
        self._def_position()



    def _prep_playbutton(self):
        """Преобразует msg в прямоугольник и выравнивает текст по центру"""
        self.button_color = (0, 255, 0)
        self.msg_image = self.font.render(self.msg, True, self.text_color,
                        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.rect.center = self.screen_rect.center
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Отображение пустой кнопки и вывод сообщения"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


    def _def_position(self):
        if self.msg == 'Play':
            self._prep_playbutton()
        elif self.msg == 'Hard':
            self._prep_hard_button()

        elif self.msg == 'Medium':
            self._prep_medium_button()

        elif self.msg == 'Light':
            self._prep_light_button()

    def _prep_hard_button(self):
        self.button_color = (255, 0, 0)
        self.msg_image = self.font.render(self.msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.rect.center = (680, 650)
        self.msg_image_rect.center = self.rect.center


    def _prep_medium_button(self):
        self.button_color = (254, 150, 0)
        self.msg_image = self.font.render(self.msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.rect.center = (960, 650)
        self.msg_image_rect.center = self.rect.center

    def _prep_light_button(self):
        self.button_color = (0, 255, 253)
        self.msg_image = self.font.render(self.msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.rect.center = (1240, 650)
        self.msg_image_rect.center = self.rect.center
