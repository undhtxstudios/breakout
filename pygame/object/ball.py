import math
import random
import pygame
from common.constants import BALL, PADDLE_STARTING_POS
from common.utils import load_images

from random import choice


class Ball:
    def __init__(self, dimension, speed, image) -> None:
        self.x, self.y = dimension
        self.speed = speed
        self.image = image
        self.direction = [1, 1]  # X-direction, Y-direction
        self.ball_rect = pygame.Rect(self.x - 10, self.y - 10, 10 * 2, 10 * 2)
        self.ball_angle = random.uniform(math.radians(30), math.radians(150))

    def draw(self, screen):
        # to do: make it a circle, or mask for collisions?
        # screen.blit(self.image, (self.x, self.y))
        pygame.draw.circle(screen, (0, 0, 255), (self.x, self.y), 10)

    def change_speed(self, speed):
        self.speed = speed

    def update(self, resolution, bricks, paddles):
        self.check_wall_collision(resolution=resolution)
        self.check_paddle_collision(paddles)
        self.check_brick_collision(bricks)
        self.x += self.speed * self.direction[0] * math.cos(self.ball_angle)
        self.y += self.speed * self.direction[1] * math.sin(self.ball_angle)
        self.ball_rect.x = self.x
        self.ball_rect.y = self.y

    def check_paddle_collision(self, paddles):
        paddle = paddles[0]
        paddle_rect = paddles[0].paddle_rect

        if self.ball_rect.colliderect(paddle_rect):
            hit_position = (self.x - (paddle.left + paddle.width / 2)) / (paddle.width / 2)
            max_bounce_angle = math.radians(75)

            ball_angle = hit_position * max_bounce_angle

            self.direction[1] = -1 * self.direction[1] * math.cos(ball_angle) # Opposite y-direction
            self.direction[0] = (
                self.direction[0] * math.sin(ball_angle)
            )  # Random choice for x-direction

    def check_wall_collision(self, resolution):
        if self.x <= 0 or self.x >= resolution[0]:
            self.direction[0] = -1 * self.direction[0]
        if self.y <= 0 or self.y > PADDLE_STARTING_POS[0]:
            self.direction[1] = -1 * self.direction[1]
        # if (self.y > PADDLE_STARTING_POS[0]):
        #     running = False
        #     return running

    def check_brick_collision(self, bricks):
        for brick in bricks:
            if self.ball_rect.colliderect(brick.brick_rect):
                bricks.remove(brick)
                self.direction[1] = -1 * self.direction[1]
                self.direction[0] = (
                -1 * self.direction[0]
            )
                break
        self.ball_rect.x = self.x
        self.ball_rect.y = self.y


class Balls:
    def __init__(self):
        self.balls = []
        self.images = []

    def load(self, theme, resolution):
        self.images = load_images(theme, BALL, resolution)
        # to do: randomize default position
        # make sure when changing resolution, if positions are out of bounds,
        # they get adjusted
        self.balls = [
            Ball((100, 100), 0.2, choice(self.images))
        ]  # , Ball((80, 80), 10, choice(self.images))]

    def add(self, x, y, speed):
        # check bounds?
        ball = Ball(x, y, speed)
        self.balls.append(ball)

    def remove(self, ball):
        if ball in self.balls:
            self.balls.remove(ball)

    def update(self, resolution, bricks, paddles):
        for ball in self.balls:
            ball.update(resolution=resolution, bricks=bricks, paddles=paddles)

    def draw(self, screen):
        for ball in self.balls:
            ball.draw(screen)

    def change_speed(self, speed):
        for ball in self.balls:
            ball.change_speed(speed)

    def reload(self, theme, resolution):
        self.images = load_images(theme, BALL, resolution)
        for ball in self.balls:
            # adjust position for resolution
            ball.image = choice(self.images)

    def reset(self):
        self.balls.clear()
