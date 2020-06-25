import random
import numpy as np

convert = ["💥", "🔳", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣"]


def setupgrid(gridsize, start, numberofmines):
    emptygrid = [[0 for i in range(gridsize)] for i in range(gridsize)]

    mines = getmines(emptygrid, start, numberofmines)

    for x in range(gridsize):
        for y in range(gridsize):
            if mines[x][y]:
                emptygrid[x][y] = -1

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
    size = len(grid)
    mines = np.zeros((size, size), dtype=np.bool)
    free_slots = list(zip(*np.where(~mines)))

    # Start
    free_slots.remove(start)
    for n in getneighbors(grid, *start):
        if n in free_slots:
            free_slots.remove(n)

    # Generation
    np.random.shuffle(free_slots)
    for _ in range(numberofmines):
        mines[free_slots.pop()] = True
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


def main(text, size=10, difficulty=4):
    numberofmines = size * difficulty

    start = (random.randint(0, size-1), random.randint(0, size-1))
    setup = setupgrid(gridsize=size, start=start, numberofmines=numberofmines)
    grid = printgrid(False, setup, start=start)
    solution = printgrid(True, setup)
    return text.replace("%size%", str(size))\
        .replace("%difficulty", str(difficulty))\
        .replace("%mines%", str(numberofmines))\
        .replace("%grid%", grid)\
        .replace("%solution%", solution)
