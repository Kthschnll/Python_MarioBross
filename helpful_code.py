# Vorlage Kommentar

"""
	date:
	    - 25.05.2020
	desc:
	    - dieses skript ist beinahlten Sachen aus dem Unterrricht die für spätere Funktionen eventuell hilfreich sein können
	param:
        - nothing
    return:
        - nothing
	to_do:
	    - helpful_code  vor Abgabe löschen
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




# Datenbanken Stunde 02
# Datenverarbeitung mit Data Frames Stunde 03

var_1 = [] #array
var_2 = () #tuple: wenn ich mehrere parameter übergeben mochte arbeite ich mit nicht veränderliche liste
var_3 = {} #dictionary
dc_variable = {"mein_key":42, "mein_key2":[1,2,3,4, "test"]}

# import statistica as s -> dann überall statistics. durch s. ersetzen
# from statistics import mean -> wir wollen nur die Funktion mean importieren

# für highscore: write, append, read files # katha

meinText = 'hallo'
saveFile = open('test.txt', 'w') # w für write, alles andere was in der datei ist wird gelöscht
saveFile.write(meinText)
saveFile.close()

meinText = '\nnomon'
saveFile = open('test.txt', 'a') # a für append es wird der meintext an letzten buchstaben angehängt
saveFile.write(meinText)
saveFile.close()

readme = open("test.txt", "r").read()
print(readme)


    # text splitten
splitme = readme.split('o') #splittet an der stelle wo ein o oder z.B. \n steht, splitme ist ein array
print(splitme)
print(splitme[2])

    #lists operations
x = [2,3,4,5,2,6,71,2,3]
print (x)
x.append(4) # hintenanhängen
print(x)
x.insert(5,66) # an Pos [5] 66 einfügen
print(x)
x.remove(3) # pos[3] löschen
print(x)
print(x.index(4)) # [] wo 4 das erste mal
print(x.count(2)) # wie viele zweier
x.sort() #aufwärts sortieren
print(x)


    #dictionarys
# haben einen eindeutigen schlüssel
grade_test = {'Daniel': 89, 'Theo': [7,90], 'Jack':90}
print(grade_test)
print(grade_test['Daniel'])
print(grade_test['Theo'][1])
grade_test['Theo'][0] = 100 #wert ändern wenn theo (7,80) also ein tupel wäre es nicht möglich
grade_test['Daniel'] = 100 #wert ändern
grade_test['Jessica'] = 0 #neuen key anlegen
grade_test['Jessi'] = [0,90] #neuen key anlegen, ohne klammern wäre es ein tupel und somit nicht veränderbar
del grade_test['Jack'] #key mit wert löschen
print(grade_test)





## aus menu
class Player(Species):
    def __init__(self, player_rect, current_move, move_list, jump, skin, state, speed, health, level_num):
        super().__init__(player_rect, current_move, move_list, skin, state, speed, health)
        self.jump = jump
        self.level_array = get_level_array(level_num)

    def move(self):
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
                - todo Schleifen zählung nicht +1 sondern effizienter
        """
        if self.current_move == 1:
            for i in range(1, self.speed + 1):
                self.player_rect.x += 1
                collide = self.collide()
                if collide:
                    self.player_rect.x -= 1
                    break
        elif self.current_move == 2:
            for i in range(1, self.speed + 1):
                self.player_rect.x -= 1
                if self.player_rect.x <= 0:  # Linkes Bildschirm Ende
                    self.player_rect.x = 0
                collide = self.collide()
                if collide:
                    self.player_rect.x += 1
                    break

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
        max_x = DISPLAYWIDTH / 2 - BLOCKWIDTH  # relative Position von Player, damit Player in der Mitte des Display erscheint
        if self.player_rect.x < max_x:  # wenn die absolute Position von Player noch kleiner wie die relative ist
            max_x = self.player_rect.x  # Player ist noch nicht bis zur Mitte gelaufen; Anfang vom Level
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
                gameDisplay.blit(getattr(self.skin, self.move_list[self.current_move + 3])[1],
                                 (max_x, self.player_rect.y))
            else:
                gameDisplay.blit(getattr(self.skin, self.move_list[self.current_move + 3])[2],
                                 (max_x, self.player_rect.y))

    def collide(self):
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
                 - Bei end block ins Menü zurück oder Animation abspielen und Name eintragen wenn Highscore unter den besten 10
                 - Funktion bei Block 40 (Wasser)
                 - eventuell Reihenfolge ändern(effizienter, statt else alle nicht passierbaren Blöcke in Array und an Anfang
        """
        if self.current_move == 1:
            pos_player = self.player_rect.x + PLAYERWIDTH

        elif self.current_move == 2:
            pos_player = self.player_rect.x

        player_list = pos_player // BLOCKWIDTH  # in welcher Liste sich Player befindet
        player_element = self.player_rect.y // BLOCKHEIGHT

        block_value = self.level_array[player_list][player_element]
        # print(pos_player)
        # print(player_list, player_element, block_value)

        if block_value in DECORATION_BLOCK:
            return False
        elif block_value in POWERUP_BLOCK:
            self.collect_drink(block_value)
            self.level_array[player_list][player_element] = 74  # getränk wird gelöscht
            return False
        elif block_value in RARE_BLOCK:
            print("found rare item")
        elif block_value in ENEMY_SPAWN:
            print("new enemy")
            return False
        elif block_value == END_BLOCK:
            print("Ende")
            return True
        else:
            return True

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
            self = green_item.item_init(self)
        elif num == 57:
            self = red_item.item_init(self)
        elif num == 63:
            print("braun")
        elif num == 64:
            print("gelb")
            self = red_item.item_init(self)

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
                if event.key == pygame.K_UP:
                    if self.jump.is_jumping:
                        if not self.jump.cancle:
                            self.jump.cancle = True
                            self.state = 0
        return running


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

std_jump = Jump(False, 400, 0, 6,
                False)  # 400 steht für den basis X-Wert von Spieler...wenn der Spieler auf einen Block springt muss hier ein neuer wert eingetragen werden
high_jump = Jump(False, 400, 0, 8, False)  # für rotes Item



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
