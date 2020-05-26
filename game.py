import pygame as pg
import time
from os import listdir
from os.path import isfile, join

# OS-Umgebung ---WIN10.10.02

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
ARRAY_LENGHT = (DISPLAYWIDTH // BLOCKWIDTH) * LEVEL_LENGTH
ARRAY_HIGHT = DISPLAYHEIGHT // BLOCKHEIGHT


i = ((DISPLAYHEIGHT // BLOCKHEIGHT) // 3) - 1
print(type(i))
level1_array = [ARRAY_LENGHT][ARRAY_HIGHT] # because of fail not: level1_array = [ARRAY_LENGHT][ARRAY_HIGHT]

# Erstellen des Levels, auslagern
for y in range(((DISPLAYHEIGHT / BLOCKHEIGHT) / 3) - 1):
    for x in range((DISPLAYWIDTH / BLOCKWIDTH) * LEVEL_LENGTH):
        level1_array = [y][x] = 1

# level grafics
resources_path = "res/level/"
ground = pg.transform.scale(pg.image.load(resources_path + "ground.png"), (BLOCKWIDTH, BLOCKHEIGHT))  # 1 in array

only_files = [files for files in listdir("res/player/") if isfile(join("res/player/", files))]

for myfile in only_files:
    if "right" in myfile:
        right_walk.append(pg.image.load("res/player/" + myfile))
        print(left_walk[0])
    if "left" in myfile:
        left_walk.append(pg.image.load("res/player/" + myfile))


def game_main(level_num):
    level = Level(level_num)
    level.load_level(level_num)


class Level:
    def __init__(self, num):
        self.x = 0  # Feld das links unten im Display angezeigt wird
        self.y = 0
        self.load_level(num)
        run()

    def load_level(self, num):
        gameDisplay.fill(GREEN)

        for i in range(DISPLAYWIDTH / BLOCKWIDTH):
            gameDisplay.blit(ground, (DISPLAYWIDTH / 2, DISPLAYHEIGHT / 3))
        pg.display.update()
        # clock.tick(50)

        Player(main.display_width / 2,
               main.display_height / 3)  # am Anfang soll Player nicht die position haben, sondern links anfangen
        print(left_walk)


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

    def move(self, direction):
        self.animation_count += 1
        if self.animation_count + 1 >= 4:  # da wir 5 Bilder pro Movement haben
            self.animation_count = 0

        if direction == 0:
            gameDisplay.blit(left_walk[self.animation_count], (self.x, self.y))
        elif direction == 1:
            gameDisplay.blit(right_walk[self.animation_count], (self.x, self.y))
        """
        elif direction == 2:
            gameDisplay.blit(up_walk[self.animation_count], (self.x, self.y))
        elif direction == 3:
            gameDisplay.blit(down_walk[self.animation_count], (self.x, self.y))
        """
        pg.display.update()

    def collide(self, X, Y):
        """
            returns if position has hit enemy
            - param x: int
            - para, y: int
            - return: boolean
        """
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False



class Enemy(Character):
    def __init__(self, x, y):
        super().__init__(x, y)

    def move(self):
        pass

    def draw(self, gameDisplay):
        """
           draws the enemy with the given images
           praram window: surfface
           return none
        """
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]
        if self.animation_count >= len(self.imgs):
            self.animation_count = 0
        gameDisplay.blit(self.img, (self.x, self.y))
        self.move()


def run():
    run = True

    while run:
        for event in pg.event.get():
            """
            if event.type == pg.Quit:
                run = False
                pg.QUIT()
            """
        # keyboard interactions
        if event.type == pg.KEYDOWN:
            # left
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                player.move(0)

            # right
            if event.key == pg.K_RIGHT or event.key == pg.K_d:
                player.move(1)

            # up
            if event.key == pg.K_UP or event.key == pg.K_w:
                player.move(2)

            # down
            if event.key == pg.K_DOWN or event.key == pg.K_s:
                player.move(3)

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_a:
                mv_left = False
            if event.key == pg.K_RIGHT or event.key == pg.K_d:
                mv_right = False
            if event.key == pg.K_UP or event.key == pg.K_w:
                mv_up = False
            if event.key == pg.K_DOWN or event.key == pg.K_s:
                mv_down = False





# aufruf aus menu

level_num = 1
game_main(level_num)
