BOARD_SIZE = 19
row_list = []
board = []


def print_board(board):
    row_str = list(map(lambda row: " ".join(row), board))
    print("\n".join(row_str))


for _ in range(BOARD_SIZE):
    r = input().split(" ")
    row_list.append(r)
for r in row_list:
    board.append(r)

n = int(input())
for _ in range(n):
    row, col = map(int, input().split())
    board[row - 1] = list(map(lambda x: "0" if x == "1" else "1", board[row - 1]))
    for i in range(BOARD_SIZE):
        board[i][col - 1] = "0" if board[i][col - 1] == "1" else "1"


print_board(board)