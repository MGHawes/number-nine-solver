import itertools
from piece import PIECES, Piece
from board import Board, ORIGIN

numbered_pieces = [Piece(p, n) for n, p in enumerate(PIECES)]
PLAY_ORDERS = [list(p) for p in itertools.permutations(numbered_pieces)]

best_score = 0
best_board = None

def solve():
    for (i, numbered_piece_order) in enumerate(PLAY_ORDERS):
        board = Board()
        piece = numbered_piece_order[0]

        board.play_piece(ORIGIN, piece.playable_tiles[0], piece.number)
        play_remaining(numbered_piece_order[1:], board)

def play_remaining(numbered_piece_order, old_board):
    global best_score
    global best_board
    if len(numbered_piece_order) == 0:
        if old_board.score > best_score:
            best_score = old_board.score
            best_board = old_board
        return

    piece = numbered_piece_order[0]

    playable_locations = old_board.get_playable_tiles()
    for playable_location in playable_locations:
        for possible_play in piece.playable_tiles:
            if old_board.is_piece_play_valid(playable_location, possible_play):
                new_board = Board(old_board)
                new_board.play_piece(playable_location, possible_play, piece.number)
                play_remaining(numbered_piece_order[1:], new_board)


solve()
