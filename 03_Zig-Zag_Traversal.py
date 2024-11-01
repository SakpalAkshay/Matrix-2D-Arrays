
n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    
    if i%2 == 0:
        for j in range(m):
            print(matrix[i][j], end = " ")
    else:
        print(*reversed(matrix[i]), end=" ")
