BOARD_SIZE = 10
board = []
for _ in range(BOARD_SIZE):
    board.append(input().split())
row = 1
col = 1
while True:
    stop = False
    for i in range(col, len(board[row])):
        if board[row][i] == "1":
            col = i - 1
            break
        elif board[row][i] == "2":
            board[row][i] = "9"
            stop = True
            break
        board[row][i] = "9"
    row += 1
    if board[row][col] == "1":
        break
    elif stop:
        break


print("\n".join(list(map(lambda row: " ".join(row), board))))
