"""
Matrix multiplication
---------------------

Matrix multiplication process involves checking compatibility of dimension
and multiplying nth row with nth column to get one cell output.

Please refer to the matrix multiplication resource to understand it easily.

given,

x =  | 1  2 |  and y = | 1  3 |
     | 3  4 |          | 2  1 |

if z is the resultant matrix,

step 1:   z[0][0] = x[0][0] * y[0][0] + x[0][1] * y[1][0] = 1 + 4 = 5
step 2:   z[0][1] = x[0][0] * y[0][1] + x[0][1] * y[1][1] = 3 + 2 = 5
step 3:   z[1][0] = x[1][0] * y[0][0] + x[1][1] * y[1][0] = 3 + 8 = 11
step 4:   z[1][1] = x[1][0] * y[0][1] + x[1][1] * y[1][1] = 9 + 4 = 13

We will be using basic python list to perform matrix multiplication without
using any third party libraries, so it might be a bit tricky to perform if you
do not have better understanding of iteration.
"""


class Matrix:
    data: list[list[int | float]]

    @classmethod
    def zeros(cls, rows: int, cols: int):
        if rows < 1 and cols < 1:
            raise ValueError("invalid rows or columns provided")
        return Matrix([[0 for _ in range(rows)] for _ in range(cols)])

    def __init__(self, data: list[list[int | float]]) -> None:
        if data.__len__():
            _len = data[0].__len__()

            # check if matrix is valid: i.e. all columns have same number of rows
            for col in range(1, data.__len__()):
                if data[col].__len__() != _len:
                    raise ValueError("Invalid matrix")
        self.data = data

    @property
    def size(self):
        if self.data.__len__() == 0:
            return (0, 0)
        return (self.data[0].__len__(), self.data.__len__())

    def get_row(self, index: int):
        return self.data[index]

    def get_column(self, index: int):
        return [d[index] for d in self.data]

    def __str__(self) -> str:
        if self.data.__len__():
            return "\n".join(
                ["| " + "".join([f"{i:^5d}" for i in row]) + " |" for row in self.data]
            )
        return "|   |"

    def __mul__(self, other: "Matrix"):
        """
        This method overloads python's default multiplication operation between
        two Matrix objects so that we can easily perform `*` operation.
        """
        (self_rows, self_cols) = self.size
        (other_rows, other_cols) = other.size
        if self_rows != other_cols:
            raise ValueError("Dimensions mismatch")

        # by for loop and matrix.zeros
        # this part is easy to understand but is a bit more computationally expensive

        # result = Matrix.zeros(other_rows, self_cols)
        # for row in range(other_rows):
        #     for col in range(self_cols):
        #         result.data[row][col] = sum(
        #             [a * b for (a, b) in zip(self.get_row(row), other.get_column(col))]
        #         )
        # return result

        # by comprehension quicker
        return Matrix(
            [
                [
                    sum(
                        [
                            a * b
                            for (a, b) in zip(self.get_row(row), other.get_column(col))
                        ]
                    )
                    for col in range(self_cols)
                ]
                for row in range(other_rows)
            ]
        )


if __name__ == "__main__":
    print("Matrix multiplication")

    # It raises error "Invalid matrix" when uncommented
    # m = Matrix(
    #     [
    #         [1, 2],
    #         [3,  ],
    #         [5, 6],
    #     ]
    # )

    # if we uncomment lines below, we get Dimensions mismatch exception
    # m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    # m2 = Matrix([[2, 3, 4], [5, 6, 7]])
    # print("result is: \n", m1 * m2)

    m1 = Matrix([[1, 2, 3], [4, 5, 6]])
    m2 = Matrix([[2, 3], [4, 5], [6, 7]])
    print("m1 X m2 = :", m1 * m2, sep="\n")
    print("m2 X m1 = :", m2 * m1, sep="\n")
