import random

convert = ["💥", "🔳", ":one:", ":two:", ":three:", ":four:", ":five:", ":six:", ":seven:", ":eight:"]


def setupgrid(gridsize, start, numberofmines):
    emptygrid = [[0 for i in range(gridsize)] for i in range(gridsize)]

    mines = getmines(emptygrid, start, numberofmines)

    for i, j in mines:
        emptygrid[i][j] = -1

    grid = getnumbers(emptygrid)

    return grid


def getrandomcell(grid):
    gridsize = len(grid)

    a = random.randint(0, gridsize - 1)
    b = random.randint(0, gridsize - 1)

    return a, b


def getneighbors(grid, rowno, colno):
    gridsize = len(grid)
    neighbors = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            elif -1 < (rowno + i) < gridsize and -1 < (colno + j) < gridsize:
                neighbors.append((rowno + i, colno + j))

    return neighbors


def getmines(grid, start, numberofmines):
    mines = []
    neighbors = getneighbors(grid, *start)

    for i in range(numberofmines):
        cell = getrandomcell(grid)
        while cell == start or cell in mines or cell in neighbors:
            cell = getrandomcell(grid)
        mines.append(cell)

    return mines


def getnumbers(grid):
    for rowno, row in enumerate(grid):
        for colno, cell in enumerate(row):
            if cell != -1:
                values = [grid[r][c] for r, c in getneighbors(grid, rowno, colno)]
                grid[rowno][colno] = values.count(-1)  # Counts how many are mines

    return grid


def printgrid(solution, grid, start=None):
    if start is None:
        start = (0, 0)
    size = len(grid)
    out = ""
    for x in range(0, size):
        for y in range(0, size):
            cell = grid[x][y]
            spoiler = "" if ((x == start[0] and y == start[1]) or solution) else "||"
            out += spoiler + convert[cell + 1] + spoiler
        out += "" if x == size - 1 else "\n"
    return out


def main(text, size=10, difficulty=-1):
    numberofmines = size * difficulty if difficulty != -1 else 4

    start = (random.randint(0, size), random.randint(0, size))
    setup = setupgrid(gridsize=size, start=start, numberofmines=numberofmines)
    grid = printgrid(False, setup, start=start)
    solution = printgrid(True, setup)
    return text.replace("%size%", str(size)).replace("%mines%", str(numberofmines)).replace("%grid%", grid).replace("%solution%", solution)