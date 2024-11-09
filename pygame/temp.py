import pygame
import sys

class Temp:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Atari Breakout")

        self.screen = pygame.display.set_mode((1280, 720))

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



Temp().run()