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

if __name__ == "__main__":
    print("Matrix multiplication")
