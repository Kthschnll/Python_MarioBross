import os
from enum import Enum

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame

pygame.init()

# display constants
display_width = 1000
display_height = 600

# menu grafics
resources_path = "res/menu/"
resources_path_player = "res/player/"
resources_path_level_background = "res/level_background/"
resources_path_enemy = "res/enemy/1/"
menu_background = pygame.transform.scale(pygame.image.load(resources_path + "Background.png"), (1000, 600))
menu_navbar = pygame.transform.scale(pygame.image.load(resources_path + "Navbar_back.png"), (1000, 40))
level_background = pygame.transform.scale(pygame.image.load(resources_path + "Level_back.png"), (240, 175))
level_place_holder = pygame.transform.scale(pygame.image.load(resources_path + "level_place_holder.png"), (240, 175))
options_menu_background = pygame.transform.scale(pygame.image.load(resources_path + "Option_menu_background.png"),
                                                 (200, 110))
default_img = pygame.transform.scale(pygame.image.load(resources_path + "default_img.png"),(1, 1))

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

# load charrackter sprites
run_right_img_list = []
run_left_img_list = []
stay_img_list = []
jump_right_img_list = []
jump_left_img_list = []

j = 0
for i in range(8):
    run_right_img_list.append(
        pygame.transform.scale(pygame.image.load(resources_path_player + "right0" + str(i + 1) + ".png"), (50, 75)))
for i in range(12):
    stay_img_list.append(
        pygame.transform.scale(pygame.image.load(resources_path_player + "idle" + str(j) + str(i + 1) + ".png"),
                               (50, 75)))
    if i == 8:
        j = str(j)
        j = ""
for i in range(8):
    run_left_img_list.append(
        pygame.transform.scale(pygame.image.load(resources_path_player + "left0" + str(i + 1) + ".png"), (50, 75)))
for i in range(4):
    jump_right_img_list.append(
        pygame.transform.scale(pygame.image.load(resources_path_player + "jump_right" + str(i) + ".png"), (50, 75)))
for i in range(4):
    jump_left_img_list.append(
        pygame.transform.scale(pygame.image.load(resources_path_player + "jump_left" + str(i) + ".png"), (50, 75)))

jump_mid_right_img_list = [jump_right_img_list[0], jump_right_img_list[0], jump_right_img_list[3]]
jump_mid_left_img_list = [jump_left_img_list[0], jump_left_img_list[0], jump_left_img_list[3]]

# load enemy sprites
green_enemy_right = []
green_enemy_left = []
for i in range(8):
    green_enemy_right.append(
        pygame.transform.scale(pygame.image.load(resources_path_enemy + "green_alien"+str(i) + ".png"), (50, 75)))
    green_enemy_left.append(pygame.transform.flip(green_enemy_right[i],True,False))

# load level background
background_img = []
for i in range(5):
    background_img.append(
        pygame.transform.scale(pygame.image.load(resources_path_level_background + "bg" + str(i + 1) + ".png"),
                               (1000, 600)))

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (80, 80, 80)

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
        static_display(self.button_text, 20, white, (self.button_rect.x + 43, self.button_rect.y + 18))

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
    def __init__(self, player_rect, current_move, img_list, state):
        self.player_rect = player_rect
        self.current_move = current_move
        self.img_list = img_list
        self.state = state


# Class Player
class Player(Species):
    def __init__(self, player_rect, current_move, jump, img_list, state):
        super().__init__(player_rect, current_move, img_list, state)
        self.jump = jump

    def draw_self(self):
        if not self.jump.is_jumping:
            gameDisplay.blit(self.img_list[self.current_move][int(self.state)],
                             (self.player_rect.x, self.player_rect.y))
            if self.state < (len(self.img_list[self.current_move]) - 1):
                self.state += 1
            else:
                self.state = 0
        else:
            self.player_rect.y = self.jump.calc_new_y()
            if self.jump.jump_count >= 0:
                gameDisplay.blit(self.img_list[self.current_move + 3][1], (self.player_rect.x, self.player_rect.y))
            else:
                gameDisplay.blit(self.img_list[self.current_move + 3][2], (self.player_rect.x, self.player_rect.y))


