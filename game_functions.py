## Created by : Sumudu Madushanka
## Last update : 8/16/2020

import pygame
import json
from grid import Map
from treasure import Treasure
from flower import Flower, LotusFlower, DangerFlower, KillerFlower
from fish import Fish, TheifFish, RubberEatingFish, DangerFish, KillerFish
from player import Player
from display_functions import display_high_score, draw_initial_display, display_normal_messages, display_special_messages
from time import sleep
from random import randint

# Init the object cordinates
def init_object_cordinate(MAP):
    cordinate = [randint(0, (MAP.getLenX() - 1)), randint(1, (MAP.getLenY() - 1))]
    while MAP.getCordinate(cordinate[0], cordinate[1]).hasObject():
        cordinate = [randint(0, (MAP.getLenX() - 1)), randint(1, (MAP.getLenY() - 1))]
    return cordinate

# Init the game map objects
def init_game(MAP, tr_x, tr_y):
    # Treasure
    treasure = Treasure()
    MAP.getCordinate(tr_x, tr_y).setObject(treasure)

    # Flowers
    # Lotus Flowers
    for i in range(4):
        lf = LotusFlower()
        cordinate = init_object_cordinate(MAP)
        MAP.getCordinate(cordinate[0], cordinate[1]).setObject(lf)

    # Danger Flowers
    for i in range(4):
        df = DangerFlower(randint(1,99))
        cordinate = init_object_cordinate(MAP)
        MAP.getCordinate(cordinate[0], cordinate[1]).setObject(df)

    # Killer Flowers
    for i in range(4):
        kf = KillerFlower()
        cordinate = init_object_cordinate(MAP)
        MAP.getCordinate(cordinate[0], cordinate[1]).setObject(kf)

    # Fish
    # Theif Fish
    for i in range(4):
        tfh = TheifFish()
        cordinate = init_object_cordinate(MAP)
        MAP.getCordinate(cordinate[0], cordinate[1]).setObject(tfh)

    # Rubber Eating Fish
    for i in range(4):
        rfh = RubberEatingFish()
        cordinate = init_object_cordinate(MAP)
        MAP.getCordinate(cordinate[0], cordinate[1]).setObject(rfh)

    # Danger Fish
    for i in range(4):
        dfh = DangerFish(randint(0, 99))
        cordinate = init_object_cordinate(MAP)
        MAP.getCordinate(cordinate[0], cordinate[1]).setObject(dfh)

    # Killer Fish
    for i in range(4):
        kfh = KillerFish()
        cordinate = init_object_cordinate(MAP)
        MAP.getCordinate(cordinate[0], cordinate[1]).setObject(kfh)

# Show high score
def high_score():
    show = True
    score_file_name = "high_score.json"

    try:
        high_score_file = open(score_file_name, "r")
        high_score_dict = json.load(high_score_file)
        high_score_file.close()

        high_score_list = high_score_dict["high score"]
        
    except FileNotFoundError:
        high_score_dict = {}
        high_score_dict["high score"] = [0 for i in range(5)]
        
        high_score_file = open(score_file_name, "w")
        json.dump(high_score_dict, high_score_file, indent = 4)
        high_score_file.close()

        high_score_list = high_score_dict["high score"]
        
    while show:
        display_high_score(high_score_list)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYUP and (event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER)):
                show = False
                break
        pygame.event.clear()

# Update High Score
def update_high_score(score):
    score_file_name = "high_score.json"
    try:
        high_score_file = open(score_file_name, "r")
        high_score_dict = json.load(high_score_file)
        high_score_file.close()
        high_score_list = high_score_dict["high score"]

    except FileNotFoundError:
        high_score_dict = {}
        high_score_dict["high score"] = [0 for i in range(5)]
        
        high_score_file = open(score_file_name, "w")
        json.dump(high_score_dict, high_score_file, indent = 4)
        high_score_file.close()

        high_score_list = high_score_dict["high score"]

    place = 6
    for i in range(5):
        if score > high_score_list[i]:
            high_score_list = high_score_list[:i] + [score] + high_score_list[i:4]
            high_score_dict["high score"] = high_score_list
            place = i + 1
            break

    if place < 6:
        display_special_messages(f"High score: {score}")
    else:
        display_special_messages(f"Your score: {score}")

    high_score_file = open(score_file_name, "w")
    json.dump(high_score_dict, high_score_file, indent = 4)
    high_score_file.close()

