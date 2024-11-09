import random


class Grid:
    def __init__(self, size: int, obj: object):
        self.matrix = [[obj for x in range(size)] for y in range(size)]

    def show(self) -> None:
        for i in self.matrix:
            for j in i:
                print(j, end=" ")
            print()
        print('\n')


class Island(Grid):
    def __init__(self, size: int, obj: object):
        super().__init__(size, obj)
        for i in range(size):
            for j in range(size):
                self.matrix[i][j] = random.randint(0, 1)


def depth_first_search(islands: Island, row: int, col: int, visited: Grid):
    if row < 0 or col < 0 \
            or row >= len(islands.matrix) or col >= len(islands.matrix) \
            or visited.matrix[row][col] or islands.matrix[row][col] == 0:
        return
    visited.matrix[row][col] = True
    depth_first_search(islands, row, col - 1, visited)
    depth_first_search(islands, row - 1, col, visited)
    depth_first_search(islands, row, col + 1, visited)
    depth_first_search(islands, row + 1, col, visited)


def number_of_islands(islands: Island, visited: Grid) -> int:
    size: int = len(islands.matrix)
    num_islands: int = 0
    for i in range(size):
        for j in range(size):
            if visited.matrix[i][j] != 1 and islands.matrix[i][j] == 1:
                depth_first_search(islands, i, j, visited)
                num_islands += 1
    return num_islands


def main():
    size = 10
    islands: Island = Island(size, 0)
    islands.show()
    visited: Grid = Grid(size, False)
    print("NoI: ", number_of_islands(islands, visited))


if __name__ == '__main__':
    main()
