h, w = map(int, input().split())
board = [[0 for _ in range(w)] for _ in range(h)]
n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    i, j = x - 1, y - 1
    if d == 0:
        for k in range(l):
            if j + k >= len(board[j]):
                break
            board[i][j + k] = 1
    else:
        for k in range(l):
            if i + k >= len(board):
                break
            board[i + k][j] = 1

for i in range(len(board)):
    print(" ".join(list(map(str, board[i]))))