# Game function
def game_loop(len_x, len_y, block_size, clock):
    # Map
    MAP = Map(len_x, len_y)
    Player.setMap(MAP)

    # Treasure Cordinates
    tr_x = len_x - 1
    tr_y = len_y - 1

    # Init game objects
    init_game(MAP, tr_x, tr_y)

    # Init Player
    player_1 = Player("P1")
    MAP.getCordinate(0, 0).setPlayer(player_1)
    around = {
        "up" : [player_1.getCordinate().getX(), player_1.getCordinate().getY() + 1],
        "down" : [player_1.getCordinate().getX(), player_1.getCordinate().getY() - 1],
        "left" : [player_1.getCordinate().getX() - 1, player_1.getCordinate().getY()],
        "right" : [player_1.getCordinate().getX() + 1, player_1.getCordinate().getY()]
    }
    discoverd = []
    discoverd.append([player_1.getCordinate().getX(), player_1.getCordinate().getY()])
    discoverd.append([tr_x, tr_y])

    # Draw initial Game Display
    draw_initial_display(MAP, player_1, len_x, len_y, discoverd)

    # Game Loop
    game_over = False
    cell_updated = False
    quiting_time = 2
    while not game_over:
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quiting_time = 0
                game_over = True
                pygame.event.clear()
                break
            elif event.type == pygame.KEYUP:
                direction = None
                if event.key == pygame.K_LEFT:
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                elif event.key == pygame.K_UP:
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    direction = "down"

                # Swim player
                if direction != None:
                    if MAP.hasCordinate(around[direction][0], around[direction][1]):
                        player_1.swim(direction)
                        if around[direction] not in discoverd:
                            discoverd.append(around[direction])
                        around = {
                            "up" : [player_1.getCordinate().getX(), player_1.getCordinate().getY() + 1],
                            "down" : [player_1.getCordinate().getX(), player_1.getCordinate().getY() - 1],
                            "left" : [player_1.getCordinate().getX() - 1, player_1.getCordinate().getY()],
                            "right" : [player_1.getCordinate().getX() + 1, player_1.getCordinate().getY()]
                        }
                        draw_initial_display(MAP, player_1, len_x, len_y, discoverd)
                        cell_updated = False
                        pygame.event.clear()
                        break

        if not cell_updated:
            if isinstance(player_1.getCordinate().getObject(), Treasure):
                player_1.takeTreasure(player_1.getCordinate().getObject())
            elif isinstance(player_1.getCordinate().getObject(), Fish):
                player_1.getCordinate().getObject().attack(player_1)
            elif isinstance(player_1.getCordinate().getObject(), Flower):
                if not isinstance(player_1.getCordinate().getObject(), LotusFlower):
                    player_1.getCordinate().getObject().attack(player_1)
            
            draw_initial_display(MAP, player_1, len_x, len_y, discoverd)
            
            if player_1.hasBinocular():
                has_lotus = player_1.useBinocular()
                for key in around.keys():
                    if has_lotus[key]:
                        display_normal_messages(f"{MAP.getCordinate(around[key][0], around[key][1]).getObject().getName()}", (block_size * around[key][0]) + 20, (block_size * (len_y - around[key][1] - 1)) + 5 + 30)

            if not (MAP.getCordinate(tr_x, tr_y).hasObject() and isinstance(MAP.getCordinate(tr_x, tr_y).getObject(), Treasure)):
                game_over = True
            elif player_1.getHealth() == 0:
                display_special_messages(f"{player_1.getName()} Died")
                draw_initial_display(MAP, player_1, len_x, len_y, discoverd)
                game_over = True
            elif player_1.hasFins() == False:
                display_special_messages(f"{player_1.getName()} Lost his Fins")
                draw_initial_display(MAP, player_1, len_x, len_y, discoverd)
                game_over = True
            cell_updated = True
        clock.tick(15)
    
    # Game over
    for i in range(len_x):
        for j in range(len_y):
            if MAP.getCordinate(i, j).hasObject():
                display_normal_messages(f"{MAP.getCordinate(i, j).getObject().getName()}", (block_size * i) + 20, (block_size * (len_y - j - 1)) + 5 + 30)
    sleep(quiting_time)
    if player_1.hasTreasure():
        score = player_1.getHealth()
        update_high_score(score)
    display_special_messages(f"Game Over!")