#!/usr/bin/env python3
from typing import List

# base class
class Figure():
    col: int
    row: int

    def __init__(self, color: str, pos: str):
        self.color = color
        allowed_colors = ["white", "black"]
        if self.color not in allowed_colors:
            raise ValueError('invalid color ' + self.color + ' ...valid colors white|black')
        if len(pos) != 2: 
            raise ValueError('invalid notation, ...valid notation for example a3, e5')
        c = pos[0].lower()
        r = pos[1]
        if (not c in 'abcdefgh') or (not r in '12345678'):
            raise ValueError('invalid position - valid positions [a-h][1-8]')
        self.col = 'abcdefgh'.find(c)
        self.row = '12345678'.find(r)
        
    def __str__(self):
        return Figure.position(self.col, self.row)
        
    @staticmethod
    def position(col: int, row: int) -> str:
        if row<0 or row>7 or col<0 or col>7:
          return ''
        return 'abcdefgh'[col] + '12345678'[row]

# class for knight
class Knight(Figure):
    def __init__(self, color: str, pos: str):
        super().__init__(color, pos)
  
    def __str__(self):
        return self.color + ' Knight @' + Figure.position(self.col, self.row)

    def findMoves(self) -> List[str]:
        offsets = [(1,2),  (2,1),  (-1,2),  (-2,1),
                   (1,-2), (2,-1), (-1,-2), (-2,-1)]
        positions = []
        for (coff,roff) in offsets:
            newpos = Figure.position(self.col + coff, self.row + roff)
            if newpos:
                positions += [newpos]
        moves = ' '.join(positions)
        return 'possible moves: ' + moves

# class for bishop
class Bishop(Figure):
    def __init__(self, color: str, pos: str):
        super().__init__(color, pos)
  
    def __str__(self):
        return self.color + ' Bishop @' + Figure.position(self.col, self.row)

    def findMoves(self) -> List[str]:
        positions = []
        for i in range(-7, 8):
            if i==0: 
                continue
            # diagonal from left bottom to right top
            newpos = Figure.position(self.col + i, self.row + i)
            if newpos:
                positions += [newpos]
            # diagonal from right bottom to left top
            newpos = Figure.position(self.col + i, self.row - i)
            if newpos:
                positions += [newpos]
        moves = ' '.join(positions)
        return 'possible moves: ' + moves

# class for rook
class Rook(Figure):
    def __init__(self, color: str, pos: str):
        super().__init__(color, pos)
  
    def __str__(self):
        return self.color + ' Rook @' + Figure.position(self.col, self.row)

    def findMoves(self) -> List[str]:
        positions = []
        for i in range(-7, 8):
            if i==0: 
                continue
            # from left to right
            newpos = Figure.position(self.col + i, self.row)
            if newpos:
                positions += [newpos]
            # from bottom to top
            newpos = Figure.position(self.col, self.row + i)
            if newpos:
                positions += [newpos]
        moves = ' '.join(positions)
        return 'possible moves: ' + moves

# class for queen
class Queen(Figure):
    def __init__(self, color: str, pos: str):
        super().__init__(color, pos)
  
    def __str__(self):
        return self.color + ' Queen @' + Figure.position(self.col, self.row)

    def findMoves(self) -> List[str]:
        positions = []
        for i in range(-7, 8):
            if i==0: continue
            # from left to right
            newpos = Figure.position(self.col + i, self.row)
            if newpos:
                positions += [newpos]
            # from bottom to top
            newpos = Figure.position(self.col, self.row + i)
            if newpos:
                positions += [newpos]
            # diagonal from left bottom to right top
            newpos = Figure.position(self.col + i, self.row + i)
            if newpos: 
                positions += [newpos]
            # diagonal from right bottom to left top
            newpos = Figure.position(self.col + i, self.row - i)
            if newpos: 
                positions += [newpos]
        moves = ' '.join(positions)
        return 'possible moves: ' + moves

# class for king
class King(Figure):
    def __init__(self, color: str, pos: str):
        super().__init__(color, pos)

    def __str__(self):
        return self.color + ' King @' + Figure.position(self.col, self.row)

    def findMoves(self) -> List[str]:
        positions = []
        for i in range(-1, 2):
            if i==0:
                continue
            # from left to right
            newpos = Figure.position(self.col + i, self.row)
            if newpos:
                positions += [newpos]
            # from bottom to top
            newpos = Figure.position(self.col, self.row + i)
            if newpos:
                positions += [newpos]
            # diagonal from left bottom to right top
            newpos = Figure.position(self.col + i, self.row + i)
            if newpos:
                positions += [newpos]
            # diagonal from right bottom to left top
            newpos = Figure.position(self.col + i, self.row - i)
            if newpos: 
                positions += [newpos]
        moves = ' '.join(positions)
        return 'possible moves: ' + moves

# class for pawn
class Pawn(Figure):
    def __init__(self, color: str, pos: str):
        self.color = color
        super().__init__(color, pos)

    def __str__(self):
        return self.color + ' Pawn @' + Figure.position(self.col, self.row)

    def findMoves(self) -> List[str]:
        positions = []
        pos = Figure.position(self.col, self.row)
        row = pos[1]
        if row == '2' or row == '7':
            step = 3
        else:
            step = 2

        if self.color == 'white':
            for i in range(step):
                if i==0:
                    continue
                # from bottom to top
                newpos = Figure.position(self.col, self.row + i)
                if newpos:
                    positions += [newpos]
                    moves = ' '.join(positions)
        elif self.color == 'black':
            for i in range(step):
                if i==0:
                    continue
                # from top to bottom
                newpos = Figure.position(self.col, self.row -i)
                if newpos: 
                    positions += [newpos]
        moves = ' '.join(positions)
        return 'possible moves: ' + moves
