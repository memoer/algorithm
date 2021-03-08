row, col = map(int, input().split())
board = [["0" for _ in range(col)] for _ in range(row)]
n = int(input())
for _ in range(n):
    l, d, x, y = map(int, input().split())
    row, col = x - 1, y - 1
    if d == 0:
        # 가로
        for k in range(len(board[row])):
            if k >= col and l > 0:
                board[row][k] = "1"
                l -= 1
    else:
        # 세로
        for k in range(len(board)):
            if k >= row:
                for t in range(len(board[k])):
                    if t == col and l != 0:
                        board[k][t] = "1"
                        l -= 1
print("\n".join(list(map(lambda x: " ".join(x), board))))
