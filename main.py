import itertools
from piece import PIECES, Piece
from board import Board, ORIGIN
import cProfile

numbered_pieces = [Piece(p, n) for n, p in enumerate(PIECES)]
PLAY_ORDERS = [list(p) for p in itertools.permutations(numbered_pieces)]

best_score = 0
best_board = None

def solve(play_order=None):
    if play_order is not None:
        play_orders = [PLAY_ORDERS[play_order]]
    else:
        play_orders = PLAY_ORDERS

    for (i, numbered_piece_order) in enumerate(play_orders):
        print(numbered_piece_order)
        board = Board()
        piece = numbered_piece_order[0]

        board.play_piece(ORIGIN, piece.playable_tiles[0], piece.number)
        play_remaining(numbered_piece_order[1:], board)

def play_remaining(numbered_piece_order, old_board):
    # print(old_board)
    global best_score
    global best_board
    if len(numbered_piece_order) == 0:
        if old_board.score > best_score:
            print(old_board.score)
            print(old_board)
            best_score = old_board.score
            best_board = old_board
        return

    piece = numbered_piece_order[0]

    playable_locations = old_board.get_playable_tiles()
    board_outcomes = set()
    for playable_location in playable_locations:
        for possible_play in piece.playable_tiles:
            if old_board.is_piece_play_valid(playable_location, possible_play):
                new_board = Board(old_board)
                new_board.play_piece(playable_location, possible_play, piece.number)
                board_outcomes.add(new_board)
    for board_outcome in board_outcomes:
        play_remaining(numbered_piece_order[1:], board_outcome)


solve()
# cProfile.run('solve(0)')