def dfs_r(maze, i, j):
    maze.animate()

    maze._cells[i][j]._visited = True
    # check for end
    if i == maze.num_cols - 1 and j == maze.num_rows - 1:
        return True
    # try each direction
    # left
    if (
        i > 0
        and not maze._cells[i - 1][j]._visited
        and not maze._cells[i][j].has_left_wall
    ):
        maze._cells[i][j].draw_move(maze._cells[i - 1][j])
        if dfs_r(maze, i - 1, j):
            return True
        else:
            maze._cells[i][j].draw_move(maze._cells[i - 1][j], True)

    # right
    if (
        i < maze.num_cols - 1
        and not maze._cells[i][j].has_right_wall
        and not maze._cells[i + 1][j]._visited
    ):
        maze._cells[i][j].draw_move(maze._cells[i + 1][j])
        if dfs_r(maze, i + 1, j):
            return True
        else:
            maze._cells[i][j].draw_move(maze._cells[i + 1][j], True)

    # up
    if (
        j > 0
        and not maze._cells[i][j - 1]._visited
        and not maze._cells[i][j].has_top_wall
    ):
        maze._cells[i][j].draw_move(maze._cells[i][j - 1])
        if dfs_r(maze, i, j - 1):
            return True
        else:
            maze._cells[i][j].draw_move(maze._cells[i][j - 1], True)

    # down
    if (
        j < maze.num_rows - 1
        and not maze._cells[i][j + 1]._visited
        and not maze._cells[i][j].has_bottom_wall
    ):
        maze._cells[i][j].draw_move(maze._cells[i][j + 1])
        if dfs_r(maze, i, j + 1):
            return True
        else:
            maze._cells[i][j].draw_move(maze._cells[i][j + 1], True)

    return False


def bfs(maze, i, j):
    to_visit = []
    to_visit.append(maze._cells[i][j])
    maze._cells[i][j].visited = True
    while to_visit:
        neighbors = []  # intialize list of neighbors
        visited_cell = to_visit.pop(0)  # visit first cell

        if visited_cell == maze._cells[-1][-1]:  # check for end
            return True
        visited_cell.visited = True  # mark cell as visited if not end

        # left neighbor

        if i > 0 and not maze._cells[i][j].has_left_wall:
            neighbors.append(maze._cells[i - 1][j])

        # right neighbor
        if i < maze.__num_cols - 1 and not maze._cells[i][j].has_right_wall:
            neighbors.append(maze._cells[i + 1][j])
        # up neighbor
        if j > 0 and not maze._cells[i][j].has_top_wall:
            neighbors.append(maze._cells[i][j - 1])
        # down neighbor
        if j < maze.__num_rows - 1 and not maze._cells[i][j].has_bottom_wall:
            neighbors.append(maze._cells[i][j + 1])

        for neighbor in neighbors:
            if not neighbor.visited and neighbor not in to_visit:
                visited_cell.draw_move(neighbor)
                to_visit.append(neighbor)
    return False
