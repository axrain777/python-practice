#ReadMe
-Use Pygame to create a graphical game window
-Handle user input to control the game
-Create and update game objects
-Detect collisions in a game
-Display and update the game score

1.Create a new file named snake_game.py

#creating a blank file named snake_game.py
touch snake_game.py

#install pygame(pre-written code)
sudo pip install pygame

2.Import necessary modules

#import the pygame and random modules
#i use nano to import pygame and random modules because terminal cant use this python code
nano snake_game.py

import pygame

#random module helps to bring the random elements to the game , making it more fun
import random

#initialize Pygame:
pygame.init()

#Set up the game window by defining the width,height and frame per second of the game window. do in inside nano snake_game.py
WIDTH = 800
HEIGHT = 600
FPS = 10

#Define colors of the game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BACKGROUND_COLOR = (50, 50, 50)

#setting the display size using the defined width and height,title of the game and time in the game
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

#Set up the snake by defining the block size and speed of the snake
snake_block_size = 20
snake_speed = 5

#Set up the game variables by defining the font styles and font sizes for displaying the score:
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

#setting up block size to add when snake eats and power up
