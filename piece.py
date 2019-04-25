import numpy as np
PIECE_SIZE = 4

class Piece:
    def __init__(self, spec, n):
        self.playable_tiles = Piece._calculate_playable_tiles(spec)
        self.number = n

    def __repr__(self):
        return "Piece({})".format(self.number)

    @staticmethod
    def _calculate_playable_tiles(spec):
        piece_rotations = [np.rot90(np.array(spec), n).tolist() for n in range(4)]

        playable_tiles = []
        for piece in piece_rotations:
            for x in range(PIECE_SIZE):
                for y in range(PIECE_SIZE):
                    if piece[y][x] is None:
                        continue

                    has_empty_neighbour = (
                        (y+1 >= PIECE_SIZE or piece[y+1][x] is None)
                        or (y-1 < 0 or piece[y-1][x] is None)
                        or (x+1 >= PIECE_SIZE or piece[y][x+1] is None)
                        or (y-1 < 0 or piece[y][x-1] is None)
                    )

                    if has_empty_neighbour:
                        origin = (y, x)
                        relative_tiles = Piece._calculate_relative_tiles(origin, piece)
                        playable_tiles.append(relative_tiles)
        return playable_tiles

    @staticmethod
    def _calculate_relative_tiles(origin, piece):
        relative_tiles = []
        for x in range(PIECE_SIZE):
            for y in range(PIECE_SIZE):
                if piece[y][x] is None:
                    continue

                Y, X = origin
                relative_location = (y - Y, x - X)
                relative_tiles.append(relative_location)
        return relative_tiles


ZERO = [
    [0,    0,       0,      None],
    [0,    None,    0,      None],
    [0,    None,    0,      None],
    [0,    0,       0,      None],
]

ONE = [
    [None,    1,     1,     None],
    [None,    None,  1,     None],
    [None,    None,  1,     None],
    [None,    None,  1,     None],
]

TWO = [
    [None,  2,      2,      None],
    [None,  2,      2,      None],
    [2,     2,      None,   None],
    [2,     2,      2,      None],
]

THREE = [
    [3,     3,      3,      None],
    [None,  None,   3,      None],
    [None,  3,      3,      None],
    [3,     3,      3,      None],
]

FOUR = [
    [None,  4,      4,      None],
    [None,  4,      None,   None],
    [4,     4,      4,      None],
    [None,  4,      4,      None],
]


FIVE = [
    [5,     5,     5,       None],
    [5,     None,  None,    None],
    [5,     5,     5,       None],
    [5,     5,     5,       None],
]

SIX = [
    [6,     6,     None,    None],
    [6,     None,  None,    None],
    [6,     6,     6,       None],
    [6,     6,     6,       None],
]

SEVEN = [
    [7,     7,      7,      None],
    [None,  7,      None,   None],
    [7,     7,      None,   None],
    [7,     None,   None,   None],
]

EIGHT = [
    [None,  8,      8,      None],
    [None,  8,      8,      None],
    [8,     8,      None,   None],
    [8,     8,      None,   None],
]

NINE = [
    [9,     9,      9,      None],
    [9,     9,      9,      None],
    [9,     9,      None,   None],
    [9,     9,      None,   None],
]

PIECES = [
    ZERO,
    ONE,
    TWO,
    THREE,
    FOUR,
    FIVE,
    SIX,
    SEVEN,
    EIGHT,
    NINE,
]
