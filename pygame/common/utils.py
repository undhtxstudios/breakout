import os
import pygame
from common.constants import THEME
    
def load_images(theme, object, resolution):
    images = []
    width, height = resolution
    folder_path = os.path.join(THEME, theme, object, f'{width}x{height}')
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith(('.png', '.jpg', '.jpeg')):
            image = pygame.image.load(file_path).convert_alpha()
            images.append(image)
    return images