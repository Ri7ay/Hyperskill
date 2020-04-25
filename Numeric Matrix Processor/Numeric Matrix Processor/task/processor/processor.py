def determinant(matrix):
    sum = 0
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        for i in range(len(matrix[0])):
            new_matrix = []
            for j in range(1, len(matrix)):
                new_matrix.append(list(matrix[j][k] for k in range(len(matrix[0])) if k != i))
            sum += (-1) ** i * (matrix[0][i] * determinant(new_matrix))
    return sum


def minor(matrix, n, m):
    new_matrix = []
    matrix[0], matrix[n] = matrix[n], matrix[0]
    for j in range(1, len(matrix)):
        new_matrix.append(list(matrix[j][k] for k in range(len(matrix[0])) if k != m))
    matrix[0], matrix[n] = matrix[n], matrix[0]
    if n <= 1:
        return (-1) ** (n + m) * determinant(new_matrix)
    else:
        return (-1) ** (n + m + ((n + 1) % 2)) * determinant(new_matrix)


while True:
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')
    select_num = int(input('Your choice:'))
    matrix_sizes = []

    if select_num == 0:
        break
    if select_num == 1:
        # Create matrix A
        n, m = map(int, input('Enter size of first matrix:').split())
        matrix_sizes.append([n, m])
        print('Enter first matrix:')
        matrix_A = [list(map(float, input().split())) for i in range(n)]

        # Create matrix B
        n, m = map(int, input('Enter size of first matrix:').split())
        matrix_sizes.append([n, m])
        print('Enter second matrix:')
        matrix_B = [list(map(float, input().split())) for j in range(n)]

        print('The result is:')
        if matrix_sizes[0] != matrix_sizes[1]:
            print('ERROR')
        else:
            for i in range(matrix_sizes[0][0]):
                print(*list(map(lambda x, y: x + y, matrix_A[i], matrix_B[i])))
    elif select_num == 2:
        # Create matrix A
        n, m = map(int, input('Enter size of first matrix:').split())
        matrix_sizes.append([n, m])
        matrix_A = [list(map(int, input().split())) for i in range(n)]

        # input constant
        num = int(input())
        print('The result is:')
        for i in range(matrix_sizes[0][0]):
            print(*list(map(lambda x: x * num, matrix_A[i])))
    elif select_num == 3:
        # Create matrix A
        n, m = map(int, input('Enter size of first matrix:').split())
        matrix_sizes.append([n, m])
        print('Enter first matrix:')
        matrix_A = [list(map(float, input().split())) for i in range(n)]

        # Create matrix B
        n, m = map(int, input('Enter size of first matrix:').split())
        matrix_sizes.append([n, m])
        print('Enter second matrix:')
        matrix_B = [list(map(float, input().split())) for j in range(n)]

        print('The result is:')
        if matrix_sizes[0][1] != matrix_sizes[1][0]:
            print('ERROR')
        else:
            for i in range(matrix_sizes[0][0]):
                for j in range(matrix_sizes[1][1]):
                    s = 0
                    for k in range(matrix_sizes[0][1]):
                        s += matrix_A[i][k] * matrix_B[k][j]
                    print(s, end=' ')
                print()
    elif select_num == 4:
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        select_num = int(input())
        if select_num == 1:
            # Create matrix A
            n, m = map(int, input('Enter size of first matrix:').split())
            print('Enter first matrix:')
            matrix_A = [list(map(float, input().split())) for i in range(n)]

            for i in range(m):
                print(*list(map(lambda x: x[i], matrix_A)))
        elif select_num == 2:
            # Create matrix A
            n, m = map(int, input('Enter size of first matrix:').split())
            print('Enter first matrix:')
            matrix_A = [list(map(float, input().split())) for i in range(n)]

            for i in range(m - 1, -1, -1):
                print(*reversed(list(map(lambda x: x[i], matrix_A))))
        elif select_num == 3:
            # Create matrix A
            n, m = map(int, input('Enter size of first matrix:').split())
            print('Enter first matrix:')
            matrix_A = [list(map(float, input().split())) for i in range(n)]

            for i in matrix_A:
                print(*reversed(i))
        elif select_num == 4:
            # Create matrix A
            n, m = map(int, input('Enter size of first matrix:').split())
            print('Enter first matrix:')
            matrix_A = [list(map(float, input().split())) for i in range(n)]

            matrix_A = reversed(matrix_A)
            for i in matrix_A:
                print(*i)
    elif select_num == 5:
        # Create matrix A
        n, m = map(int, input('Enter size of first matrix:').split())
        print('Enter first matrix:')
        matrix_A = [list(map(float, input().split())) for i in range(n)]

        print('The result is:')
        if n != m:
            print('ERROR')
        else:
            print(determinant(matrix_A))
    elif select_num == 6:
        # Create matrix A
        n, m = map(int, input('Enter size of first matrix:').split())
        print('Enter first matrix:')
        matrix_A = [list(map(float, input().split())) for i in range(n)]

        print('The result is:')
        if n != m or determinant(matrix_A) == 0:
            print('ERROR')
        else:
            const = 1 / determinant(matrix_A)
            minor(matrix_A, 2, 2)
            inverse_matrix = []
            for i in range(n):
                tmp_vector = []
                for j in range(m):
                    tmp_vector.append(minor(matrix_A, i, j))
                inverse_matrix.append(tmp_vector)

            for i in range(m):
                print(*list(map(lambda x: x[i] * const, inverse_matrix)))
