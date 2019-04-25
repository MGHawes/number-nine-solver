import itertools

BOARD_SIZE = 16
LEVELS = 10

# Board Rep.:
#   board[z][y][x]
#   score (int)

class Board:
    def __init__(self, prev_board=None):
        if prev_board is not None:
            # deepcopy
            self.board = [[[prev_board[z][y][x] for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)] for z in range(LEVELS)]
            self.score = prev_board.score
        else:
            self.board = [[[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] for _ in range(LEVELS)]
            self.score = 0

    def get_playable_tiles(self):
        playable_tiles = []
        for (z, x, y) in itertools.product(range(LEVELS), range(BOARD_SIZE), range(BOARD_SIZE)):
            is_unoccupied = self.board[z][y][x] is not None
            if not is_unoccupied:
                continue

            has_tile_beneath = (z == 0) or (self.board[z-1][y][x] is not None)
            if not has_tile_beneath:
                continue

            has_neighbour = (
                self.board[z][y+1][x] is not None
                or self.board[z][y-1][x] is not None
                or self.board[z][y][x+1] is not None
                or self.board[z][y][x-1] is not None
            )
            if not has_neighbour:
                continue

            playable_tiles.append((z, x, y))

        return playable_tiles