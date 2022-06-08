import pygame
import pygame.math
import pygame.sprite
from config.Config import *


class Bullet(pygame.sprite.Sprite):
    def __init__(self, level, groups, image_path, position, speed: pygame.math.Vector2, damage, ran, weapon):
        super().__init__(groups)
        self.level = level
        self.start_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.start_image
        self.rect = self.image.get_rect()
        self.pos = pygame.math.Vector2(position)
        self.rect.center = self.pos
        self.speed = speed
        self.damage = damage
        self.range = ran
        self.weapon = weapon

    def set_speed(self, new_speed: pygame.math.Vector2):
        self.speed = new_speed

    def move(self):
        self.image = pygame.transform.rotate(self.start_image,
                                             self.weapon.owner.look_angle.angle_to(pygame.math.Vector2(1, 0)))
        self.pos += self.speed
        self.rect.center = self.pos
        self.range -= self.speed.length()

    def update(self):
        self.move()
        if self.range <= 0:
            self.kill()
