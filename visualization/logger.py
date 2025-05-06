def print_grid(grid, robot_pos, goal):
    for y in range(grid.height):
        for x in range(grid.width):
            if (x, y) == robot_pos:
                print("R", end=" ")
            elif (x, y) == goal:
                print("G", end=" ")
            elif (x, y) in grid.obstacles:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
    print()
