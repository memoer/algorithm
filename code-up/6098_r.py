board = list()
for _ in range(10):
    board.append(input().split())
i, j = 1, 1
board[i][j] = "9"
while True:
    next_i = i + 1
    next_j = j + 1
    if board[i][next_j] == "0":
        board[i][next_j] = "9"
        j = next_j
    elif board[i][next_j] == "2":
        board[i][next_j] = "9"
        break
    elif board[next_i][j] == "0":
        board[next_i][j] = "9"
        i = next_i
    elif board[next_i][j] == "2":
        board[next_i][j] = "9"
        break
    else:
        break


for i in range(10):
    print(" ".join(board[i]))