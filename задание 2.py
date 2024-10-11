N, M = map(int, input("Введите n и m через пробел: ").split())
matrix = [list(map(int, input().split())) for _ in range(N)]

new_matrix = []
for _ in range(M):
    new_matrix.append([0] * N)
for i in range(N):
    for j in range(M):
        new_matrix[j][N - 1 - i] = matrix[i][j]

print (M, N)
for row in new_matrix:
    for x in row:
        print(x, end = '\t')
    print()
