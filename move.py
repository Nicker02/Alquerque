from dataclasses import dataclass
@dataclass
class Move:
    src: int
    trg: int

def make_move(src:int, trg:int)-> Move:
    return Move(src,trg)

def source(m:Move) -> int:
    return m.src

def target(m:Move) -> int:
    return m.trg
# make_move(1,2)
# print(source(make_move()))

