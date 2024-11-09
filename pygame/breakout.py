import pygame
import sys
from object.ball import Balls
from common.constants import (
    BACKGROUND,
    BALLS,
    BRICKS,
    PADDLES,
    themes,
    resolutions,
)
from object.brick import Bricks
from object.paddle import Paddles


class Breakout:
    def __init__(self, resolution, fps, theme) -> None:
        self.resolution = resolution
        self.fps = fps
        self.theme = theme

        pygame.init()
        pygame.display.set_caption("Atari Breakout")
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(1, 10)

        self.running = True

        self.assets = {}
        self.load_assets()

    def load_assets(self):
        self.assets[BALLS] = Balls()
        self.assets[BALLS].load(self.theme, self.resolution)
        self.assets[PADDLES] = Paddles(self.resolution[0])
        self.assets[PADDLES].load(self.theme, self.resolution)

        self.assets[BRICKS] = Bricks()
        self.assets[BRICKS].load(self.theme, self.resolution)

    def reload_assets(self, theme, resolution):
        if theme not in themes or resolution not in resolutions:
            print("Invalid theme or resolution, continuing without changes...")
            return
        if theme == self.theme and resolution == self.resolution:
            return
        for _, asset in self.assets.items():
            asset.reload(self.theme, self.resolution)

    def draw_assets(self):
        for _, asset in self.assets.items():
            asset.draw(self.screen)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # paddle movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.assets[PADDLES].move_left()
                if event.key == pygame.K_RIGHT:
                    self.assets[PADDLES].move_right()

            # custom events

    def run(self):
        while self.running:
            self.screen.fill(BACKGROUND)
            self.handle_event()
            self.draw_assets()
            self.assets[BALLS].update(self.resolution, self.assets[BRICKS])
            pygame.display.update()


Breakout((640, 480), 60, "original").run()
