from functools import reduce

board = list()
for _ in range(19):
    row = list(map(int, input().split()))
    board.append(row)
n = int(input())
for _ in range(n):
    row, column = map(lambda num: num - 1, map(int, input().split()))
    for i in range(len(board[row])):
        board[row][i] = 1 if board[row][i] == 0 else 0
    for i in range(len(board)):
        board[i][column] = 0 if board[i][column] == 1 else 1
for i in range(len(board)):
    print(" ".join(list(map(str, board[i]))))
