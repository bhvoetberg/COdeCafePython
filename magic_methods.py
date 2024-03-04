class SomeRowColList:
    def __init__(
            self, rows: int, cols: int, init_state: list[list[int]] | None = None) -> None:
        self.rows = rows
        self.cols = cols
        if init_state:
            self.grid = init_state
        else:
            self.grid = [[0] * self.cols for _ in range(self.rows)]

    def __iter__(self):
        for row in range(self.rows):
            for col in range(self.cols):
                yield row, col, self


a_list = SomeRowColList(3, 4)
for list_item in a_list:
    print(list_item)
