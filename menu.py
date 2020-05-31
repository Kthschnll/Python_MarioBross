import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame
import time

# import skrits from project
from level import get_level_array

pygame.init()

# wichtig: - absolute Postion des Player -> insgesamter Bewegungfortschritt; zurückgelegte distanz des Player
#          - raltive Position von Player -> x-Position auf dem Bildschirm
# todo (am Ende):   - extra: in allen Methoden angeben wie sie getestet werden können
#                   - in Methoden/Funktionen todos schreiben wie Projekt erweitert werden kann

# OS-Umgebung ---WIN10.10.02

"""
from PIL import Image, ImageGrab  # für crop & spiegeln
# Methode um Bilder zu spiegeln 
for myfile in only_files:
    if "right" in myfile:
        img = Image.open(resources_path_player + myfile)
        img.transpose(Image.FLIP_LEFT_RIGHT).save(resources_path_player + "transpose_" + myfile)
"""

# gaming constants
DISPLAYWIDTH = 1000
DISPLAYHEIGHT = 600
BLOCKWIDTH = 50  # BLOCKWIDTH so wählen dass gerade DISPLAYWIDTH/BLOCKWITDH = gerade Zahl
BLOCKHEIGHT = 50
DISPLAYFLAG = 0
DISPLAYCOLBIT = 32

NORMAL_GROUND = DISPLAYHEIGHT - 2 * BLOCKHEIGHT  # normalground ist die kleinste Höhe auf der sich Spieler befindet #todo sollte unnötig werden, wenn player Gravitation hat und von oben auf Displayer föllt
# level_array ist Liste, in dieser sind: x*level_lenght Listen von der jede y Werte hat
PLAYERHEIGHT = 50
PLAYERWIDTH = 40

# define_blocks
DECORATION_BLOCK = [22, 23, 29, 30, 36, 37, 40, 51, 52, 53, 58, 59, 60, 65, 66, 67, 72, 73, 74]
POWERUP_BLOCK = [56, 57, 63, 64]
RARE_BLOCK = [45, 46, 47, 48]
END_BLOCK = 11  # Ende von Spiel
ENEMY_SPAWN = [54, 55, 61, 62]
# nonpassable = alle Anderen

# menu grafics
resources_path = "res/menu/"
resources_path_level_background = "res/level_background/"
resources_path_enemy = "res/enemy/1/"
menu_background = pygame.transform.scale(pygame.image.load(resources_path + "Background.png"), (1000, 600))
menu_navbar = pygame.transform.scale(pygame.image.load(resources_path + "Navbar_back.png"), (1000, 40))
level_background = pygame.transform.scale(pygame.image.load(resources_path + "Level_back.png"), (240, 175))
level_place_holder = pygame.transform.scale(pygame.image.load(resources_path + "level_place_holder.png"), (240, 175))
options_menu_background = pygame.transform.scale(pygame.image.load(resources_path + "Option_menu_background.png"),
                                                 (200, 110))
default_img = pygame.transform.scale(pygame.image.load(resources_path + "default_img.png"), (1, 1))

# load buttons
button_names = ["_sdt", "_hower", "_clicked"]
options_button_names = ["", "_hower", "_click"]
check_box_names = ["cb_unchecked", "cb_hover", "cb_checked2"]
play_button_names = ["_std", "_level", "_click"]
button_image_list = []
options_button_list = []
cb_img_list = []
play_button_img_list = []

for i in range(len(button_names)):
    button_image_list.append(
        pygame.transform.scale(pygame.image.load(resources_path + "button" + button_names[i] + ".png"), (90, 30)))
    options_button_list.append(
        pygame.transform.scale(pygame.image.load(resources_path + "button_options" + options_button_names[i] + ".png"),
                               (30, 30)))
    cb_img_list.append(
        pygame.transform.scale(pygame.image.load(resources_path + check_box_names[i] + ".png"), (30, 30)))
    play_button_img_list.append(
        pygame.transform.scale(pygame.image.load(resources_path + "Play_button" + play_button_names[i] + ".png"),
                               (240, 175)))

# load tileset
tileset = pygame.transform.scale(pygame.image.load("res/level/nature-paltformer-tileset-16x16.png"),
                                 (350, 550))

# load charrackter sprites
run_right_img_list = []
run_left_img_list = []
stay_img_list = []
jump_right_img_list = []
jump_left_img_list = []
red_run_right_img_list = []
red_run_left_img_list = []
red_stay_img_list = []
red_jump_right_img_list = []
red_jump_left_img_list = []

resources_path_player = "res/"
skin_list = ["std_skin/", "red_skin/"]

# run images
for i in range(8):
    run_right_img_list.append(
        pygame.transform.scale(pygame.image.load(resources_path_player + skin_list[0] + "run_right" + str(i) + ".png"),
                               (PLAYERWIDTH, PLAYERHEIGHT)))
    run_left_img_list.append(pygame.transform.flip(
        pygame.transform.scale(pygame.image.load(resources_path_player + skin_list[0] + "run_right" + str(i) + ".png"),
                               (PLAYERWIDTH, PLAYERHEIGHT)), True, False))
    red_run_right_img_list.append(
        pygame.transform.scale(
            pygame.image.load(resources_path_player + skin_list[1] + "run_right" + str(i) + "_red.png"),
            (PLAYERWIDTH, PLAYERHEIGHT)))
    red_run_left_img_list.append(pygame.transform.flip(
        pygame.transform.scale(
            pygame.image.load(resources_path_player + skin_list[1] + "run_right" + str(i) + "_red.png"),
            (PLAYERWIDTH, PLAYERHEIGHT)), True, False))
# stay images
for i in range(12):
    stay_img_list.append(
        pygame.transform.scale(pygame.image.load(resources_path_player + skin_list[0] + "stand" + str(i) + ".png"),
                               (PLAYERWIDTH, PLAYERHEIGHT)))
    red_stay_img_list.append(
        pygame.transform.scale(pygame.image.load(resources_path_player + skin_list[1] + "stand" + str(i) + "_red.png"),
                               (PLAYERWIDTH, PLAYERHEIGHT)))
