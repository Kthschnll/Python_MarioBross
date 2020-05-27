# display constants from game
DISPLAYWIDTH = 1000
DISPLAYHEIGHT = 600
BLOCKWIDTH = 50
BLOCKHEIGHT = 50
NORMAL_GROUND = (DISPLAYHEIGHT // 3) * 2

level_length = 10
y = DISPLAYHEIGHT // BLOCKHEIGHT  # 12
x = (DISPLAYWIDTH // BLOCKWIDTH) * level_length  # 20

# level_array ist Liste, in dieser sind: x*level_lenght Listen von der jede y Werte hat
# Array mit Nullen befüllen
level_array = [[0 for i in range(y)] for j in range(x)]


def get_level_array(level):
    """
     	date:
     	    - 27.05.2020
     	desc:
     	    - es wird Level erstellt
     	param:
             - level_num: Level Nummer, Auswahl geschieht im Menü
         return:
             - level_array
     	todo:
     	    - display constants nicht neu erstellen
     	    - level komplett erstellen
    """
    if level == 1:
        # einzelne Werte in Array eingeben
        # [Liste][Element]
        for i in range(0, 100):
            level_array[i][NORMAL_GROUND // BLOCKHEIGHT] = 1  # 1 = normal ground
            level_array[19][NORMAL_GROUND // BLOCKHEIGHT] = 1
    else:
        printf("Level noch nicht erstellt")
    return level_array
