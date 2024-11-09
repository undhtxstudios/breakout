from random import choice

from common.constants import PADDLE_STARTING_POS, PADDLE
from common.utils import load_images


class Paddle:
    def __init__(self, dimension, screen_width, image) -> None:
        self.top, self.left, self.width, self.height = dimension
        self.right = self.left + self.width
        self.speed = 3
        self.screen_width = screen_width
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (self.left, self.top))

    def change_speed(self, speed):
        self.speed = speed

    def move_left(self):
        if self.left > 0:
            self.left = self.left - self.speed

    def move_right(self):
        if self.left < self.screen_width - self.width:
            self.left = self.left + self.speed


class Paddles:
    def __init__(self, screen_width):
        self.screen_width = screen_width
        self.images = []

    def load(self, theme, resolution):
        self.images = load_images(theme, PADDLE, resolution)
        # adjust dimensions (widht and height)
        # according to resolution (map in constants.py)
        self.paddles = [
            Paddle(PADDLE_STARTING_POS, self.screen_width, choice(self.images))
        ]

    def draw(self, screen):
        for paddle in self.paddles:
            paddle.draw(screen)

    def move_left(self):
        for paddle in self.paddles:
            paddle.move_left()

    def move_right(self):
        for paddle in self.paddles:
            paddle.move_right()

    def add_paddle(self, dimension):
        self.paddles.append(
            Paddle(dimension, self.screen_width, choice(self.paddle_images))
        )

    def change_speed(self, speed):
        for paddle in self.paddles:
            paddle.change_speed(speed)

    def reload(self, theme, resolution):
        self.images = load_images(theme, PADDLE, resolution)
        for paddle in self.paddles:
            # paddle.width, paddle.height = (adjust, adjust)
            paddle.image = choice(self.images)