# jump images
for i in range(4):
    jump_left_img_list.append(
        pygame.transform.scale(pygame.image.load(resources_path_player + skin_list[0] + "jump_left" + str(i) + ".png"),
                               (PLAYERWIDTH, PLAYERHEIGHT)))
    jump_right_img_list.append(pygame.transform.flip(
        pygame.transform.scale(pygame.image.load(resources_path_player + skin_list[0] + "jump_left" + str(i) + ".png"),
                               (PLAYERWIDTH, PLAYERHEIGHT)), True, False))
    red_jump_left_img_list.append(
        pygame.transform.scale(
            pygame.image.load(resources_path_player + skin_list[1] + "jump_left" + str(i) + "_red.png"),
            (PLAYERWIDTH, PLAYERHEIGHT)))
    red_jump_right_img_list.append(pygame.transform.flip(
        pygame.transform.scale(
            pygame.image.load(resources_path_player + skin_list[1] + "jump_left" + str(i) + "_red.png"),
            (PLAYERWIDTH, PLAYERHEIGHT)), True, False))

jump_mid_img_list = [jump_right_img_list[0], jump_right_img_list[0], jump_right_img_list[3]]
red_jump_mid_img_list = [red_jump_right_img_list[0], red_jump_right_img_list[0], red_jump_right_img_list[3]]

# load enemy sprites
green_enemy_right = []
green_enemy_left = []
for i in range(8):
    green_enemy_right.append(
        pygame.transform.scale(pygame.image.load(resources_path_enemy + "green_alien" + str(i) + ".png"),
                               (PLAYERWIDTH, PLAYERHEIGHT)))
    green_enemy_left.append(pygame.transform.flip(green_enemy_right[i], True, False))

# load level background
background_img = []
for i in range(5):
    background_img.append(
        pygame.transform.scale(pygame.image.load(resources_path_level_background + "bg" + str(i + 1) + ".png"),
                               (1000, 600)))

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
# GREEN = (0, 255, 0) not used
BLUE = (0, 153, 220)
GRAY = (109, 107, 118)

# amount of level in level menu
level_count = 6


class Button:
    def __init__(self, button_text, button_rect, function, is_clicked=False, button_color=button_image_list[0],
                 image_below=default_img, is_painted=0):
        self.button_color = button_color
        self.button_text = button_text
        self.button_rect = button_rect
        self.is_clicked = is_clicked
        self.function = function
        self.is_painted = is_painted
        self.image_below = image_below

    def draw_self(self):
        if self.is_clicked:
            if self.button_color in options_button_list:
                self.button_color = options_button_list[2]
            elif self.button_color in cb_img_list:
                self.button_color = cb_img_list[2]
            elif self.button_color in play_button_img_list:
                self.button_color = play_button_img_list[2]
            else:
                self.button_color = button_image_list[2]

        gameDisplay.blit(self.button_color, (self.button_rect.x, self.button_rect.y))
        static_display(self.button_text, 20, WHITE, (self.button_rect.x + 43, self.button_rect.y + 18))

    def action(self, game_state):
        stay = True
        if self.function != game_state:
            game_state = self.function
        elif game_state == 3 and self.function == 3:
            game_state = 0
        return game_state


# create buttons
home_button = Button("Home", pygame.Rect(4, 5, 90, 30), 0)
level_button = Button("Level", pygame.Rect(98, 5, 90, 30), 1)
scores_button = Button("Scores", pygame.Rect(192, 5, 90, 30), 2)
options_button = Button("", pygame.Rect(966, 5, 30, 30), 3, False, options_button_list[0])
check_box_music = Button("", pygame.Rect(950, 52, 30, 30), 4, False, cb_img_list[0])
check_box_sound = Button("", pygame.Rect(950, 92, 30, 30), 4, False, cb_img_list[0])
play_button = Button("", pygame.Rect(70, 90, 240, 175), 5, False, play_button_img_list[0], level_place_holder)
menu_button_list = [home_button, level_button, scores_button]
check_box_list = [check_box_music, check_box_sound]


class Skin:
    def __init__(self, stay, run_right, run_left):
        self.stay = stay
        self.run_right = run_right
        self.run_left = run_left


class PlayerSkin(Skin):
    def __init__(self, stay, run_right, run_left, jump_mid, jump_right, jump_left):
        super().__init__(stay, run_right, run_left)
        self.jump_mid = jump_mid
        self.jump_right = jump_right
        self.jump_left = jump_left


# init Skins
red_skin = PlayerSkin(red_stay_img_list, red_run_right_img_list, red_run_left_img_list, red_jump_mid_img_list,
                      red_jump_right_img_list, red_jump_left_img_list)
std_skin = PlayerSkin(stay_img_list, run_right_img_list, run_left_img_list, jump_mid_img_list,
                      jump_right_img_list, jump_left_img_list)
green_alien = Skin(green_enemy_right, green_enemy_right, green_enemy_left)
move_list_player = ["stay", "run_right", "run_left", "jump_mid", "jump_right", "jump_left"]
move_list_alien = ["run_right", "run_left"]


