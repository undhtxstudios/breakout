from common.constants import BRICK_WIDTH, BRICK_HEIGHT, BRICK_SPACE, BRICK
from common.utils import load_images
from random import choice


class Brick:
    def __init__(self, dimension, is_broken, image) -> None:
        self.top, self.left, self.width, self.height = dimension
        self.is_broken = is_broken
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (self.left, self.top))


class Bricks:
    def __init__(self, count_x=4, count_y=4) -> None:
        self.bricks = []
        self.images = []
        self.count_x = count_x
        self.count_y = count_y
        self.top = 0

    def load(self, theme, resolution):
        self.images = load_images(theme, BRICK, resolution)

        for i in range(0, self.count_y):
            for j in range(0, self.count_x):
                left = (BRICK_WIDTH * j) + (BRICK_SPACE * j)
                self.bricks.append(
                    Brick(
                        (self.top + 5, left + 5, BRICK_WIDTH, BRICK_HEIGHT),
                        False,
                        choice(self.images),
                    )
                )
            self.top = (BRICK_HEIGHT * i) + (BRICK_SPACE * i)

    def draw(self, screen):
        for brick in self.bricks:
            brick.draw(screen=screen)

    def reload(self, theme, resolution):
        self.images = load_images(theme, BRICK, resolution)
        for brick in self.bricks:
            # adjust for resolution
            brick.image = choice(self.images)
