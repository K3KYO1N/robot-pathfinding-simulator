class Grid:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = set(obstacles)

    def in_bounds(self, pos):
        (x, y) = pos
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, pos):
        return pos not in self.obstacles

    def neighbors(self, pos):
        (x, y) = pos
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        neighbors = filter(self.in_bounds, neighbors)
        neighbors = filter(self.passable, neighbors)
        return list(neighbors)
