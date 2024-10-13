class Graph:
    def __init__(self, size: int):
        self.matrix = [[0 for x in range(size)] for y in range(size)]
        self.edges = 0

    def show(self):
        for i in self.matrix:
            for j in i:
                print(j, end=" ")
            print()
        print('\n')

    def add_edge(self, x, y):
        self.matrix[x][y] += 1
        self.matrix[y][x] += 1
        self.edges += 1

    def number_of_edges(self):
        print('Number of edges', self.edges)


def main():
    g = Graph(4)
    g.show()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)

    g.show()
    g.number_of_edges()


if __name__ == '__main__':
    main()
