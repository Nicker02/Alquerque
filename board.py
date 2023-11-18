from dataclasses import dataclass
from move import*

@dataclass
class Board:
    white: list[int]
    black: list[int]
    empty: list[int]

def make_board (white:list,black:list,empty:list) -> Board:
    return Board(white,black,empty)

def white_plays(b:Board) -> bool:
    return True

def white(b:Board) -> list[int]:
    return b.white

def black(b:Board) -> list[int]:
    return b.black

def empty(b:Board) -> list[int]:
    return b.empty

def is_legal(m:Move,b:Board) -> bool:
    if white_plays(b):
        if m.trg in b.empty:
            if m.src % 2 == 0:
                diff = m.src - m.trg
                if diff == 5:
                    return True
                else:
                    return False
            elif m.src % 2 == 1:
                diff = m.src - m.trg
                if 6 >= diff >= 4:
                    return True
                elif (diff-difference in b.black for difference in [5,4,-1]):
                    return True
                else:
                    return False
        elif m.trg in b.black:
            if m.src % 2 == 1:
                diff = m.src - m.trg
                if diff == 8:
                    return True
                elif diff == 10:
                    return True
                elif diff == 12:
                    return True
                else:
                    return False
            elif m.src % 2 == 0:
                diff = m.src - m.trg
                if diff == 10:
                    return True
                else:
                    return False
    else:
        if m.trg in b.empty:
            if m.src % 2 == 0:
                diff = m.trg - m.src
                if diff == 5:
                    return True
                else:
                    return False
            elif m.src % 2 == 1:
                diff = m.trg- m.src
                if 6>= diff >= 4:
                    return True
                else:
                    return False
        elif m.trg//2 in b.white:
            if m.src % 2 == 1:
                diff = m.trg - m.src
                if diff == 8:
                    return True
                elif diff == 10:
                    return True
                elif diff == 12:
                    return True
                else:
                    return False
            elif m.src % 2 == 0:
                diff = m.trg - m.src
                if diff == 10:
                    return True
                else:
                    return False
        else:
            return False
def legal_moves(b:Board) -> list[Move]: 
     legalmoves = []
     for src in b.white:
         for trg in b.empty:
             m = Move(src,trg)
             if is_legal(m,b):
                 legalmoves.append(m)
     return legalmoves

#def legal_move(b:Board) -> list[Move]:
k = Move(13,3)
j = Board([13],[1,2,3,4,9,10,11,12],[7,8,5])
#print(23-13)
# print(target(k))
# print(is_legal(k,j))
print(legal_moves(j))
#print(white(make_board([1,2,3],[4,5,6,7],8))[2])
#print(black(make_board([1,2,3],[4,5,6,7],8))[3])
#print(empty(make_board([1,2,3],[4,5,6,7],8)))



