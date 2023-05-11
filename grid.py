def printGrid(grid: list):
    print("    0  1  2  3  4  5  6  7  8  9")
    print("--------------------------------")
    cnt = 0
    for row in grid:
        print(cnt, end=' |')  # daje = index jer su = redovi; cnt needed
        for cell in row:
            if type(cell) == tuple:
                print(' O ', end='')
            else:
                print(f" {cell} ", end='')
        cnt += 1
        print()
    print()
