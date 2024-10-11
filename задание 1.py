n, m = map(int, input("Введите n и m через пробел: ").split())
A = []
for _ in range(n):
    A.append([0] * m)

num = 0
for i in range(n):
    if i % 2 == 0:
        for j in range(m):
            A[i][j] = num
            num += 1
    else:
        for j in range(m - 1, -1, -1):
            A[i][j] = num
            num += 1

for row in A:
    for x in row:
        print(x, end = '\t')
    print()


