import os
import sys
import csv
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re

games = []

with open(sys.argv[1]) as f:
  games_list = f.readlines()

for game in games_list:
  game_clean = re.sub('\n', '', game)
  games.append(game_clean)

directory = os.path.dirname(os.path.realpath(sys.argv[0]))

def rename(name, file_extension, subdirectory_path, count):
  highest = process.extractOne(name, games)

  if highest[1] == 100:
    return count
  if highest[1] >= 90:
    full_filename = name + file_extension
    file_path_old = os.path.join(subdirectory_path, full_filename)

    new_file_name = highest[0] + file_extension
    file_path_new = os.path.join(subdirectory_path, new_file_name)

    map_to_rename[file_path_old] = file_path_new
    array_to_rename.append(file_path_old)
    print(count, ") ", file_path_old , "------>", map_to_rename[file_path_old])
    count = count + 1
  return count

blacklist_folders = ['.mypy_cache', '.git', 'games_list']
blacklist_files = ['rename.py', 'spyder.py', 'requirements.txt', '.gitignore', 'README.md']

# FIXME: extract the code bellow to functions

# RENAMING FOLDERS HERE

print("First we will rename folders, then second we will rename files\n")
print("Checking folders to rename\n")

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
  for dirr in dirs:
    if dirr in blacklist_folders:
      continue
    count = rename(dirr, "", subdir, count)

if array_to_rename:
  skips = input("Please enter the numbers separeted by spaces of the renames that you wish to skip! Or enter -1 to rename nothing. Or just hit enter to apply all renames.\n")

if array_to_rename and skips == '-1':
  exit()

if array_to_rename and skips:
  for skip in skips.split(' '):
    i = int(skip)
    key = array_to_rename[i]
    map_to_rename.pop(key)

for key in map_to_rename:
  os.rename(key, map_to_rename[key])
#
# RENAMING FILES HERE

print("Checking files to rename\n")

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
  for full_filename in files:
    if full_filename in blacklist_files:
      continue
    filename, file_extension = os.path.splitext(full_filename)
    count = rename(filename, file_extension, subdir, count)

if array_to_rename:
  skips = input("Please enter the numbers separeted by spaces of the renames that you wish to skip! Or enter -1 to rename nothing. Or just hit enter to apply all renames.\n")

if array_to_rename and skips == '-1':
  exit()

if array_to_rename and skips:
  for skip in skips.split(' '):
    i = int(skip)
    key = array_to_rename[i]
    map_to_rename.pop(key)

for key in map_to_rename:
  os.rename(key, map_to_rename[key])
