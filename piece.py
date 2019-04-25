PIECE_WIDTH = 3
PIECE_HEIGHT = 4

ZERO = [
    [0,    0,       0],
    [0,    None,    0],
    [0,    None,    0],
    [0,    0,       0],
]

ONE = [
    [None,    1,     1],
    [None,    None,  1],
    [None,    None,  1],
    [None,    None,  1],
]

TWO = [
    [None,  2,  2],
    [None,  2,  2],
    [2,     2,  None],
    [2,     2,  2],
]

THREE = [
    [3,     3,      3],
    [None,  None,   3],
    [None,  3,      3],
    [3,     3,      3],
]

FOUR = [
    [None,  4,  4],
    [None,  4,  None],
    [4,     4,  4],
    [None,  4,  4],
]


FIVE = [
    [5,  5,     5],
    [5,  None,  None],
    [5,  5,     5],
    [5,  5,     5],
]

SIX = [
    [6,  6,     None],
    [6,  None,  None],
    [6,  6,     6],
    [6,  6,     6],
]

SEVEN = [
    [7,     7,      7],
    [None,  7,      None],
    [7,     7,      None],
    [7,     None,   None],
]

EIGHT = [
    [None,  8,  8],
    [None,  8,  8],
    [8,     8,  None],
    [8,     8,  None],
]

NINE = [
    [9,  9,  9],
    [9,  9,  9],
    [9,  9,  None],
    [9,  9,  None],
]

class Piece:
    def __init__(self):
