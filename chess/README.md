# Chess

## find_moves.py

printing out all possible moves for a given figure on a given position

### example
calling the script
```
./find_moves.py
```
enter the position of your figure
(possible values: [abcdefgh][12345678])
```
enter a position: e4
```
enter the figure you want to get to know the possible moves from
(possible values: Knight, Bishop, Rook, Queen, King, Pawn)
```
enter a figure: Queen
```
and last but not least enter the color of your figure
(possible values: white|black)
```
enter a color: white
```
you get all possible positions your figure could move to:
```
white Queen @e4 possible moves: a4 a8 b4 e1 b1 b7 c4 e2 c2 c6 d4 e3 d3 d5 f4 e5 f5 f3 g4 e6 g6 g2 h4 e7 h7 h1 e8
```
and an example for a black knight at d5
```
enter a position: d5
enter a figure: Knight
enter a color: black
black Knight @d5 possible moves: e7 f6 c7 b6 e3 f4 c3 b4
```
