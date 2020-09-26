## Created by : Sumudu Madushanka
## Python version  :  Python 3.8.5

from Message import message
from display_functions import *
from game_functions import game_loop, high_score, reset_high_score
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
    item_list = ["Start Game", "High Score", "Reset High Score", "Quit Game"]
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
                    elif select_item == 2:
                        reset_high_score()
                        break
            elif event.type == pygame.MOUSEMOTION:
                m_pos = pygame.mouse.get_pos()
                m_pos_x = m_pos[0]
                m_pos_y = m_pos[1]
                if (m_pos_x > 215) and (m_pos_x < 385):
                    i = (m_pos_y - 275)//30
                    if i >= 0 and i < len(item_list):
                        select_item = i
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                m_clicked = pygame.mouse.get_pressed()
                if m_clicked == (1, 0, 0):
                    m_pos = pygame.mouse.get_pos()
                    m_pos_x = m_pos[0]
                    m_pos_y = m_pos[1]
                    if (m_pos_x > 215) and (m_pos_x < 385) and (m_pos_y > 275) and (m_pos_y < (275 + len(item_list) * 30)):
                        if select_item == (len(item_list) - 1):
                            game_over = True
                        elif select_item == 0:
                            game_loop(len_x, len_y, block_size, clock)
                        elif select_item == 1:
                            high_score()
                            break
                        elif select_item == 2:
                            reset_high_score()
                break
        pygame.event.clear()

    quit_display()

main_loop()
quit()
