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
            # Відслідковування подій клавіатури та миші
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            # Оновлення екрану
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Відображення останнього прорисованого екрану
            pg.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