# create a Player
player1 = Player(pygame.Rect(400, 400, 50, 75), 0, std_jump,
                 [stay_img_list, run_right_img_list, run_left_img_list, jump_mid_right_img_list, jump_right_img_list,
                  jump_left_img_list,
                  jump_mid_left_img_list], 0)


# class enemy
class Enemy(Species):
    def __init__(self, player_rect, current_move, img_list, state, alive,pace,range,sporn_x):
        super().__init__(player_rect, current_move, img_list, state)
        self.alive = alive
        self.pace = pace
        self.range = range
        self.sporn_x = sporn_x

    def draw_self(self):
        gameDisplay.blit(self.img_list[self.current_move][self.state], (self.player_rect.x, self.player_rect.y))
        self.calc_next_x_position()
        if self.state < (len(self.img_list[self.current_move]) - 1):
            self.state += 1
        else:
            self.state = 0

    def calc_next_x_position(self):
        if self.current_move == 0:
            if self.player_rect.x < self.sporn_x+self.range:
                self.player_rect.x += self.pace
            else: self.current_move = 1
        if self.current_move == 1:
            if self.player_rect.x > self.sporn_x-self.range:
                self.player_rect.x -= self.pace
            else: self.current_move = 0


green_enemy1 = Enemy(pygame.Rect(700, 400, 50, 75), 0, [green_enemy_right,green_enemy_left], 0, True,2,60,700)
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


# create backgrounds
background_4 = Background(0, 0, 0, background_img[4], 0)
background_32 = Background(sporn_x, 0, 1, background_img[3], 0)
background_31 = Background(0, 0, 1, background_img[3], 0)
background_22 = Background(sporn_x, 0, 2, background_img[2], 0)
background_21 = Background(0, 0, 2, background_img[2], 0)
background_12 = Background(sporn_x, 0, 3, background_img[1], 0)
background_11 = Background(0, 0, 3, background_img[1], 0)
background_02 = Background(sporn_x, 0, 5, background_img[0], 0)
background_01 = Background(0, 0, 5, background_img[0], 0)

background_list = [background_4, background_32, background_31, background_22, background_21, background_12,
                   background_11, background_02, background_01]


# printen
def text_object(text="", font="", color="red"):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_display(text="", size=50, color="red"):
    largeText = pygame.font.Font("freesansbold.ttf", size)
    TextSurf, TextRect = text_object(text, largeText, color)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


def static_display(text="", size=10, color="black", position=((display_width / 2), (display_height / 2))):
    largeText = pygame.font.Font("freesansbold.ttf", size)
    TextSurf, TextRect = text_object(text, largeText, color)
    TextRect.center = position
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()


# init display
gameDisplay = pygame.display.set_mode((display_width, display_height))
gameDisplay.fill(white)
pygame.display.set_caption("MarioPy")

clock = pygame.time.Clock()


def draw_menu_background(text=""):
    gameDisplay.blit(menu_background, (0, 38))
    static_display(text, 20, white, (100, 100))


def draw_options_background():
    gameDisplay.blit(options_menu_background, (796, 35))
    static_display("Music", 20, white, (840, 70))
    static_display("Sound effects", 18, white, (870, 110))


def draw_level_place_holder():
    for i in range(int(level_count / 2)):
        for j in range(int(level_count / 3)):
            x = i % 3 * 290 + 80
            y = j * 250 + 100
            gameDisplay.blit(level_background, (x, y))
            gameDisplay.blit(level_place_holder, (x - 10, y - 10))
            if (j * 3 + i) > 0:
                static_display("comming soon...", 20, gray, (x + 100, y + 90))


def draw_level_nums():
    for i in range(int(level_count / 2)):
        for j in range(int(level_count / 3)):
            x = i % 3 * 290 + 80
            y = j * 250 + 100
            static_display(str(j * 3 + i + 1), 40, white, (x + 40, y + 40))


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
        green_enemy1.draw_self()
        player1.draw_self()
        check_buttons()
        game_state = check_events(game_state)
        pygame.display.update()
        clock.tick(30)
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


main()
