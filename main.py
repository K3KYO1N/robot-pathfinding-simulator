from grid import Grid
from robot import Robot
from pathfinding.a_star import a_star_search
from visualization.logger import print_grid

def run_simulation():
    width, height = 10, 10
    obstacles = [(3, y) for y in range(1, 9)] + [(6, y) for y in range(2, 10)]
    start = (0, 0)
    goal = (9, 9)

    grid = Grid(width, height, obstacles)
    robot = Robot(grid, start, goal)

    path = a_star_search(grid, start, goal)
    robot.set_path(path[1:])  # skip starting point

    print("Initial Grid:")
    print_grid(grid, robot.position, goal)

    while robot.position != goal and robot.path:
        robot.move_step()
        print_grid(grid, robot.position, goal)

if __name__ == "__main__":
    run_simulation()
