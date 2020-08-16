## Created by : Sumudu Madushanka
## Last update : 8/16/2020

from Message import message
from display_functions import *
from game_functions import game_loop, high_score
import pygame

### Global Variables ###
# Font
item_font_size = 30
head_font_size = 25
normal_font_size = 20

# Display
block_size = 65
len_x = 10
len_y = 10
width = block_size * len_x
height = block_size * len_y + head_font_size + 5

#Clock 
clock = pygame.time.Clock()

init_display(width, height, block_size, item_font_size, head_font_size, normal_font_size)

### Main Function ###
def main_loop():
    # Basic Variables
    game_over = False
    item_list = ["Start Game", "High Score", "Quit Game"]
    select_item = 0

    while not game_over:
        draw_main_menu(item_list, select_item)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                break
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    tmp = select_item - 1
                    select_item = ((len(item_list) - 1) if tmp < 0 else tmp)
                    break
                elif event.key == pygame.K_DOWN:
                    tmp = select_item + 1
                    select_item = (0 if tmp > (len(item_list) - 1) else tmp)
                    break
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    if select_item == (len(item_list) - 1):
                        game_over = True
                    elif select_item == 0:
                        game_loop(len_x, len_y, block_size, clock)
                    elif select_item == 1:
                        high_score()
                        break
        pygame.event.clear()

    quit_display()

main_loop()
quit()
