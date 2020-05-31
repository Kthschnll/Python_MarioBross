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

# level_array ist Liste, in dieser sind: x*level_lenght Listen von der jede y Werte hat
PLAYERHEIGHT = 50
PLAYERWIDTH = 40

# define_blocks
DECORATION_BLOCK = [22, 23, 29, 30, 36, 37, 51, 52, 53, 58, 59, 60, 65, 66, 67, 72, 73, 74]
POWERUP_BLOCK = [56, 57, 63, 64]
RARE_BLOCK = [45, 46, 47, 48]
END_BLOCK = 11  # Ende von Spiel
WATER_BLOCK = 40
ENEMY_SPAWN = [54, 55, 61, 62]
NOT_PASSABLE_BLOCK = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25, 26, 27, 31, 32, 33, 34,
                      41, 42, 43, 44]

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
logo_img = pygame.transform.scale(pygame.image.load(resources_path + "Jumpmaster24_red.png"), (600, 450))

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
green_run_right_img_list = []
green_run_left_img_list = []
green_stay_img_list = []
green_jump_right_img_list = []
green_jump_left_img_list = []

resources_path_player = "res/"
skin_list = ["std_skin/", "red_skin/", "green_skin/"]

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
    green_run_right_img_list.append(
        pygame.transform.scale(
            pygame.image.load(resources_path_player + skin_list[2] + "run_right" + str(i) + "_green.png"),
            (PLAYERWIDTH, PLAYERHEIGHT)))
    green_run_left_img_list.append(pygame.transform.flip(
        pygame.transform.scale(
            pygame.image.load(resources_path_player + skin_list[2] + "run_right" + str(i) + "_green.png"),
            (PLAYERWIDTH, PLAYERHEIGHT)), True, False))
# stay images
for i in range(12):
    stay_img_list.append(
        pygame.transform.scale(pygame.image.load(resources_path_player + skin_list[0] + "stand" + str(i) + ".png"),
                               (PLAYERWIDTH, PLAYERHEIGHT)))
    red_stay_img_list.append(
        pygame.transform.scale(pygame.image.load(resources_path_player + skin_list[1] + "stand" + str(i) + "_red.png"),
                               (PLAYERWIDTH, PLAYERHEIGHT)))
    green_stay_img_list.append(
        pygame.transform.scale(
            pygame.image.load(resources_path_player + skin_list[2] + "stand" + str(i) + "_green.png"),
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
    green_jump_left_img_list.append(
        pygame.transform.scale(
            pygame.image.load(resources_path_player + skin_list[2] + "jump_left" + str(i) + "_green.png"),
            (PLAYERWIDTH, PLAYERHEIGHT)))
    green_jump_right_img_list.append(pygame.transform.flip(
        pygame.transform.scale(
            pygame.image.load(resources_path_player + skin_list[2] + "jump_left" + str(i) + "_green.png"),
            (PLAYERWIDTH, PLAYERHEIGHT)), True, False))

jump_mid_img_list = [jump_right_img_list[0], jump_right_img_list[0], jump_right_img_list[3]]
red_jump_mid_img_list = [red_jump_right_img_list[0], red_jump_right_img_list[0], red_jump_right_img_list[3]]
green_jump_mid_img_list = [green_jump_right_img_list[0], green_jump_right_img_list[0], green_jump_right_img_list[3]]

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
#global music varables
music_on = True
sound_on = True
music_menu = False
music_list = ["res/sound/level_music.mp3","res/sound/menu_music.mp3"]
# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
# GREEN = (0, 255, 0) not used
BLUE = (0, 153, 220)
GRAY = (109, 107, 118)

# amount of level in level menu
level_count = 6

# init display
gameDisplay = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT), DISPLAYFLAG, DISPLAYCOLBIT)
gameDisplay.fill(WHITE)
pygame.display.set_caption("MarioPy")

