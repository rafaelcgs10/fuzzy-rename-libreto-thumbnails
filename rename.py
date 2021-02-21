import os
import sys
import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re

games = []

with open('games_list.txt') as f:
  games_list = f.readlines()

for game in games_list:
  game_clean = re.sub('\n', '', game)
  games.append(game_clean)

directory = os.path.dirname(os.path.realpath(sys.argv[0]))

def rename(full_filename, current_directory, count):
  filename, file_extension = os.path.splitext(full_filename)

  highest = process.extractOne(filename, games)

  if highest[1] == 100:
    return
  if highest[1] >= 90:
    subdirectory_path = os.path.relpath(subdir, current_directory)

    file_path_old = os.path.join(subdirectory_path, full_filename)

    new_file_name = highest[0] + file_extension
    file_path_new = os.path.join(subdirectory_path, new_file_name)

    map_to_rename[file_path_old] = file_path_new
    array_to_rename.append(file_path_old)
    print(count, ") ", file_path_old , "------>", map_to_rename[file_path_old], "score:", highest[1])
    count = count + 1
  return count

blacklist_folders = ['.mypy_cache', '.git']
blacklist_files = ['rename.py', 'spyder.py', 'games_list.txt', 'requirements.txt', '.gitignore']

map_to_rename = {}
array_to_rename = []

count = 0

for subdir, dirs, files in os.walk(directory):
  contains = False
  for blacklist_folder in blacklist_folders:
    if blacklist_folder in subdir:
      contains = True
  if contains:
    continue
  for directory in dirs:
    if directory in blacklist_folders:
      continue
    count = rename(directory, subdir, count)
  for full_filename in files:
    if full_filename in blacklist_files:
      continue
    count = rename(full_filename, subdir, count)

if array_to_rename:
  print("Please enter the numbers separeted by spaces of the renames that you wish to skip! Or enter -1 to rename nothing. Or just hit enter to apply all renames.")
  skips = input()

if array_to_rename and skips == '-1':
  exit()

if array_to_rename and skips:
  for skip in skips.split(' '):
    i = int(skip)
    key = array_to_rename[i]
    map_to_rename.pop(key)

for key in map_to_rename:
  os.rename(key, map_to_rename[key])
