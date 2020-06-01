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


