clock = pygame.time.Clock()


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
check_box_music = Button("", pygame.Rect(950, 52, 30, 30), 4, True, cb_img_list[0])
check_box_sound = Button("", pygame.Rect(950, 92, 30, 30), 4, True, cb_img_list[0])
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
green_skin = PlayerSkin(green_stay_img_list, green_run_right_img_list, green_run_left_img_list, green_jump_mid_img_list,
                        green_jump_right_img_list, green_jump_left_img_list
                        )
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
                - timer is drawn in the correct format on the display
            param:
                - nothing
            return:
                - nothing
        """
        end = time.time()
        hours, rem = divmod(end - self.start, 3600)
        minutes, seconds = divmod(rem, 60)
        timer = self.font.render("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds), True, WHITE)
        gameDisplay.blit(timer, (0, 0))


class Jump:
    def __init__(self, jump_count):
        self.jump_count = jump_count
        self.jump_height = BLOCKHEIGHT * 2 + 10
        # max. jump height
        self.cancel = False
        # indicates if the player still performs the jump,
        # if cancle = True: either an obstacle in the way or user does not press the "Jump" button anymore
        self.size = 6
        # after each call of calc_new_y the player will jump up by this number of pixels
        self.is_running = False
        # when it is True new jump is not accepted

    def jump_init(self, speed):
        self.is_running = True
        self.cancel = False
        # jump is not at the end
        self.jump_height = BLOCKHEIGHT * 2 + 10
        self.size = speed
        # jump faster if the player has more speed

    def calc_new_y(self, player):
        """
            date:
                - 27.05.2020
            desc:
                - is calculating the new vertical position of the player if he jumps
            param:
                - player: to get vertical position of the player and to execute the method collision()
            return:
                - nothing
            todo:
                - Loop count not +1, to do it more more efficient
        """
        self.jump_height -= self.size
        # max. possible jump height - Number of pixels player is jumping
        if self.jump_height >= 0:
            # player can still jump
            for x in range(1, self.size + 1):
                player.player_rect.y -= 1
                if player.collide(player.player_rect.x, player.player_rect.y) or player.collide(
                        player.player_rect.x + PLAYERWIDTH, player.player_rect.y):
                    # coordinate values from top left player or top right have collision
                    player.player_rect.y += 1
                    # change players vertical position back
                    self.cancel = True
                    # Jump is finished because player is hitting block with his head
                    break
        else:
            self.cancel = True
            # Jump is finished, because player reaches the max. jump height


class Species:
    def __init__(self, player_rect, current_move, move_list, skin, state, speed, health):
        self.player_rect = player_rect
        self.current_move = current_move
        self.skin = skin
        self.state = state
        self.speed = speed
        self.health = health
        self.move_list = move_list


class Player(Species):
    def __init__(self, player_rect, current_move, move_list, jump, skin, state, speed, health, level_num):
        super().__init__(player_rect, current_move, move_list, skin, state, speed, health)
        self.jump = jump
        self.level_array = get_level_array(level_num)
        self.reached_end = False

    def move(self):
        """
            date:
                - 27.05.2020
            desc:
                - depending on the movement the player want to make (due to keystroke) his new horizontal and vertical Positon is calculated
                - calls the method collision() which checks if the new position is allowed
                - depending on the return value of the method collision() the player is moved or not
            param:
                - nothing
            return:
                - nothing
            todo:
                - Loop count not +1, to do it more more efficient
        """
        # Player want to move to the right
        if self.current_move == 1:
            for i in range(1, self.speed + 1):
                # count i up, maximal speed if there is no collision
                self.player_rect.x += 1
                if self.collide(self.player_rect.x + PLAYERWIDTH, self.player_rect.y + 1) or self.collide(
                        self.player_rect.x + PLAYERWIDTH, self.player_rect.y + PLAYERHEIGHT):
                    # coordinate values from top right player or bottom right have collision
                    # - 1 to make player fit through gaps and
                    self.player_rect.x -= 1
                    # change players horizontal position back
                    break

        # Player want to move to the left
        elif self.current_move == 2:
            for i in range(1, self.speed + 1):
                # count i up, maximal speed if there is no collision
                self.player_rect.x -= 1
                if self.player_rect.x <= 0:
                    # Left screen end is reached
                    self.player_rect.x = 0
                if self.collide(self.player_rect.x, self.player_rect.y) or self.collide(self.player_rect.x,
                                                                                        self.player_rect.y + PLAYERHEIGHT):
                    # coordinate values from top left player or bottom left have collision
                    self.player_rect.x += 1
                    # change players horizontal position back
                    break

        # Player want to jump up
        if self.jump.is_running and not self.jump.cancel:
            # jump is still executed
            self.jump.calc_new_y(self)

        # Gravity -> if no jump is performed, check if underground under the player
        elif self.collide(self.player_rect.x + PLAYERWIDTH // 2, self.player_rect.y + PLAYERHEIGHT + 1) == False:
            # Coordinate values from bottom middle player have no collision
            # -> no collision with level blocks when player moves one place down
            for i in range(1, self.jump.size + 1):
                # count y up, maximal jump.size if bottom is not reached
                # proof if bottom is reached after every change of players vertical position
                self.player_rect.y += 1
                if self.collide(self.player_rect.x, self.player_rect.y + PLAYERHEIGHT) or self.collide(
                        self.player_rect.x, self.player_rect.y + PLAYERHEIGHT):
                    # Coordinate values from bottom left player and coordinate values from bottom right player
                    # collision with background when player moves one place down
                    self.jump.is_running = False
                    # new jump can begin, because player reached the ground
                    self.player_rect.y -= 1
                    # change players vertical position back
                    break

        # Player is on the ground
        else:
            self.jump.is_running = False
            # new jump can begin, because player already reached the ground

    def collide(self, x_pos_player, y_pos_player):
        """
             date:
                 - 27.05.2020
             desc:
                 - detect collisions from player with blocks from level
             param:
                 - x_pos_player: relevant horizontal position of the player
                 - y_pos_player: relevant vertical position of the player
             return:
                 - true:  if there is a collisions with blocks
                 - false: no collision
             todo:
                 - Bei end block ins Menü zurück oder Animation abspielen und Name eintragen wenn Highscore unter den besten 10
                 - eventuell Reihenfolge ändern(effizienter, statt else alle nicht passierbaren Blöcke in Array und an Anfang
        """
        player_list = (x_pos_player // BLOCKWIDTH)
        # which list of the 2-dim array is relevant
        player_element = y_pos_player // BLOCKHEIGHT
        # which element of the list is relevant
        block_value = self.level_array[player_list][player_element]
        # get the value of the block

        # depending on block type there is a collision or not
        if block_value in NOT_PASSABLE_BLOCK:
            collision = True
        elif block_value in DECORATION_BLOCK:
            collision = False
        elif block_value in POWERUP_BLOCK:
            self.collect_drink(block_value)
            self.level_array[player_list][player_element] = 74
            # drink is deleted
            collision = False
        elif block_value in RARE_BLOCK:
            print("found rare item")
            collision = False
        elif block_value == WATER_BLOCK:
            print("water")
            self.health -= 3
            # Player die
            collision = True
        elif block_value in ENEMY_SPAWN:
            print("new enemy")
            collision = False
        elif block_value == END_BLOCK:
            self.reached_end = True
            # see method dead() for more
            collision = True
        return collision

    def handle_keys(self, running):
        """
             date:
                 - 27.05.2020
             desc:
                 - handle input from User while game is running
             param:
                 - running: game_loop status
             return:
                 - nothing
            todo:
                - pg.Quit
        """
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
                        if self.jump.is_running == False:
                            # if no jump is performed just yet
                            self.state = 0
                            self.jump.jump_init(self.speed // 2)
                            # set: is_running = True , cancel = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.current_move = 0
                    self.state = 0
                if event.key == pygame.K_UP:
                    self.jump.cancel = True
                    # Jump is canceled, new jump can only start when jump.is_running is set to False
                    self.state = 0
            return running

    def dead(self):
        """
            date:
                - 27.05.2020
            desc:
                - checks the number of lives the player has left
                - check if player has reached the end
            param:
                - nothing
            return:
                - running: running state of the function game_loop()
        """
        if self.health <= 0:
            # player has no lives left
            # create Font and put some output on the screen
            font = pygame.font.SysFont(None, 100)
            gameDisplay.fill(BLACK)
            end = font.render(("You Lost"), True, WHITE)
            gameDisplay.blit(end, (300, 300))
            pygame.display.update()
            play_music(5)
            time.sleep(2)
            running = False
        else:
            running = True
        if self.reached_end == True:
            # todo: katha

            running = False

        return running

    def draw_self(self):
        """
            date:
                - 27.05.2020
            desc:
                - depending on the movement the player makes he is drawn
            param:
                - nothing
            return:
                - nothing
            todo:
                - jump mit einbauen
                - comments
        """
        max_x = DISPLAYWIDTH / 2 - BLOCKWIDTH
        # relative position of player, so that player appears in the middle of the display
        if self.player_rect.x < max_x:
            # if the absolute position of player is even smaller than the relative one
            # Player hasn't run to the middle yet; beginning of the level
            max_x = self.player_rect.x
        if not self.jump.is_running:
            gameDisplay.blit(getattr(self.skin, self.move_list[self.current_move])[int(self.state)],
                             (max_x, self.player_rect.y))
            if self.state < (len(getattr(self.skin, self.move_list[self.current_move])) - 1):
                self.state += 1  # damit die nächste Animation geladen wird
            else:
                self.state = 0  # wenn letztes element von Array erreicht -> Bewegung von Vorne anfangen
        else:
            if self.jump.jump_count >= 0:
                gameDisplay.blit(getattr(self.skin, self.move_list[self.current_move + 3])[1],
                                 (max_x, self.player_rect.y))
            else:
                gameDisplay.blit(getattr(self.skin, self.move_list[self.current_move + 3])[2],
                                 (max_x, self.player_rect.y))

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
            # self = green_item.item_init(self)
        elif num == 57:
            print("rot")
            # self = red_item.item_init(self)
        elif num == 63:
            print("braun")
        elif num == 64:
            print("gelb")
            # self = red_item.item_init(self)


class Item:
    def __init__(self, color, collected, duration, skin, jump, speed, health, player_copy):
        self.color = color
        self.duration = duration  # in sec
        self.skin = skin
        self.jump = jump
        self.speed = speed
        self.player_copy = player_copy
        self.health = health
        self.collected = collected

    def item_init(self, player):
        if not self.collected:
            self.player_copy = player
            player.skin = self.skin
            player.jump = self.jump
            player.speed = self.speed
            player.health += self.health
            self.collected = True
            self.start_time()
        return player

    def start_time(self):
        time1 = Timer()

    def time_is_up(self, player):
        player.skin = self.player_copy.skin
        player.jump = self.player_copy.jump
        player.speed = self.player_copy.speed
        return player


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


class Background:
    def __init__(self, x, y, speed, image, position):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.position = position

    def draw_self(self):
        pass
        """
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
        """


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
            todo:
                - comments
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
sporn_x = 990
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


def draw_level_background():
    for i in range(len(background_list)):
        background_list[i].draw_self()


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

def play_music(game_state):
    if music_on:
        global music_menu
        if game_state < 4:
            if not music_menu:
                music_menu = True
                pygame.mixer.music.load("res/sound/menu_music.mp3")
        elif game_state == 4 :
            pygame.mixer.music.load("res/sound/level_music.mp3")
            music_menu = False
        elif game_state == 5: pygame.mixer.music.load("res/sound/lost_music.mp3")
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.stop()
        music_menu = False

def check_events(game_state):
    global music_on
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
                            if i == 0:
                               music_on= False
                               pygame.mixer.music.stop()
                            draw_options_background()
                        else:
                            check_box_list[i].is_clicked = True
                            if i == 0:
                                music_on = True
                                play_music(game_state)
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
    draw_menu_background("")
    gameDisplay.blit(logo_img, (185, 100))

    while game_state == 0:
        check_buttons()
        game_state = check_events(game_state)
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
        check_trans_button(play_button, play_button_img_list)
        game_state = check_events(game_state)
        pygame.display.update()
        clock.tick(30)
    return game_state


def menu_score_loop(game_state):
    gameDisplay.blit(menu_navbar, (0, 0))
    draw_menu_background()

    while game_state == 2:
        draw_level_background()
        # green_enemy1.draw_self()
        # player1.draw_self()
        check_buttons()
        game_state = check_events(game_state)
        pygame.display.update()
        clock.tick(10)
    return game_state


def main():
    game_state = 0
    former_game_state = 0
    play_music(game_state)
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
            - it is checked if an enemy has to be created based on the player position
        param:
            - enemy_status: array where enemy status is defined
            - player_pos: vertical position of player
        return:
            - enemy_status
        todo:
            - noch mehr gegner erstellen abh. von player_pos
    """
    # 0 = not created, 1 = create, 2 = created, 3 = dead
    if player_pos >= 500 and enemy_status[0] == 0:
        # if enemy is not created and player vertical pos above 500
        enemy_status[0] = 1
        # manipulate arrray, so that gameloop can create enemy
    elif player_pos >= 1000 and enemy_status[1] == 0:
        enemy_status[1] = 1

    return enemy_status


def game_loop(level_num):
    """
     	date:
     	    - 27.05.2020
     	desc:
     	    - here the game takes place
     	    - Create objects: player, jump, level, enemy
     	param:
             - level_num: selection is made in the level menu
         return:
             - game_state: to jump back to menu
     	todo:
     	    - Button um Spiel abzubrechen
     	    - Gegener einbinden an den Stellen wo Coins sind (Gegenerlogik)
     	    - Gegener sichtbart erstellen, abhägig von absoluter Position von Player
     	    - Gegner move methode in dauerschleife er bewegt sich auch wenn kein event; ähnlich zu idle zustand
     	    - Highscore abspeichern, diesen im Menü anzeigen können (-> siehe helpful code, zum abspeichern in extra Datei)
    """
    running = True
    # create objects
    std_jump = Jump(0)
    # high_jump = Jump()  # für rotes Item
    player = Player(pygame.Rect(BLOCKWIDTH, DISPLAYHEIGHT - 4 * BLOCKHEIGHT, PLAYERWIDTH, PLAYERHEIGHT), 0,
                    move_list_player, std_jump,
                    red_skin, 0, 20, 2, level_num)
    # red_item = Item("red", False, 5, red_skin, high_jump, 20, 0, player)
    # green_item = Item("green", False, 5, green_skin, std_jump, 30, 0, player)
    level = Level(level_num)

    enemy_status = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # 0 = not created, 1 = create, 2 = created, 3 = dead
    time = Timer()
    play_music(4)
    while running:
        # continuous loop until player dies or wins game
        running = player.handle_keys(running)
        gameDisplay.fill(BLUE)
        player.move()
        level.draw_level(player.player_rect.x, player.level_array)
        """
        # sporn_x = 990
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
        running = player.dead()
        pygame.display.update()  # Display updaten
        clock.tick(30)  # max 30 Herz
    play_music(0)
    return 0


main()
