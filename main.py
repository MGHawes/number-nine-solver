import itertools
from piece import PIECES, Piece
from board import Board, ORIGIN

PIECES = [Piece(p) for p in PIECES]
PLAY_ORDERS = itertools.permutations(PIECES)

best_score = 0
best_board = None

for piece_order in PLAY_ORDERS:
    board = Board()
    for (turn, piece) in enumerate(piece_order):
        if turn == 0:
