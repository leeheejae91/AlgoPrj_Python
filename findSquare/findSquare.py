board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
cnt = 0
s_idx = 0
e_idx = 0


def find_square(row_n, x, y):
    print(row_n, x, y + 1)

    for i in range(row_n, row_n + (y-x)+1):
        if i < len(board):
            print(board[i][x:y+1])



for row_num in range(len(board)):
    for i in range(len(board[row_num])):
        for j in range(i, len(board[row_num])):
            sub_row = board[row_num][i:j + 1]
            print(row_num, i, j + 1, sub_row)
            if len(sub_row) != 1 and sum(sub_row) == len(sub_row):
                find_square(row_num, i, j)




