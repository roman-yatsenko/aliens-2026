import pygame as pg


class Button:
    """Клас для кнопок у грі"""

    def __init__(self, ai_game, msg):
        """ініціалізує атрибути кнопки"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Призначення розмірів та властивостей кнопки
        self.width, self.height = 200, 50
        self.button_color = "green"
        self.text_color = "white"
        self.font = pg.font.SysFont(None, 48)

        # Вирівнювання кнопки по центру екрана
        self.rect = pg.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Текст кнопки створюється тільки один раз
        self._prep_msg(msg)

    def draw_button(self):
        """Відображає пусту кнопку та виводе текст"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_inage_rect)

    def _prep_msg(self, msg):
        """Перетворює msg в прямокутник і вирівнює текст по центру"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_inage_rect = self.msg_image.get_rect()
        self.msg_inage_rect.center = self.rect.center
