# Fuzzy Rename Libreto Thumbnails
This a small collection of Python scripts to rename your games based on file names for the box arts in the Libreto repository.


All you have to do is run

```
python rename.py games_lists/Nintendo\ -\ GameCube.txt
```

with these files in the games folder.

Don't forget to give the `.txt` file of which console you are renaming.

This script works recursively in the directory tree.

Don't worry, the script will prompt a question before start renaming files.

To update the `games_lists` folder run:

```
scrapy runspider spyder.py
```

## On the Windows version

Yes, you can easily run this on Window!

Just go to the [releases](https://github.com/rafaelcgs10/fuzzy-rename-libreto-thumbnails/releases) section and download the last Windows build.

To run in Windows all you have to do is to extract the zip file and copy all its content to the folder where your roms are, then just run de binary.
Remember, this program scans everything recursively, so to avoid long scans put this in a directory that doesn't have too many sub-directories.

The Windows build is made using pyinstaller. That is why the binary is so fat.
