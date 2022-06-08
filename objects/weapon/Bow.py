from objects.weapon.ShootingWeapon import ShootingWeapon
from config.Config import *


class Bow(ShootingWeapon):
    def __init__(self, level, owner):
        super().__init__(level, BOW_IMAGE_PATH, owner, BOW_DISTANCE, BOW_COOLDOWN, ARROW_SPEED, ARROW_DAMAGE, ARROW_RANGE, ARROW_IMAGE_PATH)  # later <bullet_speed, ..., bullet_img_path> change to prepared Bullet examplar or to fabric
