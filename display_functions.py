## Created by : Sumudu Madushanka
## Last update : 8/16/2020

import pygame
from Message import message
from time import sleep

### Globle Variables ###
dis = None
width = None
height = None
block_size = None
item_font_size = None
head_font_size = None
normal_font_size = None

# Colours
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
green = (0, 255, 0)
blue = (0, 0, 255)
darkblue = (0, 0, 139)

# Init the game display
def init_display(w, h, blc_size, i_font_size, h_font_size, n_font_size):
    global dis
    global width
    global height
    global block_size
    global item_font_size
    global head_font_size
    global normal_font_size
    width = w
    height = h
    block_size = blc_size
    item_font_size = i_font_size
    head_font_size = h_font_size
    normal_font_size = n_font_size
    
    pygame.init()
    dis = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lake Nozama")

# Draw the Game menu
def draw_main_menu(item_list, select_item):
    dis.fill(white)
    message(dis, (2 * item_font_size), "Lake Nozama", green, white, width//4, (height - item_font_size)//4)
    for i in range(len(item_list)):
        if (select_item == i):
            f_colour = white
            bg_colour = blue
        else:
            f_colour = blue
            bg_colour = white
        message(dis, item_font_size, item_list[i], f_colour, bg_colour, width//3, ((height - item_font_size)//3 + ((2 + i) * item_font_size)))
    pygame.display.update()

# Display High Score
def display_high_score(high_score_list):
    dis.fill(white)
    message(dis, (2 * item_font_size), "High Score", green, white, width//4, (height - item_font_size)//4)
    
    for i in range(5):
        message(dis, item_font_size, str(i + 1) + ") " + str(high_score_list[i]), blue, white, width/3, (height - item_font_size)/3 + ((1 + i) * item_font_size))
    
    pygame.display.update()

# Game Display
def draw_initial_display(MAP, player, len_x, len_y, discoverd):
    dis.fill(white)
    message(dis, head_font_size, f"{player.getName()}", blue, white, 10, 0)
    message(dis, head_font_size, f"Health: {player.getHealth()}", green, white, 100, 0)
    message(dis, head_font_size, f"Fins: {player.hasFins()}", black, white, 300, 0)
    pygame.draw.rect(dis, darkblue, [0, head_font_size, (len_x * block_size), 5])
    
    for i in range(len_x):
        for j in range(len_y):
            if [i, j] not in discoverd:
                pygame.draw.rect(dis, gray, [(block_size * i), (block_size * (len_y - j - 1)) + (head_font_size + 5), block_size, block_size])
    
    message(dis, normal_font_size, f"{player.getName()}", black, white, (block_size * player.getCordinate().getX()) + 20, (block_size * (len_y - player.getCordinate().getY() - 1)) + 25 + (head_font_size + 5))

    for cordinate in discoverd:
        if MAP.getCordinate(cordinate[0], cordinate[1]).hasObject():
             message(dis, normal_font_size, f"{MAP.getCordinate(cordinate[0], cordinate[1]).getObject().getName()}", black, white, (block_size * cordinate[0]) + 20, (block_size * (len_y - cordinate[1] - 1)) + 5 + (head_font_size + 5))

    pygame.display.update()

# Display pop up messages
def display_popup_messages(msg):
    dis.fill(white)
    message(dis, head_font_size, msg, black, white, width//3, height//3)
    pygame.display.update()
    sleep(1)
    pygame.event.clear()
    
# Display map objects in given location box
def display_map_objects(obj, x, y):
    message(dis, normal_font_size, obj, black, white, x, y)
    pygame.display.update()

# Quit pygame
def quit_display():
    pygame.quit()