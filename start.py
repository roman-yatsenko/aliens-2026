import sys

import pygame as pg


class AlienInvasion:
    """Клас для управління ресурсами та поведінкою гри"""

    def __init__(self):
        """Ініціалізує гру та створює ігрові ресурси"""
        pg.init()
        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode((1200, 800))
        pg.display.set_caption("Alien Invasion 2026")

        # Призначення коліру фону
        self.bg_color = "lightgray"  # (230, 230, 230)

    def run_game(self):
        """Запуск основного циклу гри"""
        while True:
            # Відслідковування подій клавіатури та миші
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            # Оновлення екрану
            self.screen.fill(self.bg_color)

            # Відображення останнього прорисованого екрану
            pg.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    # Створення екземпляру та запуск гри
    ai = AlienInvasion()
    ai.run_game()
