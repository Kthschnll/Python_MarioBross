import pygame as pg
import time
import os
from os import listdir
from os.path import isfile, join

from enum import Enum  # für enums  todo: enum für left_walk,right_walk,jump_walk,idle_walk um entprechenden, siehe player.draw


"""

wichtig todo: zwieten damit animationen passen -> mehrere events kommen auch ohne die eine funktion


"""
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
level_length = 5
temp_y = DISPLAYHEIGHT // BLOCKHEIGHT  # 12
temp_x = (DISPLAYWIDTH // BLOCKWIDTH) * level_length  # 20
NORMAL_GROUND = (DISPLAYHEIGHT // 3) * 2  # normalground ist die kleinste Höhe auf der sich spieler befindet

"""
    Erstellen des Levels, auslagern 
    Hilfe: from array import *
    level1_array = [[0,0,0,0,0,0,0],[1,1,1,1,1,1,1],[1,1,1,1,1,1,1]]
"""

# level grafics
resources_path_level = "res/level/"
ground = pg.transform.scale(pg.image.load(resources_path_level + "ground.png"), (BLOCKWIDTH, BLOCKHEIGHT))  # 1 in array
# todo weiter blöcke hinzufügen, eventuell methode um aus großem bild in python auszuschenden, sinnvoll??

# player preparation
left_walk = []
right_walk = []
jump_walk = []  # sprung
idle_walk = []  # idle

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
    player = Player(BLOCKWIDTH, NORMAL_GROUND - PLAYERHEIGHT, 20, PLAYERHEIGHT, PLAYERWIDTH, 2)

    run(level, player)  # solange hier drin bis Level zu Ende


def run(level, player):
    running = True
    pg.key.set_repeat(50, 50)  # erster par. wann das erste mal wiederholt wird, zweiter par. ab dem 2ten mal  intervall
    # todo: anders möglich? ohne die anweisung darüber
    while running:
        for event in pg.event.get():
            """
            if event.type == pg.Quit:
                running = False
                pg.QUIT()
            """
            # keyboard interactions
            if event.type == pg.KEYDOWN:
                # player.animation_count = 0  # damit Bewegung immer mit erstem Bild anfängt
                # left
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    player.move(0, level)
                # right
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    player.move(1, level)
                # jump
                # todo: Bild 01, 02 müssen solange wiederholt werden bis player boden ereicht (davor collision machen erkennung)
                if event.key == pg.K_UP or event.key == pg.K_w:
                    player.move(2, level)

        player.move(3, level)  # Dauerschleife für idle falls kein event in python
        # todo: schlecht da es die ganze Zeit rein geht zwischen anderen movements


class Level:
    def __init__(self, num):
        self.x = 0  # x = Feld das ganz Links im Window angezeigt wird
        """
        if num == 0:
            # todo: entprechendes array laden (aus anderer Datei laden)
            #   self.level_array = ...
        """
        # todo: in anderer Datei Level erstellen mit Blöcken an den richtigen stellen, level muss am ende eine halbe displaygröße gößer sein wie letzte pos die spieler erreichen kann
        # generate Level to see something
        # array hat y Listen, jede Liste hat x werte
        # level_array mit Nullen befüllen
        self.level_array = [[0 for i in range(temp_y)] for j in range(temp_x)]
        # einzelne Werte in Array eingeben
        #   [Liste][Element] ; NORMAL_GROUND // BLOCKHEIGHT = 8
        for i in range(0, 10):
            self.level_array[i][NORMAL_GROUND // BLOCKHEIGHT] = 1  # 1 = normal ground
        self.level_array[19][NORMAL_GROUND // BLOCKHEIGHT] = 1
        self.draw_level(0)

    def draw_level(self, player_pos):
        # todo: nicht nur ganze arrays überspringen sondern self.player.speed
        # todo: ende von array muss sich auf spieler zu bewegen
        # allgemeine Funktion um Abhängig von player_pos Level zu zeichnen
        # Grenzen von array x, y berechnen das nötig ist für die ausgabe
        player_array_pos = player_pos // BLOCKWIDTH  # position von player im Array
        space = (DISPLAYWIDTH // 2) // BLOCKWIDTH  # Felder die nach links/rechts auf display kommen
        print(player_array_pos, space)
        if player_array_pos > space:
            left_border = player_array_pos - space
            right_border = player_array_pos + space
        else:  # Spieler läuft die ersten paar Meter -> nach links geht Level nicht weiter
            left_border = 0
            right_border = temp_x

        # for-loop begrenzen
        for x in range(left_border, right_border):
            for y in range(0, temp_y):
                value = self.level_array[x][y]
                if value == 1:  # ground
                    gameDisplay.blit(ground, (x * BLOCKWIDTH, y * BLOCKHEIGHT))


class Character:
    def __init__(self, x, y, speed, height, width, health):
        self.x = x
        self.y = y
        self.speed = speed
        self.height = height  # character picture height
        self.width = width  # character picture width
        self.animation_count = 0
        self.health = health

    def hit(self):
        """
        returns if character die
        """
        self.health -= 1
        if self.health <= 0:
            return True


class Player(Character):
    def __init__(self, x, y, speed, height, width, health):
        super().__init__(x, y, speed, height, width, health)


    def draw(self, direction, level):
        gameDisplay.fill(GREEN)  # um alles vorherige zu löschen
        max_x = DISPLAYWIDTH / 2 - PLAYERWIDTH / 2

        if self.x < max_x:
            max_x = self.x

        self.animation_count += 1
        # todo: bei bewegungswechsel muss neue bewegung mit count = 0 anfangen, extra animation count für jede bewegungsart??
        # left
        if direction == 0:
            if self.animation_count + 1 >= len(left_walk):  # todo diese if abfrage mit enum für alle Arrays machen
                self.animation_count = 0
            gameDisplay.blit(left_walk[self.animation_count], (max_x, self.y))
        # right
        if direction == 1:
            if self.animation_count + 1 >= len(right_walk):
                self.animation_count = 0
            gameDisplay.blit(right_walk[self.animation_count], (max_x, self.y))
        # jump
        if direction == 2:
            if self.animation_count + 1 >= len(jump_walk):
                self.animation_count = 0
            gameDisplay.blit(jump_walk[self.animation_count], (max_x, self.y))
        # idle
        if direction == 3:
            if self.animation_count + 1 >= len(idle_walk):
                self.animation_count = 0
            gameDisplay.blit(idle_walk[self.animation_count], (max_x, self.y))

        level.draw_level(self.x)  # um Level blöcke neu zu zeichen
        pg.display.update()  # komplettes window updaten
        clock.tick(50)

    def move(self, direction, level):
        """
            - does effect Level x Wert, charackter y Wert if jump or down, draw function of level and character
        """
        # left
        if direction == 0:
            self.x -= self.speed
            if self.x < 0:
                self.x = 0
        # right
        if direction == 1:
            self.x += self.speed
        # jump
        if direction == 2:
            self.y -= self.speed
            clock.tick(500)
            self.draw(direction, level)
            self.y += self.speed
            # todo: ist :  self.level_array[][]
        self.draw(direction, level)

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
