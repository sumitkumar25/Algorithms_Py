class KnightTour:
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    def __init__(self, n=8, start=[0, 0]):
        super().__init__()
        self.n = 8
        self.board = [[-1 for i in range(n)] for i in range(n)]
        self.start = start

    def validCell(self, x, y):
        return x >= 0 and y >= 0 and x < self.n and y < self.n and self.board[x][y] == -1

    # returns True/False if path existes.
    def checkKnightPath(self):
        cell_sequence = 1
        self.board[0][0] = 1
        self.KnightTourPath(self.start[0], self.start[1], cell_sequence)
        for i in self.board:
            print(i)

    def KnightTourPath(self, x, y, cell_sequence):
        if cell_sequence == self.n ** 2:
            print("success")
            return True
        # check all possible moves from x,y
        for i in range(8):
            _x = x + self.move_x[i]
            _y = y + self.move_y[i]
            if self.validCell(_x, _y):
                # print(cell_sequence)
                self.board[_x][_y] = cell_sequence
                if self.KnightTourPath(_x, _y, cell_sequence + 1):
                    return True
                else:
                    self.board[x][y] = -1
        return False

# if move is false
# xy = -1
# else check move the piece.
# if all failed return false.


# instance = KnightTour()
# instance.checkKnightPath()
