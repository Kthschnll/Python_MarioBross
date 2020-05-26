import pygame as pg
import time
import os
from os import listdir
from os.path import isfile, join

# OS-Umgebung ---WIN10.10.02

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

pg.init()
clock = pg.time.Clock()

# display constants
DISPLAYWIDTH = 1000
DISPLAYHEIGHT = 600
DISPLAYFLAG = 0
DISPLAYCOLBIT = 32

BLOCKWIDTH = 25
BLOCKHEIGHT = 25

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (109, 107, 118)

# init display
gameDisplay = pg.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT), DISPLAYFLAG, DISPLAYCOLBIT)

# sprite preparation
left_walk = []
right_walk = []
up_walk = []  # sprung
down_walk = []  # landen

# level preparation
LEVEL_LENGTH = 2
ARRAY_Y = (DISPLAYWIDTH // BLOCKWIDTH)  # * LEVEL_LENGTH  = 24
ARRAY_X = DISPLAYHEIGHT // BLOCKHEIGHT  #
NORMAL_GROUND = BLOCKHEIGHT * (2 / 3 * ARRAY_X)

"""
    Erstellen des Levels, auslagern 
    Hilfe: from array import *
    level1_array = [[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]]
"""

# level grafics
resources_path = "res/level/"
# todo: hier aus großem Bild entsprechende Sachen ausschneiden
# siehe Youtube Video
ground = pg.transform.scale(pg.image.load(resources_path + "ground.png"), (BLOCKWIDTH, BLOCKHEIGHT))  # 1 in array

# load player assets
only_files = [files for files in listdir("res/player/") if isfile(join("res/player/", files))]

for myfile in only_files:
    if "right" in myfile:
        right_walk.append(pg.image.load("res/player/" + myfile))
    if "left" in myfile:
        left_walk.append(pg.image.load("res/player/" + myfile))
    # jump, down mising


def game_main(level_num):
    level = Level(level_num)  # Erstellen des Levels und Ausgabe von Start Level mit x = 0
    player = Player(DISPLAYWIDTH // 2,
                    NORMAL_GROUND - 31)  # todo: x pos. von Player soll am Anfang 0 sein und erst nach ein paar Metern in der Mitte
    run(level, player)  # solange hier drin bis Level zu Ende


def run(level, player):
    running = True

    mv_left = False
    mv_right = False
    mv_up = False
    mv_down = False

    while running:
        for event in pg.event.get():
            """
            if event.type == pg.Quit:
                running = False
                pg.QUIT()
            """
            # keyboard interactions
            if event.type == pg.KEYDOWN:
                # left
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    mv_left = True
                # right
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    mv_right = True
                # up
                if event.key == pg.K_UP or event.key == pg.K_w:
                    mv_up = True
                # down
                if event.key == pg.K_DOWN or event.key == pg.K_s:
                    mv_down = True

            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    mv_left = False
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    mv_right = False
                if event.key == pg.K_UP or event.key == pg.K_w:
                    mv_up = False
                if event.key == pg.K_DOWN or event.key == pg.K_s:
                    mv_down = False

        # movement
        if mv_left:
            player.move(0)
        if mv_right:
            player.move(1)
        if mv_up:
            player.move(2)
        if mv_down:
            player.move(3)


class Level:
    def __init__(self, num):
        self.x = 0  # x = Feld das ganz Links im Window angezeigt wird
        gameDisplay.fill(GREEN)
        self.load_level(num)

    def load_level(self, num):
        # todo: hier allegemeine Funktion um Abhängig von self.x Level zu zeichnen mit Hilfe von: level1_array
        # siehe Youtube Video
        for i in range(ARRAY_Y + 1):
            gameDisplay.blit(ground, (i * BLOCKWIDTH, NORMAL_GROUND))
        pg.display.update()


class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 15
        self.height = 32  # character picture height
        self.width = 16  # character picture width
        self.animation_count = 0
        self.health = 1

    def hit(self):
        """
        returns if character die
        """
        self.health -= 1
        if self.health <= 0:
            return True


class Player(Character):  # Aufruf mit: player(main.display_width / 2, main.display_height / 3)
    def __init__(self, x, y):
        super().__init__(x, y)
        self.draw(1)

    def draw(self, direction):
        self.animation_count += 1
        if self.animation_count + 1 >= 4:  # da nur 5 Bilder pro Movement haben
            self.animation_count = 0

        if direction == 0:
            gameDisplay.blit(left_walk[self.animation_count], (self.x, self.y))
        elif direction == 1:
            gameDisplay.blit(right_walk[self.animation_count], (self.x, self.y))
        elif direction == 2:
            gameDisplay.blit(up_walk[self.animation_count], (self.x, self.y))
        elif direction == 3:
            gameDisplay.blit(down_walk[self.animation_count], (self.x, self.y))
        pg.display.update()
        clock.tick(50)

    def move(self, direction):
        """
            - does effect Level x Wert, charackter y Wert if jump or down, draw function of level and character
        """
        self.draw(direction)
        pass

    def collide(self, level):
        """
            - with enemy or level
        """


"""class Enemy(Character):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        pass

    def draw(self):
        
           #draws the enemy with the given images
           #praram window: surfface
           #return none
        
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
        gameDisplay.blit(self.img, (self.x, self.y))
        self.move()
"""

# aufruf aus menu

level_num = 1
game_main(level_num)
