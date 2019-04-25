import itertools

BOARD_SIZE = 20
ORIGIN = (0, int(BOARD_SIZE / 2), int(BOARD_SIZE / 2))
LEVELS = 6

# Board Rep.:
#   board[z][y][x]
#   score (int)

class Board:
    def __init__(self, prev_board=None):
        if prev_board is not None:
            # deepcopy
            self.board = [[[prev_board.board[z][y][x] for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)] for z in range(LEVELS)]
            self.score = prev_board.score
        else:
            self.board = [[[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)] for _ in range(LEVELS)]
            self.score = 0

    def __repr__(self):
        return "\n".join(" ".join(["-" if i is None else str(i) for i in r]) for r in self.board[0])

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
                (y+1 < BOARD_SIZE and self.board[z][y+1][x] is not None)
                or (y-1 >= 0 and self.board[z][y-1][x] is not None)
                or (x+1 < BOARD_SIZE and self.board[z][y][x+1] is not None)
                or (x-1 >= 0 and self.board[z][y][x-1] is not None)
            )
            if not has_neighbour:
                continue

            playable_tiles.append((z, y, x))

        return playable_tiles

    def is_valid_location(self, coords):
        z, y, x = coords
        return self.board[z][y][x] is None

    def is_piece_play_valid(self, play_location, relative_locations):
        (Z, Y, X) = play_location
        if self.board[Z][Y][X] is not None:
            return False

        covering_numbers = set()
        for relative_location in relative_locations:
            y, x = relative_location
            if (Y+y >= BOARD_SIZE) or (Y+y < 0) or (X+x >= BOARD_SIZE) or (X+x < 0):
                return False

            if self.board[Z][Y+y][X+x] is not None:
                return False

            if (Z != 0) and (self.board[Z-1][Y+y][X+x] is None):
                return False

            if Z != 0:
                covering_numbers.add(self.board[Z-1][Y+y][X+x])



        if (Z != 0) and (len(covering_numbers) == 1):
            return False

        return True

    def play_piece(self, play_location, relative_locations, number):
        # print("Playing {} at {}".format(number, play_location))
        (Z, Y, X) = play_location
        for relative_location in relative_locations:
            y, x = relative_location
            self.board[Z][Y+y][X+x] = number
        # print(self)
        self.score += Z * number
