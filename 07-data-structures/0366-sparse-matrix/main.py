class SparseMatrix:
    def __init__(self):
        self.cells = {}

    def set(self, row, col, value):
        if value == 0:
            self.cells.pop((row, col), None)
        else:
            self.cells[(row, col)] = value

    def get(self, row, col):
        return self.cells.get((row, col), 0)


def main():
    matrix = SparseMatrix()
    matrix.set(1, 1, 5)
    print(matrix.get(1, 1), matrix.get(0, 0))


if __name__ == "__main__":
    main()
