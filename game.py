import os
from os import listdir
from os.path import isfile, join

# player preparation
left_walk = []
right_walk = []
jump_walk = []  # sprung
idle_walk = []  # idle

resources_path_player = "res/player/"
only_files = [files for files in listdir(resources_path_player) if isfile(join(resources_path_player, files))]



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

















