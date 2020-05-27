import pygame as pg
import time
import os
from os import listdir
from os.path import isfile, join
from enum import Enum  # für enums  todo: wird derzeit nicht benötigt
from menu import player1
# import skrits from project
from level import get_level_array


# wichtig: - absolute Postion des Player -> insgesamter Bewegungfortschritt; zurückgelegte distanz des Player
#          - raltive Position von Player -> x-Position auf dem Bildschirm
# todo (am Ende):   - extra: in allen Methoden angeben wie sie getestet werden können
#                   - in Methoden/Funktionen todos schreiben wie Projekt erweitert werden kann

# OS-Umgebung ---WIN10.10.02

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

pg.init()
clock = pg.time.Clock()

# display constants
DISPLAYWIDTH = 1000
DISPLAYHEIGHT = 600
HALF_DISPLAYWIDTH = DISPLAYHEIGHT / 2

DISPLAYFLAG = 0
DISPLAYCOLBIT = 32

BLOCKWIDTH = 50  # BLOCKWIDTH so wählen dass gerade DISPLAYWIDTH/BLOCKWITDH = gerade Zahl
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
NORMAL_GROUND = (
                        DISPLAYHEIGHT // 3) * 2  # normalground ist die kleinste Höhe auf der sich Spieler befindet #todo sollte unnötig werden, wenn player Gravitation hat und von oben auf Displayer föllt

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
# Methode um Bilder zu spiegeln 
for myfile in only_files:
    if "right" in myfile:
        img = Image.open(resources_path_player + myfile)
        img.transpose(Image.FLIP_LEFT_RIGHT).save(resources_path_player + "transpose_" + myfile)
"""
# die Bildernamen in entsprechnedes Array laden
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
    """
     	date:
     	    - 27.05.2020
     	desc:
     	    - Objekte Player, Level erstellen
     	    - run() dort findet der Spielablauf statt (es werde Eingaben entgegengenommen)
     	param:
             - level_num: Level Nummer, Auswahl geschieht im Menü
         return:
             - nothing
     	todo:
     	    - zurückspringen ins Menü
     	    - Highscore abspeichern, wenn im Menü dann Punktzahl returnen
     	    - Gegener erstellen
    """

    level = Level(level_num)  # Erstellen des Levels und Ausgabe von Start Level mit x = 0
    player = Player(NORMAL_GROUND - PLAYERHEIGHT, 20, PLAYERHEIGHT, PLAYERWIDTH, 2)
    run(level, player)  # solange hier drin bis Level zu Ende


def run(level, player):
    """
     	date:
     	    - 27.05.2020
     	desc:
     	    - auf Grund von Events(Tasteneingaben) Gegner und Level verändern
     	param:
             - Objecte: Player, Level
         return:
             - nothing
     	todo:
     	    - eventuell wieder mit variablen für richutng abrieten:true false; diese abfragen und setzten somit leicher idle als dauerhafter stustand
     	    - mehrere Events auch ohne pg.key.set:repeat(), damit bei gedrückter Taste mehrere Events entstehen
     	    - testen ob clock tick funktioniert!!!; passende Zeit für clock(ticck)
     	    - Zustand idle nicht die ganze Zeit dazwischen reinmachen
     	    - wenn bestimmte Taste gedrückt wird Spiel beenden -> running = False
     	    - pg.event.quit einbauen -> bei druck auf Fenster X dieses schließen
     	    - Gegener sichtbart machen/ erstellen, abhägig von absoluter Position von Player
     	    - Gegner move methode in dauerschleife er bewegt sich auch wenn kein event; ähnlich zu idle zustand
    """
    player1.draw_self()
    running = True
    pg.key.set_repeat(100,
                      100)  # erster par. wann das erste mal wiederholt wird, zweiter par. ab dem 2ten mal Intervall

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
                    player.move(0, level)
                    player.draw(0)
                # right
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    player.move(1, level)
                    player.draw(1)
                # jump
                if event.key == pg.K_UP or event.key == pg.K_w:
                    player.move(2, level)
                    player.draw(2)

            # draw level new
            level.draw_level(player.x)  # um Level Blöcke neu zu zeichen abhänig von absoluter Player Position x
            pg.display.update()  # komplettes window updaten
            clock.tick(30)  # Framerate höchstens 30

        # Dauerschleife für idle falls kein neues event in python
        player.draw(3)
        """
        max_x = DISPLAYWIDTH / 2 - PLAYERWIDTH / 2  # max.x relative position von Player, damit dieser in der Mitte erscheint
        if player.x < max_x:  # wenn absolute Position noch nicht in der Mitte von Bildschirm ist
            max_x = player.x  # setzte relative Position ist gleich absolute Position
        gameDisplay.fill(GREEN)
        player_rect = pg.Rect(max_x, player.y, PLAYERWIDTH, PLAYERHEIGHT)
        pg.display.update(player_rect)  # nur Bereich von Player updaten
        """


class Level:
    """
     	todo:
     	    - erstellen des Arrays auslagern in andere Datei
     	    - Level muss am ende eine halbe displaygröße gößer sein wie letzte letzte absolute Player position
    """

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
                - player.x
            return:
                - nothing
        	todo:
        	    - in if neue Blockarten reinmachen
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
                value = self.level_array[x][y]  # value = id von richtigem Block
                if value == 1:  # ground
                    block = ground
                else:
                    continue
                gameDisplay.blit(block, (i * BLOCKWIDTH - rest, y * BLOCKHEIGHT)) # Block wird auf Display gezeichnet, i um an richtiger x-Stelle auf Display zu zeichnen
            i += 1

class Character:
    def __init__(self, x, y, speed, height, width, health):
        self.x = x  # absolute position in Pixel
        self.y = y  # absolute Position in Pixel
        self.speed = speed
        self.height = height  # character picture height
        self.width = width  # character picture width
        self.animation_count = 0
        self.health = health  # Gesundheit

    def hit(self):
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
                 - true wenn Charckter gehittet wird
         	todo:
         	    - ganze Funktionn
        """
        pass


class Player(Character):
    def __init__(self, y, speed, height, width, health):
        super().__init__(BLOCKWIDTH, y, speed, height, width,
                         health)  # player Anfangsposition ist BLOCKWidth vom linken Diplayrand

    def draw(self, direction):
        """
            date:
                - 27.05.2020
            desc:
                - in Abhängigkeit von der Bewegung die Player (aufgrund von Tastedruck) macht wird sein neues Bild an der richtigen Position gezeichnet
            param:
                - direction: Richtung in die sich Player bewegt
            return:
                - nothing
            todo:
                - bei bewegungswechsel muss neue bewegung mit count = 0 anfangen, extra animation_count für jede bewegungsart??
                - player.animation_count_left = 0  # damit Bewegung immer mit erstem Bild anfängt
                - Abfrage ob Länge des Arrays überschritten wird mit Hilfe von enums, damit nur eine Abfrage rauskommt
        """

        max_x = DISPLAYWIDTH / 2 - PLAYERWIDTH / 2  # relative Position von Player, damit Player in der Mitte des Display erscheint
        self.animation_count += 1  # damit die nächste Animation geladen wird

        if self.x < max_x:  # wenn die absolute Position von Player noch kleiner wie die relative ist
            max_x = self.x  # Player ist noch nicht bis zur mitte gelaufen; Anfang vom Level

        gameDisplay.fill(GREEN)  # um ganzes Bild neuzuladen # todo:nicht mehr nötig wen Hintergrund davor geladen wird?

        # left
        if direction == 0:
            if self.animation_count + 1 >= len(
                    left_walk):  # wenn letztes element von Array erreicht -> Bewegung von Vorne anfangen
                self.animation_count = 0
            gameDisplay.blit(left_walk[self.animation_count],
                             (max_x, self.y))  # Player an Position auf Display zeichnen
        # right
        elif direction == 1:
            if self.animation_count + 1 >= len(right_walk):
                self.animation_count = 0
            gameDisplay.blit(right_walk[self.animation_count], (max_x, self.y))
        # jump
        elif direction == 2:
            if self.animation_count + 1 >= len(jump_walk):
                self.animation_count = 0
            gameDisplay.blit(jump_walk[self.animation_count], (max_x, self.y))
        # idle
        elif direction == 3:
            if self.animation_count + 1 >= len(idle_walk):
                self.animation_count = 0
            gameDisplay.blit(idle_walk[self.animation_count], (max_x, self.y))

    def move(self, direction, level):
        """
            date:
                - 27.05.2020
            desc:
                - in Abhängigkeit von der Bewegung die Player (aufgrund von Tastedruck) macht und seinem speed wird sein neue y und seine absolute Postion x ermittel
            param:
                - direction: Richtung in die sich Player bewegen WILL, muss noch mit collide überprüft werden
                - level: Object
            return:
                - nothing
            todo:
                - collisionen mit Blöcken aus Level erkennen -> Bewegung wird gestoppt
                - richtige Jump Bewegung implementieren (dazwischen zeichnen), Sprung kann nach links/rechts gehen, Player hat Gravitation
                - in player.draw muss Bild 01, 02 solange wiederholt werden bis player boden ereicht
        """

        # left
        if direction == 0:
            self.x -= self.speed
        # right
        if direction == 1:
            self.x += self.speed
        # jump
        if direction == 2:
            self.y -= self.speed
            clock.tick(500)
            self.draw(direction)
            self.y += self.speed
            # todo: ist :  self.level_array[][]
        self.collide(level)

    def collide(self, level):
        """
            - with enemy or level
        """
        if self.x < 0:
            self.x = 0
        # todo: if selx.x >= level_end: self.x = level_end


class Enemy(Character):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        """
        	date:
        	    - 27.05.2020
        	desc:
        	    - bewegt sich immer so lange in eine Richtung bis er kolliediert, dann richuntgswechsel
        	    - Methode muss im loop mit rein, damit sich Spieler immer beieinem Durchlauf bewegt
        	todo:
        	    - alles
        """
        pass

    def draw(self):
        """
            date:
                - 27.05.2020
            desc:
                - Ähnlichkeit zu player.draw
            todo:
                - alles
        """
        pass


# todo: Aufruf aus menu

level_num = 1
game_main(level_num)
