# gomoku

Basic implementation of min-max algorithm to create a Gomoku ai.
To compile on windows, you will have to have pip installed on your computer and python 3.6 or 3.7.

to compile :
$    pip install pyinstaller
$    pyinstaller gomoku.py check_win.py score.py tree_minmax.py --name pbrain-antoine-carlier.exe --onefile

Then the executable will be available in dist folder.
