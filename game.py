import pygame as pg
import time
import os
from os import listdir
from os.path import isfile, join
from PIL import Image  # for mirror image

# OS-Umgebung ---WIN10.10.02

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

pg.init()
clock = pg.time.Clock()

# display constants
DISPLAYWIDTH = 1000
DISPLAYHEIGHT = 600
DISPLAYFLAG = 0
DISPLAYCOLBIT = 32

BLOCKWIDTH = 50
BLOCKHEIGHT = 50

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (109, 107, 118)

# init display
gameDisplay = pg.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT), DISPLAYFLAG, DISPLAYCOLBIT)

# level preparation
LEVEL_LENGTH = 2
ARRAY_Y = (DISPLAYWIDTH // BLOCKWIDTH)  # * LEVEL_LENGTH
ARRAY_X = DISPLAYHEIGHT // BLOCKHEIGHT  #
NORMAL_GROUND = BLOCKHEIGHT * ((2 * ARRAY_X) // 3)  # normalground ist die kleinste Höhe auf der sich spieler befindet

"""
    Erstellen des Levels, auslagern 
    Hilfe: from array import *
    level1_array = [[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]]
"""

# level grafics
resources_path_level = "res/level/"
# todo: hier aus großem Bild entsprechende Sachen ausschneiden
# siehe Youtube Video
ground = pg.transform.scale(pg.image.load(resources_path_level + "ground.png"), (BLOCKWIDTH, BLOCKHEIGHT))  # 1 in array

# player preparation
left_walk = []
right_walk = []
jump_walk = []  # sprung
idle_walk = []  # landen
PLAYERHEIGHT = 75
PLAYERWIDTH = 50

# player grafics
resources_path_player = "res/player/"
only_files = [files for files in listdir(resources_path_player) if isfile(join(resources_path_player, files))]

"""
# transpose pictures
for myfile in only_files:
    if "right" in myfile:
        img = Image.open(resources_path_player + myfile)
        img.transpose(Image.FLIP_LEFT_RIGHT).save(resources_path_player + "transpose_" + myfile)
"""

for myfile in only_files:
    if "left" in myfile:
        left_walk.append(pg.transform.scale(pg.image.load(resources_path_player + myfile), (PLAYERWIDTH, PLAYERHEIGHT)))
    if "right" in myfile:
        right_walk.append(
            pg.transform.scale(pg.image.load(resources_path_player + myfile), (PLAYERWIDTH, PLAYERHEIGHT)))
    if "jump" in myfile:
        jump_walk.append(pg.transform.scale(pg.image.load(resources_path_player + myfile), (PLAYERWIDTH, PLAYERHEIGHT)))
    if "idle" in myfile:
        idle_walk.append(pg.transform.scale(pg.image.load(resources_path_player + myfile), (PLAYERWIDTH, PLAYERHEIGHT)))


def game_main(level_num):
    level = Level(level_num)  # Erstellen des Levels und Ausgabe von Start Level mit x = 0
    player = Player(0, NORMAL_GROUND - PLAYERHEIGHT)
    run(level, player)  # solange hier drin bis Level zu Ende


def run(level, player):
    running = True

    mv_left = False
    mv_right = False
    mv_up = False
    mv_idle = True

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
                mv_idle = True

        # movement
        if mv_left:
            player.move(0)
        if mv_right:
            player.move(1)
        if mv_up:
            player.move(2)
        if mv_idle:
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
        self.speed = 50
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


class Player(Character):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.draw(3)

    def draw(self, direction):
        self.animation_count += 1
        if direction == 0:
            if self.animation_count + 1 >= len(left_walk):
                self.animation_count = 0
            gameDisplay.blit(left_walk[self.animation_count], (self.x, self.y))
        elif direction == 1:
            if self.animation_count + 1 >= len(right_walk):
                self.animation_count = 0
                if self.x < (DISPLAYWIDTH / 2 - PLAYERWIDTH / 2):
                    self.x += self.speed
            gameDisplay.blit(right_walk[self.animation_count], (self.x, self.y))
        elif direction == 2:
            if self.animation_count + 1 >= len(jump_walk):
                self.animation_count = 0
            gameDisplay.blit(jump_walk[self.animation_count], (self.x, self.y))
        elif direction == 3:
            if self.animation_count + 1 >= len(idle_walk):
                self.animation_count = 0
            gameDisplay.blit(idle_walk[self.animation_count], (self.x, self.y))
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
