from brod import Brod


def inputCoord() -> tuple[int, int]:
    while True:
        try:
            x = int(input("Unesi 'x' koordinatu: "))
            y = int(input("Unesi 'y' koordinatu: "))
            if x > -1 and x < 10 and y > -1 and y < 10:
                return x, y
        except ValueError:
            pass
        print("Koordinata mora biti broj 0-9")


def isTaken(brodovi: list, x: int, y: int) -> bool:
    for nekiBrod in brodovi:
        if (x, y) in nekiBrod.koordinate:
            print("Odabrana koordinata je vec zauzeta. Izaberi drugu\n")
            return True
    return False


def isInline(brod: Brod, x: int, y: int):
    if brod.koordinate:
        for koord in brod.koordinate:
            if koord[0] != x and koord[1] != y:
                print(
                    "Brodovi se moraju postavljati u okomitoj ili vodoravnoj liniji.\n")
                return False
    return True


def hasEnoughSize(brod: Brod, x: int, y: int):
    if brod.koordinate:
        for koord in brod.koordinate:
            if abs(koord[0] - x) >= brod.velicina or abs(koord[1] - y) >= brod.velicina:
                print(f"Ovaj brod zauzima samo {brod.velicina} mista.\n")
                return False
    return True


# izgleda dobro, fali ako nemoze stat vj.;  gleda samo izmedu
def isNotInCollision(grid: list, brod: Brod, x: int, y: int):
    # i tipa ako je prva koordinata da ga ne uvalis utisno
    minCoord, maxCoord = (9, 9), (0, 0)
    if brod.koordinate:
        koordsCopyPlus = brod.koordinate.copy()
        koordsCopyPlus.append((x, y))
        minCoord = min(koordsCopyPlus)
        maxCoord = max(koordsCopyPlus)

        minX, minY = minCoord[0], minCoord[1]
        maxX, maxY = maxCoord[0], maxCoord[1]
        if minX == maxX:
            for i in range(minY + 1, maxY):
                if type(grid[minX][i]) != tuple and (minX, i) not in brod.koordinate:
                    print("Brodovi se ne mogu preklapati, unesi drugu koordinatu.\n")
                    return False
        else:
            for i in range(minX + 1, maxX):
                if type(grid[i][minY]) != tuple and (i, minY) not in brod.koordinate:
                    print("Brodovi se ne mogu preklapati, unesi drugu koordinatu.\n")
                    return False
    return True


def hasSpace(grid: list, brod: Brod, x: int, y: int):
    left, right, up, down = 0, 0, 0, 0
    lFlag, rFlag, uFlag, dFlag = True, True, True, True
    for i in range(1, brod.velicina):
        if y + i < 10 and type(grid[x][y + i]) == tuple and rFlag:
            right += 1
        else:
            rFlag = False
        if y - i > -1 and type(grid[x][y - i]) == tuple and lFlag:
            left += 1
        else:
            lFlag = False
        if x + i < 10 and type(grid[x + i][y]) == tuple and dFlag:
            down += 1
        else:
            dFlag = False
        if x - i > -1 and type(grid[x - i][y]) == tuple and uFlag:
            up += 1
        else:
            uFlag = False

        if not (rFlag or lFlag or uFlag or dFlag): # untested
            break

    if (left + right) >= (brod.velicina - 1) or (up + down) >= (brod.velicina - 1):
        return True
    print("Nema dovoljno mista za brod. Unesi drugu koordinatu.\n")
    return False
