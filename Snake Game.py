import pygame

# Initialize Pygame
pygame.init()

# Set up the display window
screen_width = 640
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.flip()

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Create food
food = pygame.Rect(0, 0, 25, 25)
food_color = RED

# Initialize score and length of snake
score = 0
snake_length = 8
position = [(50, 50)] * snake_length
for i in range(len(position)):
    position[i] = [pygame.randint(0, screen_width - 1), pygame.randint(0,