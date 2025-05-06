class Robot:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.position = start
        self.goal = goal
        self.path = []

    def set_path(self, path):
        self.path = path

    def move_step(self):
        if self.path:
            self.position = self.path.pop(0)
