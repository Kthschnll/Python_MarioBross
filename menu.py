import os
from enum import Enum

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame

pygame.init()

# display constants
display_width = 1000
display_height = 600

# menu grafics
resources_path = "res/"
menu_background = pygame.transform.scale(pygame.image.load(resources_path + "Background.png"), (1000, 600))
menu_navbar = pygame.transform.scale(pygame.image.load(resources_path + "Navbar_back.png"), (1000, 40))
level_background = pygame.transform.scale(pygame.image.load(resources_path + "Level_back.png"), (240, 175))
level_place_holder = pygame.transform.scale(pygame.image.load(resources_path + "level_place_holder.png"), (240, 175))
options_menu_background = pygame.transform.scale(pygame.image.load(resources_path + "Option_menu_background.png"), (200, 300))

# load buttons
button_names = ["_sdt", "_hower", "_clicked"]
options_button_names = ["", "_hower", "_click"]
check_box_names = ["cb_unchecked","cb_hover","cb_checked2"]
button_image_list = []
options_button_list = []
cb_img_list = []

for i in range(len(button_names)):
    button_image_list.append(
        pygame.transform.scale(pygame.image.load(resources_path + "button" + button_names[i] + ".png"), (90, 30)))
    options_button_list.append(
        pygame.transform.scale(pygame.image.load(resources_path + "button_options" + options_button_names[i] + ".png"),
                               (30, 30)))
    cb_img_list.append(pygame.transform.scale(pygame.image.load(resources_path + check_box_names[i] +".png"), (30, 30)))

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gray = (109, 107, 118)

plane_list = ["home_menu", "level_menu"]

# level
level_count = 6


# Buttons
class Button:
    def __init__(self, button_text, button_rect, function, is_clicked=False, button_color=button_image_list[0]):
        self.button_color = button_color
        self.button_text = button_text
        self.button_rect = button_rect
        self.is_clicked = is_clicked
        self.function = function

    def draw_self(self):
        if self.is_clicked:
            if self.button_color in options_button_list:
                self.button_color = options_button_list[2]
            elif self.button_color in cb_img_list:
                self.button_color = cb_img_list[2]
            else: self.button_color = button_image_list[2]

        gameDisplay.blit(self.button_color, (self.button_rect.x, self.button_rect.y))
        static_display(self.button_text, 20, white, (self.button_rect.x + 43, self.button_rect.y + 18))

    def action(self, game_state):
        stay = True
        if self.function != game_state:
            game_state = self.function
        elif game_state == 3 and self.function == 3:
            game_state = 0
        return game_state


home_button = Button("Home", pygame.Rect(4, 5, 90, 30), 0)
level_button = Button("Level", pygame.Rect(98, 5, 90, 30), 1)
scores_button = Button("Scores", pygame.Rect(192, 5, 90, 30), 2)
options_button = Button("", pygame.Rect(966, 5, 30, 30), 3, False, options_button_list[0])
check_box_music = Button("",pygame.Rect(950, 52, 30, 30),4,False,cb_img_list[0])
check_box_sound = Button("",pygame.Rect(950, 92, 30, 30),4,False,cb_img_list[0])

menu_button_list = [home_button, level_button, scores_button]
check_box_list=[check_box_music,check_box_sound]


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
gameDisplay.fill(gray)
pygame.display.set_caption("MarioPy")

clock = pygame.time.Clock()


def draw_menu_background(text=""):
    gameDisplay.blit(menu_background, (0, 0))
    gameDisplay.blit(menu_navbar, (0, 0))
    static_display(text, 20, white, (100, 100))

def draw_options_background():
    gameDisplay.blit(options_menu_background, (796, 35))
    static_display("Music", 20, white, (840, 70))
    static_display("Sound effects", 18, white, (870, 110))

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

def check_events(game_state):
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
                        else: check_box_list[i].is_clicked = True
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
    return game_state

def options_menu_loop(game_state,former_game_state):
    draw_options_background()

    while game_state == 3:
        check_buttons()
        check_check_boxes()
        game_state = check_events(game_state)
        pygame.display.update()
        clock.tick(30)
    return former_game_state


def menu_home_loop(game_state):
    draw_menu_background("Home_slide")

    while game_state == 0:
        check_buttons()
        game_state = check_events(game_state)
        pygame.display.update()
        clock.tick(30)
    return game_state


def menu_level_loop(game_state):
    draw_menu_background()

    for i in range(level_count):
        for j in range(int(level_count / 3)):
            x = i % 3 * 290 + 80
            y = j * 250 + 100
            gameDisplay.blit(level_background, (x, y))
            gameDisplay.blit(level_place_holder, (x - 10, y - 10))
            static_display(str(j * 3 + i - 2), 40, white, (x + 40, y + 40))

    while game_state == 1:
        check_buttons()
        game_state = check_events(game_state)
        pygame.display.update()
        clock.tick(30)
    return game_state


def menu_score_loop(game_state):
    draw_menu_background()

    while game_state == 2:
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
            game_state = options_menu_loop(3,former_game_state)


main()
