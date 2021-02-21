# Fuzzy Rename Libreto Thumbnails
This a small collection of Python scripts to rename your games based on file names for the box arts in the Libreto repository.


All you have to do is run

```
python rename.py games_list/Nintendo\ -\ GameCube.txt
```

with these files in the games folder.

Don't forget to give the `.txt` file of which console you are renaming.

This script works recursively in the directory tree.

Don't worry, the script will prompt a question before start renaming files.

To update the `games_list` folder run:

```
scrapy runspider spyder.py
```
