import os
from enum import Enum

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
#                   - mit der Taste "g" wird Spiel derzeit gestartet

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

tileset = pygame.transform.scale(pygame.image.load("res/level/nature-paltformer-tileset-16x16.png"),
                                 (350, 550))
NORMAL_GROUND = DISPLAYHEIGHT - 2 * BLOCKHEIGHT  # normalground ist die kleinste Höhe auf der sich Spieler befindet #todo sollte unnötig werden, wenn player Gravitation hat und von oben auf Displayer föllt
# level_array ist Liste, in dieser sind: x*level_lenght Listen von der jede y Werte hat
PLAYERHEIGHT = 50
PLAYERWIDTH = 33

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


# Button class
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


class Species:
    def __init__(self, player_rect, current_move, move_list, skin, state, speed, health):
        self.player_rect = player_rect
        self.current_move = current_move
        self.skin = skin
        self.state = state
        self.speed = speed
        self.health = health
        self.move_list = move_list


# Class Player
class Player(Species):
    def __init__(self, player_rect, current_move, move_list, jump, skin, state, speed, health):
        super().__init__(player_rect, current_move, move_list, skin, state, speed, health)
        self.jump = jump

    def move(self, level_array):
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
        """
        if self.current_move == 1:
            for i in range(1, self.speed + 1):
                self.player_rect.x += 1
                ##collide = self.collide(level_array)
                ##if collide:
                #   break

        elif self.current_move == 2:
            self.player_rect.x -= self.speed
            if self.player_rect.x <= 0:
                self.player_rect.x = 0

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

        max_x = DISPLAYWIDTH / 2 - PLAYERWIDTH / 2  # relative Position von Player, damit Player in der Mitte des Display erscheint
        if self.player_rect.x < max_x:  # wenn die absolute Position von Player noch kleiner wie die relative ist
            max_x = self.player_rect.x  # Player ist noch nicht bis zur mitte gelaufen; Anfang vom Level

        if not self.jump.is_jumping:
            gameDisplay.blit(getattr(self.skin, self.move_list[self.current_move])[int(self.state)],
                             (max_x, self.player_rect.y))
            if self.state < (len(getattr(self.skin, self.move_list[self.current_move])) - 1):
                self.state += 1  # damit die nächste Animation geladen wird
            else:
                self.state = 0  # wenn letztes element von Array erreicht -> Bewegung von Vorne anfangen
        else:
            self.player_rect.y = self.jump.calc_new_y()
            if self.jump.jump_count >= 0:
                gameDisplay.blit(getattr(self.skin,self.move_list[self.current_move+3])[1], (max_x, self.player_rect.y))
            else:
                gameDisplay.blit(getattr(self.skin,self.move_list[self.current_move+3])[2], (max_x, self.player_rect.y))

    def collide(self, level_array):
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
        """
        # x_player = self.player_rect.x + PLAYERWIDTH
        # x_level = level_array[][self.player_rect.y//BLOCKHEIGHT]

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
                        print("rechts")
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
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if self.jump.is_jumping:
                        if not self.jump.cancle:
                            self.jump.cancle = True
                            self.state = 0
        return running


# create a Player
player1 = Player(pygame.Rect(400, 400, 50, 75), 0, move_list_player, std_jump,
                 std_skin, 0, 7, 3)


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
            gameDisplay.blit(getattr(player.skin,player.move_list[player.current_move])[player.state],
                             (player.player_rect.x, player.player_rect.y))
            if i % 2 == 0:
                gameDisplay.blit(
                    pygame.transform.scale(getattr(self.skin,self.move_list[self.current_move])[3], (PLAYERWIDTH, (PLAYERHEIGHT - 10))),
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
        self.draw_level(0)

    def draw_level(self, player_pos):
        """
        	date:
        	    - 27.05.2020
        	desc:
        	    - das Level (2-Dimensionales Array) wird gezeichnet in Abhängigkeit von absoluter x-Position Player
        	    - es wird berechnet welcher Bereich des Arrays auf dem Display gezeichnet werden muss
        	    - je nach Inhalt im Array werden unterschiedliche Blöcke gezeichnet
        	param:
                - player.player_rect.x
            return:
                - nothing
        """
        anz_listen = DISPLAYWIDTH // BLOCKWIDTH  # Anzahl Blöcke/Listen die auf Diyplay möglich sind
        max_x_player = DISPLAYWIDTH / 2 - PLAYERWIDTH / 2  # 475
        if player_pos > max_x_player:  # player bewegt sich nicht mehr weiter sondern Level abhängig von absoluten x-Wert von Player
            rest = player_pos % BLOCKWIDTH  # rest = anzahl Pixel die Player über player_array ist
            player_list = player_pos // BLOCKWIDTH  # in welcher Liste sich Player befindet
            space = anz_listen // 2 - 1  # Anzahl Listen die vor und nach player_list angezigt werden auf Display
            left_list = player_list - space  # Liste die ganz links im Display angezeigt wird

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
                # print(value)
                # print("x-pos Tilesheet", source_x)
                # print("y-pos Tilesheet", source_y)
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
        # gprint("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))
        timer = self.font.render("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds), True, WHITE)
        gameDisplay.blit(timer, (0, 0))


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
     	    - von Level-Menü game_loop aufrufen
     	    - zurückspringen ins Menü
     	    - Zeit einbinden im Bild und Button um Spiel abzubrechen
     	    - Gegener einbinden an den Stellen wo Coins sind (Gegenerlogik)
     	    - Gegener sichtbart erstellen, abhägig von absoluter Position von Player
     	    - Gegner move methode in dauerschleife er bewegt sich auch wenn kein event; ähnlich zu idle zustand
     	    - Highscore abspeichern, diesen im Menü anzeigen können (-> siehe helpful code, zum abspeichern in extra Datei)
     	    - pygame.Quit() einbauen
    """
    running = True
    std_jump = Jump(False, 400, 0, 6, False)
    player = Player(pygame.Rect(400, 400, 50, 75), 0, move_list_player, std_jump,
                    red_skin, 0, 7, 3)

    # green_enemy1 = Enemy(pygame.Rect(700, 400, 50, 75), 0, [green_enemy_right, green_enemy_left], 0, True, 2, 60, 700)
    # draw_level_background(player)
    # green_enemy1.draw_self()
    level = Level(level_num)
    time = Timer()

    while running:
        player.handle_keys(running)
        gameDisplay.fill(BLUE)
        player.move(level.level_array)
        level.draw_level(player.player_rect.x)
        player.draw_self()  # drt

        time.draw()  # for Time
        pygame.display.update()  # Display updaten
        clock.tick(30)  # max 30 Herz
    return 0


main()
