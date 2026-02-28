class Settings:
    """Клас для зберігання всіх налаштувань гри"""

    def __init__(self):
        """Ініціалізує налаштування гри"""
        # Параметри екрану
        self.screen_width = 1200
        self.screen_height = 800
        self.dark_mode = True
        self.bg_color = "black" if self.dark_mode else "gray90"

        # Налаштування корабля
        self.ship_limit = 3

        # Налаштування снарядів
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = "firebrick2"
        self.bullets_allowed = 3

        # Налаштування прибульців
        self.fleet_drop_speed = 10

        # Параметри зірок
        self.star_limit = 100
        self.star_speed = 0.1
        self.star_start_color = 150
        self.star_color_limit = 256
        self.star_color_step = 0.15
        self.star_radius = 3

        # Темп пришвидшення гри
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Ініціалізує налаштування, що змінюються під час гри"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 1

        # fleet_direction = 1 якщо флот рухається, -1 якщо ліворуч
        self.fleet_direction = 1

        # Підрахунок очок
        self.alien_points = 50

    def increase_speed(self):
        """Збільшує налаштування швидкості"""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
