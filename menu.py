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
# load buttons
button_names = ["_sdt", "_hower", "_clicked"]
button_image_list = []

for i in range(3):
    button_image_list.append(
        pygame.transform.scale(pygame.image.load(resources_path + "button" + button_names[i] + ".png"), (90, 30)))

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
            self.button_color = button_image_list[2]
        gameDisplay.blit(self.button_color, (self.button_rect.x, self.button_rect.y))
        static_display(self.button_text, 20, white, (self.button_rect.x + 43, self.button_rect.y + 18))

    def action(self, game_state):
        stay = True
        if self.function != game_state:
            game_state = self.function
        return game_state


home_button = Button("Home", pygame.Rect(4, 5, 90, 30), 0)
level_button = Button("Level", pygame.Rect(98, 5, 90, 30), 1)
scores_button = Button("Scores", pygame.Rect(192, 5, 90, 30), 2)

menu_button_list = [home_button, level_button, scores_button]


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


def check_buttons():
    for i in range(len(menu_button_list)):
        if menu_button_list[i].button_rect.collidepoint(pygame.mouse.get_pos()):
            menu_button_list[i].button_color = button_image_list[1]
        else:
            menu_button_list[i].button_color = button_image_list[0]

        menu_button_list[i].draw_self()


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
        elif event.type == pygame.MOUSEBUTTONUP:
            # 1 is the left mouse button, 2 is middle, 3 is right.
            if event.button == 1:
                # check buttons
                for i in range(len(menu_button_list)):
                    if menu_button_list[i].is_clicked:
                        menu_button_list[i].is_clicked = False
                        game_state = menu_button_list[i].action(game_state)
    return game_state


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
            x = i%3 * 290 + 80
            y = j * 250 + 100
            gameDisplay.blit(level_background, (x, y))
            gameDisplay.blit(level_place_holder, (x - 10, y - 10))
            static_display(str(j*3+i-2), 40, white, (x + 40, y + 40))

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
    while game_state != 100:
        if game_state == 0:
            game_state = menu_home_loop(0)
        elif game_state == 1:
            game_state = menu_level_loop(1)
        elif game_state == 2:
            game_state = menu_score_loop(2)


main()
