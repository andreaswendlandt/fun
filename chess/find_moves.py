#!/usr/bin/env python3
from chess_lib.figures import *

position = input('enter a position: ') 
chess_figure = input('enter a figure: ')
color = input('enter a color: ')
figure = eval(chess_figure)(color, position)
print(figure, figure.findMoves())
