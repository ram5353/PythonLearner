def transpose(matrix):
    m, n = len(matrix), len(matrix[0])
    answer = [[None] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            answer[j][i] = matrix[i][j]
    return answer


print(transpose([[1,2,3], [4,5,6]]))