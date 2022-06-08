import pygame
from config.Config import *
from objects.weapon.Bullet import Bullet
from objects.weapon.Weapon import Weapon


class Shield(Weapon):
    def __init__(self, level, groups, image_path, owner, owner_distance, cooldown):
        # maybe change to const path, cooldown
        super().__init__(level, groups, image_path, owner, owner_distance, cooldown)

    def reflect_bullets(self):
        if self.last_use >= self.cooldown:
            self.last_use = 0
            self.uses[0] = True

    def redirect_bullet(self, bullet: Bullet):
        new_speed = self.owner.look_angle * bullet.speed.length() * BULLET_REFLECTION_ACCELERATION
        bullet.set_speed(new_speed)
        bullet.damage *= BULLET_REFLECTION_DAMAGE_UP

