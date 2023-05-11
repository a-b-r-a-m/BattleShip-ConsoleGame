from brod import Brod
from grid import printGrid
from validate import *


def setBoat(grid: list, brodovi: list, brod: Brod):

    n = brod.velicina
    while n != 0:
        print(
            f"Unesi koordinate za brod '{brod.klasa}' veličine ({brod.velicina}), još {n} polja.")
        printGrid(grid)
        x, y = inputCoord()
        print() # poslat n umisto velicine #############################################
        if n == brod.velicina:  # nije dovoljno, ti ga pustis, moze ic samo u jednon smjeru, a dopusti i u drugon .. vratit TUPLE
            if not hasSpace(grid, brod, x, y):
                continue
        if not isTaken(brodovi, x, y) and isInline(brod, x, y) and hasEnoughSize(brod, x, y) and isNotInCollision(grid, brod, x, y):
            brod.koordinate.append((x, y))
            n -= 1
            grid[x][y] = 'X'


grid = [[(x, y) for y in range(10)] for x in range(10)]
# grid = [(x, y) for y in range(10) for x in range(10)]
# grid = [[y for y in range(10)] for x in range(10)]
brodovi = [Brod('jadrolinija', 6),
           Brod('jedrenjak', 4), Brod('jedrenjak', 4),
           Brod('istranka', 3), Brod('istranka', 3), Brod('istranka', 3),
           Brod('kaic', 2), Brod('kaic', 2), Brod('kaic', 2), Brod('kaic', 2)
           ]

for brod in brodovi:
    setBoat(grid, brodovi, brod)
printGrid(grid)
