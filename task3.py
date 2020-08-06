class Cell(object):
    def __init__(self, count: int):
        if count <= 0:
            raise ValueError
        self.count = count

    def __add__(self, other):
        return Cell(count=self.count + other.count)

    def __sub__(self, other):
        sub = self.count - other.count
        if sub <= 0:
            raise ValueError
        return Cell(count=sub)

    def __mul__(self, other):
        return Cell(count=self.count * other.count)

    def __truediv__(self, other):
        return Cell(count=self.count // other.count)

    def make_order(self, cols):
        rows = self.count // cols
        cells_full = '\n'.join([''.join(['*' for col in range(cols)])
                                for row in range(rows)])
        rows_part = self.count % cols
        if rows_part > 0:
            cells_part = '\n'.join([''.join(['*' for col in range(rows_part)])
                                    for row in range(1)])
            out = cells_full + '\n' + cells_part
        else:
            out = cells_full
        print(out)

    def __str__(self):
        return str(self.count)


cell_1 = Cell(9)
cell_2 = Cell(2)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

cell_1.make_order(2)
