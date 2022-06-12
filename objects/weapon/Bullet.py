import pygame
import pygame.math
import pygame.sprite
from config.Config import *


class Bullet(pygame.sprite.Sprite):
    """Bullet class."""

    def __init__(
        self,
        level,
        groups: tuple,
        image_path: str,
        position: tuple,
        speed: pygame.math.Vector2,
        damage: int,
        ran: int,
        weapon,
        extra_scale=1
    ):
        """
        Init bullet.

        :param level: Level
        :param groups: tuple
        :param image_path: str: bullet image path
        :param position: tuple: bullet position in Level
        :param speed: pygame.math.Vector2: bullet speed
        :param damage: int: bullet damage
        :param ran: int: shot range
        :param weapon: ShootingWeapon: shot source weapon
        """
        super().__init__(groups)
        self.level = level
        self.weapon = weapon
        image = pygame.image.load(image_path).convert_alpha()
        width, height = image.get_width(), image.get_height()
        self.start_image = pygame.transform.scale(image, (int(width * SCALE * extra_scale), int(height * SCALE * extra_scale)))
        self.image = pygame.transform.rotate(
            self.start_image,
            self.weapon.owner.look_angle.angle_to(pygame.math.Vector2(1, 0)),
        )
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(position)
        self.rect.center = self.pos
        self.speed = speed
        self.damage = damage
        self.start_range = ran
        self.range = ran
        self.owner = self.weapon.owner

    def set_speed(self, new_speed: pygame.math.Vector2):
        """Set bullet speed.

        :param new_speed: pygame.math.Vector2: speed to set with
        """
        self.speed = new_speed

    def move(self):
        """Change bullet position."""
        self.pos += self.speed
        self.rect.center = self.pos
        self.range -= self.speed.length()

    def update(self):
        """Update bullet position."""
        self.move()
        if self.range <= 0:
            self.kill()
