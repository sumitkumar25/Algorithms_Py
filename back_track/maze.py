class Maze:
    def __init__(self, maze, moves, start=[0, 0], end=[4, 3]):
        self.maze = maze
        self.start = start
        self.end = end
        self.move_x = moves['x']
        self.move_y = moves['y']
        self.traversed = 't'
        self.rows = len(self.maze) - 1
        self.columns = len(self.maze[0])-1
        super().__init__()

    def validMove(self, row, column):
        return row <= self.rows and column <= self.columns and self.maze[row][column] == 1

    def findMazePath(self):
        pos = 2
        self.maze[self.start[0]][self.start[1]] = self.traversed
        return self.traverseMaze(self.start[0], self.start[1], pos)

    def traverseMaze(self, x, y, pos):
        # maze solved
        if x == self.end[0] and y == self.end[1]:
            for i in self.maze:
                print(i)
            return True
        for move in range(len(self.move_x)):
            _x = x + self.move_x[move]
            _y = y + self.move_y[move]
            if self.validMove(_x, _y):
                self.maze[_x][_y] = self.traversed
                if self.traverseMaze(_x, _y, pos + 1):
                    return True
                else:
                    self.maze[_x][_y] = 1

        return False


maze = [[1, 1, 1, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 1]]
moves = {
    'x': [1, 0],
    'y': [0, 1]
}
instance = Maze(maze, moves)
print(instance.findMazePath())
