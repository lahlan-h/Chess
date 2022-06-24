from pathlib import Path
from setuptools import setup

APP = ['main.py']

DATA_FILES = ['gameManager.py', 'calculateMoves.py', "blackbishop.png", 
"whitebishop.png", "blackrook.png", 
"whiterook.png", "blackqueen.png", 
"whitequeen.png", "blackpawn.png", 
"whitepawn.png", "blackknight.png", 
"whiteknight.png", "blackking.png", 
"whiteking.png", "Icon.png","move_piece.wav"]

#'testIcon.png','drawBoard.py'
OPTIONS = {
 'argv_emulation': True,
 'iconfile':'Icon.png'
}

 #'packages': ['certifi'],
 
setup(
    name="Chess",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)