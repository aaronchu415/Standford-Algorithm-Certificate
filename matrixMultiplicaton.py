A = [[2, 1], [3, 4], [5, 6]]
B = [[1, 3, 6], [2, 4, 5]]


def naieveSolution(A, B):

    o = []

    for i in range(len(A)):
        row = []
        for col in range(len(B[0])):
            s = 0
            for j in range(len(A[i])):
                s += A[i][j] * B[j][col]
            row.append(s)
        o.append(row)

    return o


naieveSolution(A, B)
