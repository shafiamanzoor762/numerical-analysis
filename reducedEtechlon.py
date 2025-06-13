# def reduced_echelon(matx):
#     num_rows = len(matx)
#     num_cols = len(matx[0])

#     lead = 0

#     for r in range(num_rows):
#         if lead >= num_cols:
#             return
        
#         pivot_row = r
#         while matx[pivot_row][lead] == 0:
#             pivot_row += 1
#             if pivot_row == num_rows:
#                 pivot_row = r
#                 lead += 1
#                 if lead == num_cols:
#                     return

#         matx[pivot_row], matx[r] = matx[r], matx[pivot_row]
#         pivot_val = matx[r][lead]
#         matx[r] = [elem / pivot_val for elem in matx[r]]

#         for i in range(num_rows):
#             if i != r:
#                 multiplier = matx[i][lead]
#                 matx[i] = [elem - multiplier * matx[r][idx] for idx, elem in enumerate(matx[i])]

#         lead += 1

# matx = [
#     [1, 2, -1, -4],
#     [2, 3, -1, -11],
#     [-2, 0, -3, 22]
# ]

# reduced_echelon(matx)

# print("Reduced Row Echelon Form:")
# for row in matx:
#     print(row)

# print('_____________')
# print(' X  | Y |  Z |')
# for row in matx:
#     print(row[3],end='|')


def reduced_echelon(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for i in range(min(num_rows, num_cols)):
        if matrix[i][i] != 0:
            multiplier = 1.0 / matrix[i][i]
            for j in range(num_cols):
                matrix[i][j] *= multiplier

        for k in range(num_rows):
            if k != i and matrix[k][i] != 0:
                multiplier = matrix[k][i]
                for j in range(num_cols):
                    matrix[k][j] -= multiplier * matrix[i][j]

matrix = [
    [1, 2, -1, -4],
    [2, 3, -1, -11],
    [-2, 0, -3, 22]
]

reduced_echelon(matrix)

print("Reduced Echelon Form:")
for row in matrix:
    print(row)

print('_____________')
print(' X  | Y |  Z |')
for row in matrix:
    print(row[3],end='|')