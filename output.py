def print_board_line(board,line):
    line_string="|"
    num=0
    for i in board[line]:
        is_original=False
        if "." in i:
            is_original=True
            i=i.replace(".","")
        if is_original:
            i=f"\x1b[33m{i}\x1b[0m"
        vert=""
        if num%3==2:
            vert="|"
        num+=1
        line_string+=f" {i} {vert}"
    print(line_string)

def output_board(board):
    hor_sep="+---------+---------+---------+"
    for i in range(0,3):
        for j in range(0,3):
            if j==0:
                print(hor_sep)
            print_board_line(board,(3*i+j))
    print(hor_sep)
output_board(board)

