board = [[0 for _ in range(20)] for _ in range(20)]
n = int(input())
for _ in range(n):
    row, column = map(int, input().split())
    board[row][column] = 1
for i in range(20):
    if i == 0:
        continue
    print(" ".join(map(str, board[i][1:])))
