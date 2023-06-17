# import numpy library
import numpy as np

def find_max_number_in_row_and_column():
    # create a 2D matrix of unique integer numbers
    matrix = np.random.randint(1, 10, size=(3, 3))
    print("The matrix is:")
    print(matrix)

    row_max = []
    col_max = []

    # loop over the rows of the matrix
    for i in range(len(matrix)):
        max_row = 0
        max_col = 0
        # loop over the columns of the matrix
        for j in range(len(matrix[i])):
            # compare the current element with the max value in the current row
            if matrix[i][j] > max_row:
                max_row = matrix[i][j]
                max_col = j
                row_max.append(max_col)


    # loop over the columns of the matrix
    for j in range(len(matrix[0])):
        max_col = 0
        max_row = 0
        # loop over the rows of the matrix
        for i in range(len(matrix)):
            # compare the current element with the max value in the current column
            if matrix[i][j] > max_col:
                # update the max value and the row index
                max_col = matrix[i][j]
                max_row = i
                # append the row index to the col_max list
                col_max.append(max_row)

    # initialize an empty list to store the coordinates of the elements that satisfy the condition
    indices = []

    # loop over the row_max and col_max lists simultaneously
    for i, j in zip(row_max, col_max):
        # check if the element at (i, j) is equal to the max value in its row and column
        if matrix[i][j] == matrix[row_max[i], col_max[j]]:
            # append the coordinates to the indices list
            indices.append((i, j))

    print(list(set(indices)))



find_max_number_in_row_and_column()