class Timer:
    def __init__(self):
        self.start = time.time()  # starter tick
        self.font = pygame.font.SysFont(None, 40)  # create Font

    def draw(self):
        """
            date:
                - 27.05.2020
            desc:
                - Timer wird im richtigen Format auf Display gezeichnet
            param:
                - nothing
            return:
                - nothing
        """
        end = time.time()
        hours, rem = divmod(end - self.start, 3600)
        minutes, seconds = divmod(rem, 60)
        # print("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))
        timer = self.font.render("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds), True, WHITE)
        gameDisplay.blit(timer, (0, 0))


class Jump:
    def __init__(self, is_jumping, next_y, jump_count, jump_size, cancle):
        self.is_jumping = is_jumping
        self.next_y = next_y
        self.jump_count = jump_count
        self.jump_size = jump_size
        self.cancle = cancle

    def jump_init(self):
        self.is_jumping = True
        self.cancle = False
        self.jump_count = self.jump_size

    def calc_new_y(self):
        self.next_y -= self.jump_count * abs(self.jump_count)
        if self.jump_count == -self.jump_size:
            self.is_jumping = False
        if self.cancle and self.jump_count > 0:
            self.jump_count = -self.jump_count
        else:
            self.jump_count -= 1
        return self.next_y


std_jump = Jump(False, 400, 0, 6, False)


class Jump2:
    def __init__(self):
        self.jump_height = BLOCKHEIGHT * 2 + 10  # ist die gesamte Sprunghöhe
        self.cancel = False  # gibt an ob der Spieler noch den Sprung ausführt, # wenn cancle = True ist entweder ein Hinderniss im Weg oder User drück nicht mehr die "Springtaste"
        self.size = 6  # nach jedem Aufruf von calc_new_y wird der Spieler um diese Anzahl von Pixeln hoch springen
        self.is_running = False  # wenn es auf True geht kann kein neuer Sprung angenommen werden # todo: wenn Speiler Bden erreicht wieder auf False setzen

    def jump_init(self, speed):
        self.is_running = True  # es kann kein neuer Sprung ausgeführt werden
        self.cancel = False  # Sprung ist noch nicht zuende
        self.jump_height = BLOCKHEIGHT * 2 + 10
        self.size = speed  # damit wird springen auch schneller wenn der Spieler mehr speed hat

    def calc_new_y(self, player):
        self.jump_height -= self.size  # Gesamte Sprunghöhe - Anz. die Player nach diesem Aufruf hoch springt
        if self.jump_height >= 0:
            for x in range(1, self.size + 1):  # es wird überprüft ob Kollision mit Blöcken stattfinden
                player.player_rect.y -= 1
                # Koordinaten Werte von links oben Spieler
                x_pos_player = player.player_rect.x
                y_pos_player = player.player_rect.y
                collide1 = player.collide(x_pos_player, y_pos_player)
                if collide1 == True:
                    player.player_rect.y += 1
                    self.cancel = True  # Sprung wird beendet, da Spieler am links am Kopf auf Block trifft
                else:
                    # Koordinaten Werte von rechts oben Spieler
                    x_pos_player = player.player_rect.x + PLAYERWIDTH
                    y_pos_player = player.player_rect.y
                    collide2 = player.collide(x_pos_player, y_pos_player)
                    if collide2 == True:
                        player.player_rect.y += 1
                        self.cancel = True  # Sprung wird beendet, da Spieler am rechts am Kopf auf Block trifft

        else:
            self.cancel = True  # Sprung wird beendet, da Spieler die max. Sprunghöhe erreicht


class Species:
    def __init__(self, player_rect, current_move, move_list, skin, state, speed, health):
        self.player_rect = player_rect
        self.current_move = current_move
        self.skin = skin
        self.state = state
        self.speed = speed
        self.health = health
        self.move_list = move_list


class Player2(Species):
    def __init__(self, player_rect, current_move, move_list, jump, skin, state, speed, health, level_num):
        super().__init__(player_rect, current_move, move_list, skin, state, speed, health)
        self.jump = jump
        self.level_array = get_level_array(level_num)

    def move(self):
        """
            date:
                - 27.05.2020
            desc:
                - in Abhängigkeit von der Bewegung die Player (aufgrund von Tastedruck) macht und seinem speed wird sein neue y und seine absolute Postion x ermittel
            param:
                - nothing
            return:
                - nothing
            todo:
                - Collisionen mit Blöcken und Gegenern aus Level erkennen -> Bewegung wird gestoppt
                - todo Schleifen zählung nicht +1 sondern effizienter
        """

        # Bewegung nach rechts
        if self.current_move == 1:
            for i in range(1, self.speed + 1):
                self.player_rect.x += 1
                # Koordinaten Werte von rechts oben Spieler
                x_pos_player = self.player_rect.x + PLAYERWIDTH
                y_pos_player = self.player_rect.y
                collide1 = self.collide(x_pos_player, y_pos_player)
                if collide1:
                    self.player_rect.x -= 1
                    break
                else:
                    # Koordinaten Werte von rechts unten Spieler
                    x_pos_player = self.player_rect.x + PLAYERWIDTH
                    y_pos_player = self.player_rect.y + PLAYERHEIGHT
                    collide2 = self.collide(x_pos_player, y_pos_player)
                    if collide2:
                        self.player_rect.x -= 1
                        break


        # Bewegung nach links
        elif self.current_move == 2:
            for i in range(1, self.speed + 1):
                self.player_rect.x -= 1
                # Koordinaten Werte von links oben Spieler
                x_pos_player = self.player_rect.x
                y_pos_player = self.player_rect.y
                if self.player_rect.x <= 0:  # Linkes Bildschirm Ende
                    self.player_rect.x = 0
                collide1 = self.collide(x_pos_player, y_pos_player)
                if collide1:
                    self.player_rect.x += 1
                    break
                else:
                    # Koordinaten Werte von links unten Spieler
                    x_pos_player = self.player_rect.x
                    y_pos_player = self.player_rect.y + PLAYERHEIGHT
                    collide2 = self.collide(x_pos_player, y_pos_player)
                    if collide2:
                        self.player_rect.x += 1
                        break


        # Gegner springt nach oben
        if self.jump.is_running == True and self.jump.cancel == False:  # Sprung wird noch ausgeführt
            self.jump.calc_new_y(self)

        # Gravitation, wenn kein Sprung ausgeführt wird, überprüfen ob Untergrund unter dem Player
        # Koordinaten Werte von links unten Spieler                                        # Koordinaten Werte von rechts unten Spieler
        elif self.collide(self.player_rect.x, self.player_rect.y + PLAYERHEIGHT) == False and self.collide(self.player_rect.x, self.player_rect.y + PLAYERHEIGHT) == False: # keine Kollision mit Untergrund
            for i in range(1, self.jump.size + 1):  # zähle y solange hoch bis Boden erreicht ist
                self.player_rect.y += 1
                if self.player_rect.y + PLAYERHEIGHT == DISPLAYHEIGHT:  # Spieler ist mit Beinen am Boden von Wasser angekommen
                    self.health -= 2  # Leben wird abgezogen
                    break
                # Koordinaten Werte von links unten Spieler
                collide1 = self.collide(self.player_rect.x, self.player_rect.y + PLAYERHEIGHT)
                if collide1:
                    self.jump.is_running = False # es kann neuer Sprung beginnen
                    self.player_rect.y -= 1
                    break
                else: # Koordinaten Werte von rechts unten Spieler
                    collide2 = self.collide(self.player_rect.x, self.player_rect.y + PLAYERHEIGHT)
                    if collide2:
                        self.jump.is_running = False  # es kann neuer Sprung beginnen
                        self.player_rect.y -= 1
                        break

    def collide(self, x_pos_player, y_pos_player):
        """
             date:
                 - 27.05.2020
             desc:
                 - es wird überprüft ob Player und Gegner sich berühren
                 - wenn berührung stattfindet: Player von oben auf Gegner -> Gegner health - 1
                 - Gegner von der Seite auf Player -> Player health - 1
             param:
                 - die relevante x,y Position von dem Player
             return:
                 - true wenn Gegner gehittet wird
             todo:
                 - ganze Funktion -> Gegner oder Spiler Leben abziehen, Mehtode in Level sinnvoll
                 - Bei end block ins Menü zurück oder Animation abspielen und Name eintragen wenn Highscore unter den besten 10
                 - Funktion bei Block 40 (Wasser)
                 - eventuell Reihenfolge ändern(effizienter, statt else alle nicht passierbaren Blöcke in Array und an Anfang
        """

        player_list = (x_pos_player // BLOCKWIDTH)  # in welcher Liste sich relevante Player x-Position befindet
        player_element = y_pos_player // BLOCKHEIGHT  # in welchem Element sich relevante Player y-Position befindet
        block_value = self.level_array[player_list][player_element]
        # print(pos_player)
        # print(player_list, player_element, block_value)

        # je nach Blockart gibt es eine/keine Kollision
        if block_value in DECORATION_BLOCK:
            collision = False
        elif block_value in POWERUP_BLOCK:
            self.collect_drink(block_value)
            self.level_array[player_list][player_element] = 74  # getränk wird gelöscht
            collision = False
        elif block_value in RARE_BLOCK:
            print("found rare item")
            collision = False
        elif block_value in ENEMY_SPAWN:
            print("new enemy")
            collision = False
        elif block_value == END_BLOCK:
            print("Ende")
            collision = True
        else:
            collision = True
        return collision

    def handle_keys(self, running):
        for event in pygame.event.get():
            """
            if event.type == pg.Quit:
                running = False
                pg.QUIT()
            """
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # for exit
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.current_move = 1
                        self.state = 0
                    if event.key == pygame.K_LEFT:
                        self.current_move = 2
                        self.state = 0
                    if event.key == pygame.K_UP:
                        if self.jump.is_running == False:  # wenn gerade noch kein Sprung ausgeführt wird
                            self.state = 0
                            self.jump.jump_init(self.speed // 2)  # is_running = True , cancel = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.current_move = 0
                    self.state = 0
                if event.key == pygame.K_UP:
                    self.jump.cancel = True  # Sprung wird gecancelt, neuer Sprung kann erst anfangen wenn jump.is_running auf False gesetzt wird
                    self.state = 0
        return running

    def dead(self):
        """
            date:
                - 27.05.2020
            desc:
                - wenn Spieler keine Leben mehr hat, ist Spiel zu Ende
            param:
                - anzahl Leben die Spieler verliert
            return:
                - running
        """

        if self.health <= 0:
            font = pygame.font.SysFont(None, 100)  # create Font
            gameDisplay.fill(BLACK)
            ende = font.render(("You Lost"), True, WHITE)
            gameDisplay.blit(ende, (300, 300))
            pygame.display.update()  # Display updaten
            time.sleep(3)
            running = False
        else:
            running = True
        return running

    def draw_self(self):
        """
            date:
                - 27.05.2020
            desc:
                - in Abhängigkeit von der Bewegung die Player (aufgrund von Tastedruck) macht wird sein neues Bild an der richtigen Position gezeichnet
            param:
                - nothing
            return:
                - nothing
        """
        max_x = DISPLAYWIDTH / 2 - BLOCKWIDTH  # relative Position von Player, damit Player in der Mitte des Display erscheint
        if self.player_rect.x < max_x:  # wenn die absolute Position von Player noch kleiner wie die relative ist
            max_x = self.player_rect.x  # Player ist noch nicht bis zur Mitte gelaufen; Anfang vom Level

        """
        def __init__(self, is_jumping, next_y, jump_count, jump_size, cancle):
             std_jump = Jump(False,       0,          0,         6, False)

                    if event.key == pygame.K_UP:
                        if self.jump.is_jumping = False:
                            self.state = 0
                            self.jump.jump_init()

                if event.key == pygame.K_UP:
                    if self.jump.is_jumping = True:
                        if self.jump.cancle = False:
                            self.jump.cancle = True
                            self.state = 0


    def jump_init(self):
        self.is_jumping = True
        self.cancle = False
        self.jump_count = self.jump_size

    def calc_new_y(self):
        self.next_y -= self.jump_count * abs(self.jump_count)
        if self.jump_count == -self.jump_size:
            self.is_jumping = False
        if self.cancle and self.jump_count > 0:
            self.jump_count = -self.jump_count
        else:
            self.jump_count -= 1
        return self.next_y


        """

        gameDisplay.blit(getattr(self.skin, self.move_list[self.current_move])[int(self.state)],
                         (max_x, self.player_rect.y))
        if self.state < (len(getattr(self.skin, self.move_list[self.current_move])) - 1):
            self.state += 1  # damit die nächste Animation geladen wird
        else:
            self.state = 0  # wenn letztes element von Array erreicht -> Bewegung von Vorne anfangen
        """
        else:  # es wird gesprungen
            #self.player_rect.y = self.jump.calc_new_y(self)  # todo: in move methode
            if self.jump2.jump_count >= 0:
                gameDisplay.blit(getattr(self.skin, self.move_list[self.current_move + 3])[1],
                                 (max_x, self.player_rect.y))
            else:
                gameDisplay.blit(getattr(self.skin, self.move_list[self.current_move + 3])[2],
                                 (max_x, self.player_rect.y))
        """

    def collect_drink(self, num):
        """
             date:
                 - 27.05.2020
             desc:
                 - Funktion wird ausgeführt wenn Spieler ein Getränk einsammelt
                 - es werden je nach Art des Getränks die Spielereigenschaften geändert
             param:
                 - num: ID of collected drink
             return:
                 - nothing
             todo:
                 - Spieler Layout verändern
                 - Eigneschaften von Spieler beeinflussen
                 - Timer ablaufen lassen ??
        """
        if num == 56:
            print("Grün")
        elif num == 57:
            print("rosa")
        elif num == 63:
            print("braun")
        elif num == 64:
            print("gelb")


class Player(Species):
    def __init__(self, player_rect, current_move, move_list, jump, skin, state, speed, health, level_num):
        super().__init__(player_rect, current_move, move_list, skin, state, speed, health)
        self.jump = jump
        self.level_array = get_level_array(level_num)

    def move(self):
        """
            date:
                - 27.05.2020
            desc:
                - in Abhängigkeit von der Bewegung die Player (aufgrund von Tastedruck) macht und seinem speed wird sein neue y und seine absolute Postion x ermittel
            param:
                - nothing
            return:
                - nothing
            todo:
                - Collisionen mit Blöcken und Gegenern aus Level erkennen -> Bewegung wird gestoppt
                - todo Schleifen zählung nicht +1 sondern effizienter
        """
        if self.current_move == 1:
            for i in range(1, self.speed + 1):
                self.player_rect.x += 1
                collide = self.collide()
                if collide:
                    self.player_rect.x -= 1
                    break
        elif self.current_move == 2:
            for i in range(1, self.speed + 1):
                self.player_rect.x -= 1
                if self.player_rect.x <= 0:  # Linkes Bildschirm Ende
                    self.player_rect.x = 0
                collide = self.collide()
                if collide:
                    self.player_rect.x += 1
                    break

    def draw_self(self):
        """
            date:
                - 27.05.2020
            desc:
                - in Abhängigkeit von der Bewegung die Player (aufgrund von Tastedruck) macht wird sein neues Bild an der richtigen Position gezeichnet
            param:
                - nothing
            return:
                - nothing
        """
        max_x = DISPLAYWIDTH / 2 - BLOCKWIDTH  # relative Position von Player, damit Player in der Mitte des Display erscheint
        if self.player_rect.x < max_x:  # wenn die absolute Position von Player noch kleiner wie die relative ist
            max_x = self.player_rect.x  # Player ist noch nicht bis zur Mitte gelaufen; Anfang vom Level
        if not self.jump.is_jumping:
            gameDisplay.blit(getattr(self.skin, self.move_list[self.current_move])[int(self.state)],
                             (max_x, self.player_rect.y))
            if self.state < (len(getattr(self.skin, self.move_list[self.current_move])) - 1):
                self.state += 1  # damit die nächste Animation geladen wird
            else:
                self.state = 0  # wenn letztes element von Array erreicht -> Bewegung von Vorne anfangen
        else:  # es wird gesprungen
            self.player_rect.y = self.jump.calc_new_y(self)  # todo: in move methode
            if self.jump.jump_count >= 0:
                gameDisplay.blit(getattr(self.skin, self.move_list[self.current_move + 3])[1],
                                 (max_x, self.player_rect.y))
            else:
                gameDisplay.blit(getattr(self.skin, self.move_list[self.current_move + 3])[2],
                                 (max_x, self.player_rect.y))

    def collide(self):
        """
             date:
                 - 27.05.2020
             desc:
                 - es wird überprüft ob Player und Gegner sich berühren
                 - wenn berührung stattfindet: Player von oben auf Gegner -> Gegner health - 1
                 - Gegner von der Seite auf Player -> Player health - 1
             param:
                 - nothing
             return:
                 - true wenn Gegner gehittet wird
             todo:
                 - ganze Funktion -> Gegner oder Spiler Leben abziehen, Mehtode in Level sinnvoll
                 - Bei end block ins Menü zurück oder Animation abspielen und Name eintragen wenn Highscore unter den besten 10
                 - Funktion bei Block 40 (Wasser)
                 - eventuell Reihenfolge ändern(effizienter, statt else alle nicht passierbaren Blöcke in Array und an Anfang
        """
        if self.current_move == 1:
            pos_player = self.player_rect.x + PLAYERWIDTH

        else:  # self.current_move == 2:
            pos_player = self.player_rect.x

        player_list = pos_player // BLOCKWIDTH  # in welcher Liste sich Player befindet
        player_element = self.player_rect.y // BLOCKHEIGHT

        block_value = self.level_array[player_list][player_element]
        # print(pos_player)
        # print(player_list, player_element, block_value)

        if block_value in DECORATION_BLOCK:
            return False
        elif block_value in POWERUP_BLOCK:
            self.collect_drink(block_value)
            self.level_array[player_list][player_element] = 74  # getränk wird gelöscht
            return False
        elif block_value in RARE_BLOCK:
            print("found rare item")
        elif block_value in ENEMY_SPAWN:
            print("new enemy")
            return False
        elif block_value == END_BLOCK:
            print("Ende")
            return True
        else:
            return True

    def collect_drink(self, num):
        """
             date:
                 - 27.05.2020
             desc:
                 - Funktion wird ausgeführt wenn Spieler ein Getränk einsammelt
                 - es werden je nach Art des Getränks die Spielereigenschaften geändert
             param:
                 - num: ID of collected drink
             return:
                 - nothing
             todo:
                 - Spieler Layout verändern
                 - Eigneschaften von Spieler beeinflussen
                 - Timer ablaufen lassen ??
        """
        if num == 56:
            print("Grün")
        elif num == 57:
            print("rosa")
        elif num == 63:
            print("braun")
        elif num == 64:
            print("gelb")

    def handle_keys(self, running):
        for event in pygame.event.get():
            """
            if event.type == pg.Quit:
                running = False
                pg.QUIT()
            """
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # for exit
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.current_move = 1
                        self.state = 0
                    if event.key == pygame.K_LEFT:
                        self.current_move = 2
                        self.state = 0
                    if event.key == pygame.K_UP:
                        if not self.jump.is_jumping:
                            self.state = 0
                            self.jump.jump_init()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.current_move = 0
                    self.state = 0
                if event.key == pygame.K_UP:
                    if self.jump.is_jumping:
                        if not self.jump.cancle:
                            self.jump.cancle = True
                            self.state = 0
        return running


# create a Player
player1 = Player(pygame.Rect(400, 400, 50, 75), 0, move_list_player, std_jump,
                 std_skin, 0, 7, 3, 1)


# class enemy
class Enemy(Species):
    def __init__(self, player_rect, current_move, move_list, skin, state, alive, range, sporn_x, speed, health):
        super().__init__(player_rect, current_move, move_list, skin, state, speed, health)
        self.alive = alive
        self.range = range
        self.sporn_x = sporn_x

    def draw_self(self, player):
        if self.alive:
            gameDisplay.blit(getattr(self.skin, self.move_list[self.current_move])[self.state],
                             (self.player_rect.x, self.player_rect.y))
            self.collide_detection(player)
            self.calc_next_x_position(player)
            if self.state < (len(self.skin.run_right) - 1):
                self.state += 1
            else:
                self.state = 0

    def calc_next_x_position(self, player):
        if self.current_move == 0:
            if self.player_rect.x < self.sporn_x + self.range:
                if player.current_move == 1:
                    self.player_rect.x += (self.speed - player.speed)
                    self.sporn_x -= player.speed
                elif player.current_move == 2:
                    self.player_rect.x += (self.speed + player.speed)
                    self.sporn_x += player.speed
                else:
                    self.player_rect.x += self.speed
            else:
                self.current_move = 1
        if self.current_move == 1:
            if self.player_rect.x > self.sporn_x - self.range:
                if player.current_move == 1:
                    self.player_rect.x -= (self.speed + player.speed)
                    self.sporn_x -= player.speed
                elif player.current_move == 2:
                    self.player_rect.x -= (self.speed - player.speed)
                    self.sporn_x += player.speed
                else:
                    self.player_rect.x -= self.speed
            else:
                self.current_move = 0

    def collide_detection(self, player):
        if self.player_rect.x - PLAYERWIDTH <= player.player_rect.x <= self.player_rect.x + PLAYERWIDTH:
            if self.player_rect.y - PLAYERHEIGHT + 5 <= player.player_rect.y <= self.player_rect.y + PLAYERHEIGHT + 5:
                if player.player_rect.y + PLAYERHEIGHT - 15 <= self.player_rect.y:
                    self.alive = False
                    self.die_animation(player)
                else:
                    print("player lost life")

    def die_animation(self, player):
        for i in range(6):
            for j in range(len(background_list)):
                gameDisplay.blit(background_list[j].image, (background_list[j].x, background_list[j].y))
            gameDisplay.blit(getattr(player.skin, player.move_list[player.current_move])[player.state],
                             (player.player_rect.x, player.player_rect.y))
            if i % 2 == 0:
                gameDisplay.blit(
                    pygame.transform.scale(getattr(self.skin, self.move_list[self.current_move])[3],
                                           (PLAYERWIDTH, (PLAYERHEIGHT - 10))),
                    (self.player_rect.x, self.player_rect.y + 10))
            pygame.display.update()
            pygame.time.wait(60)


green_enemy1 = Enemy(pygame.Rect(700, 400, 50, 75), 0, move_list_alien, green_alien, 0, True, 30, 700, 1, 1)
sporn_x = 990


class Background:
    def __init__(self, x, y, speed, image, position):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.position = position

    def draw_self(self, player):
        gameDisplay.blit(self.image, (self.x, self.y))
        if player.current_move == 1:
            if self.x > -sporn_x:
                self.x -= self.speed
            else:
                self.x = sporn_x
        if player.current_move == 2:
            if self.x < sporn_x:
                self.x += self.speed
            else:
                self.x = -sporn_x


class Level:
    def __init__(self, num):
        self.level_array = get_level_array(num)
        self.draw_level(0, self.level_array)

    def draw_level(self, player_pos, modified_level):
        """
        	date:
        	    - 27.05.2020
        	desc:
        	    - das Level (2-Dimensionales Array) wird gezeichnet in Abhängigkeit von absoluter x-Position Player
        	    - es wird berechnet welcher Bereich des Arrays auf dem Display gezeichnet werden muss
        	    - je nach Inhalt im Array werden unterschiedliche Blöcke gezeichnet

        	param:
                - player.player_rect.x
                - modified_level: wird von Spieler übergeben da dort bei Kollision mit zum Beispiel tränken das Level modifiziert wird
            return:
                - nothing
        """
        self.level_array = modified_level
        anz_listen = DISPLAYWIDTH // BLOCKWIDTH  # Anzahl Blöcke/Listen die auf Diyplay möglich sind
        max_x_player = DISPLAYWIDTH / 2  # 500
        if player_pos + PLAYERWIDTH > max_x_player:  # player bewegt sich nicht mehr weiter sondern Level abhängig von absoluten x-Wert von Player
            rest = player_pos % BLOCKWIDTH  # rest = anzahl Pixel die Player über player_array ist
            player_list = player_pos // BLOCKWIDTH  # in welcher Liste sich Player befindet
            space = anz_listen // 2 - 1  # Anzahl Listen die vor und nach player_list angezigt werden auf Display
            left_list = player_list - space  # Liste die ganz links im Display angezeigt wird
            # print(rest, player_list, space, left_list)
        else:  # player ist noch nicht in der Mitte von Spielfeld -> Feld verschiebt sich noch nicht bei Bewegung von Spieler
            left_list = 0
            rest = 0
            player_list = player_pos // BLOCKWIDTH
        i = 0
        # Blöcke werden auf Display gesetzt mit Hilfe begrenzter for-loop
        for x in range(left_list, left_list + anz_listen + 1):
            for y in range(0, DISPLAYHEIGHT // BLOCKHEIGHT):  # DISPLAYHEIGHT//BLOCKHEIGHT = Anzahl Blöcke in der Höhe
                tile_height = 50
                tile_width = 50
                tilesheet_columns = 7
                value = self.level_array[x][y]  # value = id von richtigem Block
                if value == 74:
                    continue
                source_x = (value % tilesheet_columns) * tile_width
                source_y = (value // tilesheet_columns) * tile_height
                gameDisplay.blit(tileset, (i * BLOCKWIDTH - rest, y * BLOCKHEIGHT), (source_x, source_y, BLOCKWIDTH,
                                                                                     BLOCKHEIGHT))  # Block wird auf Display gezeichnet, i um an richtiger x-Stelle auf Display zu zeichnen
            i += 1


# create backgrounds
background_4 = Background(0, 0, 0, background_img[4], 0)
background_32 = Background(sporn_x, 0, 1, background_img[3], 0)
background_31 = Background(0, 0, 1, background_img[3], 0)
background_22 = Background(sporn_x, 0, 2, background_img[2], 0)
background_21 = Background(0, 0, 2, background_img[2], 0)
background_12 = Background(sporn_x, 0, 3, background_img[1], 0)
background_11 = Background(0, 0, 3, background_img[1], 0)
background_02 = Background(sporn_x, 0, 7, background_img[0], 0)
background_01 = Background(0, 0, 7, background_img[0], 0)

background_list = [background_4, background_32, background_31, background_22, background_21, background_12,
                   background_11, background_02, background_01]


# printen
def text_object(text="", font="", color="RED"):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text="", size=50, color="RED"):
    largeText = pygame.font.Font("freesansbold.ttf", size)
    TextSurf, TextRect = text_object(text, largeText, color)
    TextRect.center = ((DISPLAYWIDTH / 2), (DISPLAYHEIGHT / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def static_display(text="", size=10, color="BLACK", position=((DISPLAYWIDTH / 2), (DISPLAYHEIGHT / 2))):
    largeText = pygame.font.Font("freesansbold.ttf", size)
    TextSurf, TextRect = text_object(text, largeText, color)
    TextRect.center = position
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


# init display
gameDisplay = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT), DISPLAYFLAG, DISPLAYCOLBIT)
gameDisplay.fill(WHITE)
pygame.display.set_caption("MarioPy")

clock = pygame.time.Clock()


def draw_menu_background(text=""):
    gameDisplay.blit(menu_background, (0, 38))
    static_display(text, 20, WHITE, (100, 100))


def draw_options_background():
    gameDisplay.blit(options_menu_background, (796, 35))
    static_display("Music", 20, WHITE, (840, 70))
    static_display("Sound effects", 18, WHITE, (870, 110))


def draw_level_place_holder():
    for i in range(int(level_count / 2)):
        for j in range(int(level_count / 3)):
            x = i % 3 * 290 + 80
            y = j * 250 + 100
            gameDisplay.blit(level_background, (x, y))
            gameDisplay.blit(level_place_holder, (x - 10, y - 10))
            if (j * 3 + i) > 0:
                static_display("comming soon...", 20, GRAY, (x + 100, y + 90))


def draw_level_nums():
    for i in range(int(level_count / 2)):
        for j in range(int(level_count / 3)):
            x = i % 3 * 290 + 80
            y = j * 250 + 100
            static_display(str(j * 3 + i + 1), 40, WHITE, (x + 40, y + 40))


def draw_level_background(player):
    for i in range(len(background_list)):
        background_list[i].draw_self(player)


def check_buttons():
    for i in range(len(menu_button_list)):
        if menu_button_list[i].button_rect.collidepoint(pygame.mouse.get_pos()):
            menu_button_list[i].button_color = button_image_list[1]
        else:
            menu_button_list[i].button_color = button_image_list[0]

        menu_button_list[i].draw_self()

    if options_button.button_rect.collidepoint(pygame.mouse.get_pos()):
        options_button.button_color = options_button_list[1]
    else:
        options_button.button_color = options_button_list[0]
    options_button.draw_self()


def check_check_boxes():
    for i in range(len(check_box_list)):
        if check_box_list[i].button_rect.collidepoint(pygame.mouse.get_pos()):
            check_box_list[i].button_color = cb_img_list[1]
        else:
            check_box_list[i].button_color = cb_img_list[0]

        check_box_list[i].draw_self()


def check_single_button(button, image_list):
    if button.button_rect.collidepoint(pygame.mouse.get_pos()):
        button.button_color = image_list[1]
    else:
        button.button_color = image_list[0]
    button.draw_self()


def check_trans_button(button, image_list):
    color = 0
    if button.button_rect.collidepoint(pygame.mouse.get_pos()):
        button.button_color = image_list[1]
        color = 1
        if button.is_clicked == False and button.is_painted == 2:
            gameDisplay.blit(button.image_below, (button.button_rect.x, button.button_rect.y))
            draw_level_nums()

    else:
        button.button_color = image_list[0]
        if color != button.is_painted:
            gameDisplay.blit(button.image_below, (button.button_rect.x, button.button_rect.y))
            draw_level_nums()
    if button.is_painted != color:
        button.draw_self()
        if button.is_clicked == False:
            button.is_painted = color


def check_events(game_state, player=player1):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_state = 100
            elif event.key == pygame.K_g:
                game_state = 4
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 1 is the left mouse button, 2 is middle, 3 is right.
            if event.button == 1:
                # check buttons
                for i in range(len(menu_button_list)):
                    if menu_button_list[i].button_rect.collidepoint(event.pos):
                        menu_button_list[i].is_clicked = True
                if options_button.button_rect.collidepoint(event.pos):
                    options_button.is_clicked = True
                for i in range(len(check_box_list)):
                    if check_box_list[i].button_rect.collidepoint(event.pos):
                        if check_box_list[i].is_clicked:
                            check_box_list[i].is_clicked = False
                            draw_options_background()
                        else:
                            check_box_list[i].is_clicked = True
                if play_button.button_rect.collidepoint(event.pos):
                    play_button.is_clicked = True
                    play_button.is_painted = 2
        elif event.type == pygame.MOUSEBUTTONUP:
            # 1 is the left mouse button, 2 is middle, 3 is right.
            if event.button == 1:
                # check buttons
                for i in range(len(menu_button_list)):
                    if menu_button_list[i].is_clicked:
                        menu_button_list[i].is_clicked = False
                        game_state = menu_button_list[i].action(game_state)
                if options_button.is_clicked:
                    options_button.is_clicked = False
                    game_state = options_button.action(game_state)
                if play_button.is_clicked:
                    play_button.is_clicked = False
                    check_trans_button(play_button, play_button_img_list)
                    game_state = 4
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.current_move = 1
                player.state = 0
            if event.key == pygame.K_LEFT:
                player.current_move = 2
                player.state = 0
            if event.key == pygame.K_UP:
                if not player.jump.is_jumping:
                    player.state = 0
                    player.jump.jump_init()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.current_move = 0
                player1.state = 0
            if event.key == pygame.K_UP:
                if player.jump.is_jumping:
                    if not player.jump.cancle:
                        player.jump.cancle = True
                        player.state = 0

    return game_state


def options_menu_loop(game_state, former_game_state):
    draw_options_background()

    while game_state == 3:
        check_buttons()
        check_check_boxes()
        game_state = check_events(game_state)
        pygame.display.update()
        clock.tick(30)
    return former_game_state


def menu_home_loop(game_state):
    gameDisplay.blit(menu_navbar, (0, 0))
    draw_menu_background("Home")

    while game_state == 0:
        draw_menu_background("Home")
        check_buttons()
        game_state = check_events(game_state, player1)
        pygame.display.update()
        clock.tick(20)
    return game_state


def menu_level_loop(game_state):
    gameDisplay.blit(menu_navbar, (0, 0))
    draw_menu_background()
    draw_level_place_holder()
    draw_level_nums()

    while game_state == 1:
        check_buttons()
        # todo: game_state 4 zurückgeben und level Nummer wenn level gestartet werden soll
        check_trans_button(play_button, play_button_img_list)
        game_state = check_events(game_state)
        pygame.display.update()
        clock.tick(30)
    return game_state


def menu_score_loop(game_state):
    gameDisplay.blit(menu_navbar, (0, 0))
    draw_menu_background()

    while game_state == 2:
        draw_level_background(player1)
        green_enemy1.draw_self(player1)
        player1.draw_self()
        check_buttons()
        game_state = check_events(game_state)
        pygame.display.update()
        clock.tick(10)
    return game_state


def main():
    game_state = 0
    former_game_state = 0
    while game_state != 100:
        if game_state == 0:
            game_state = menu_home_loop(0)
            former_game_state = 0
        elif game_state == 1:
            game_state = menu_level_loop(1)
            former_game_state = 1
        elif game_state == 2:
            game_state = menu_score_loop(2)
            former_game_state = 2
        elif game_state == 3:
            game_state = options_menu_loop(3, former_game_state)
        elif game_state == 4:
            game_state = game_loop(1)


def check_create(enemy_status, player_pos):
    """
        date:
            - 27.05.2020
        desc:
            - es wird überprüft ob aufgrund von der Player Position ein Gegner erstellt werden muss
        param:
            - player_pos: Distanz die Spieler zurückgelgt hat
        return:
            - enemy
        todo:
            - noch mehr gegner erstellen abh. von player_pos
    """
    if player_pos >= 500 and enemy_status[0] == 0:
        enemy_status[0] = 1
    elif player_pos >= 1000 and enemy_status[1] == 0:
        enemy_status[1] = 1

    return enemy_status


def game_loop(level_num):
    """
     	date:
     	    - 27.05.2020
     	desc:
     	    - hier findet Spielablauf statt (es werde Eingaben entgegengenommen)
     	    - auf Grund von Events(Tasteneingaben) Gegner und Level verändern
     	    - Objekte erstellen: Player, (jump), Level, Gegner
     	param:
             - level_num: Level Nummer, Auswahl geschieht im Level-Menü
         return:
             - game_state: um in menü zurück zu springen
     	todo:
     	    - zurückspringen ins Menü
     	    - Button um Spiel abzubrechen
     	    - Gegener einbinden an den Stellen wo Coins sind (Gegenerlogik)
     	    - Gegener sichtbart erstellen, abhägig von absoluter Position von Player
     	    - Gegner move methode in dauerschleife er bewegt sich auch wenn kein event; ähnlich zu idle zustand
     	    - Highscore abspeichern, diesen im Menü anzeigen können (-> siehe helpful code, zum abspeichern in extra Datei)
     	    - pygame.Quit() einbauen
    """
    running = True
    std_jump2 = Jump2()
    player = Player2(pygame.Rect(BLOCKWIDTH, 0, PLAYERWIDTH, PLAYERHEIGHT), 0,
                     move_list_player, std_jump2,
                     red_skin, 0, 20, 2, level_num)

    level = Level(level_num)
    enemy_status = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0 = nicht erstellt,  1 = erstellen, 2 = erstellt, 3 = tot,
    time = Timer()

    while running:
        running = player.handle_keys(running)
        gameDisplay.fill(BLUE)
        player.move()
        level.draw_level(player.player_rect.x, player.level_array)
        """
        # Gegner einbinden
        enemy_status = check_create(enemy_status, player.player_rect.x)
        for i in enemy_status:
            for j in range(0, 4):
                if i == 1:
                    if j == 0:
                        enemy_1 = Enemy(pygame.Rect(700, 400, 50, 75), 0, move_list_alien, green_alien, 0, True, 30,
                                        700, 1, 1)
                        enemy_status[j] = 2
                    elif j == 1:
                        enemy_2 = Enemy(pygame.Rect(700, 400, 50, 75), 0, move_list_alien, green_alien, 0, True,
                                        30, 700, 1, 1)
                        enemy_status[j] = 2
                if i == 2:
                    if j == 0:
                        enemy_1.draw_self(player)
                    elif j == 1:
                        enemy_2.draw_self(player)
        """
        player.draw_self()
        running = player.dead()
        time.draw()  # for Time
        pygame.display.update()  # Display updaten
        clock.tick(30)  # max 30 Herz
    return 0


main()
