import sys

import pygame as pg

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Клас для управління ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізує гру та створює ігрові ресурси"""
        pg.init()
        self.clock = pg.time.Clock()
        self.settings = Settings()

        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pg.display.set_caption("Alien Invasion 2026")

        # Створення ігрових об'єктів
        self.ship = Ship(self)

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Обробляє натиснення клавіш та події миші"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    # Переміщуємо корабель праворуч
                    self.ship.rect.x += 1

    def _update_screen(self):
        """Оновлює зображення на екрані та відображає новий екран"""
        # Оновлення екрану
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Відображення останнього прорисованого екрану
        pg.display.flip()


if __name__ == "__main__":
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
