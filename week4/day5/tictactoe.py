

board1 = ["   |", "   |", "   "]
board2 = ["   |", "   |", "   "]
board3 = ["   |", "   |", "   "]
def create__board():
    line1 = "__________"
    print("".join(board1),"\n", line1,'\n'+"".join(board2),'\n', line1, '\n'+"".join(board3) )

create__board()

def player1():
    row = input("player 1 choose a row")
    row = int(row)
    col = input("player1 choose acolumn")
    col = int(col)
    if row == 1:
        if col == 1:
            board1[0] = " x |"
        elif col == 2:
            board1[1] = " x |"
        elif col == 3:
            board1[3] = " x |"
    if row == 2:
        if col == 1:
            board2[0] = " x |"
        elif col == 2:
            board2[1] = " x |"
        elif col == 3:
            board2[3] = " x |"
    if row == 3:
        if col == 1:
            board3[0] = " x |"
        elif col == 2:
            board3[1] = " x |"
        elif col == 3:
            board3[3] = " x |"
    create__board()
player1()   

def player2():
    row = input("player 2 choose a row")
    row = int(row)
    col = input("player 2 choose acolumn")
    col = int(col)
    if row == 1:
        if col == 1:
            board1[0] = " 0 |"
        elif col == 2:
            board1[1] = " 0 |"
        elif col == 3:
            board1[3] = " 0 |"
    if row == 2:
        if col == 1:
            board2[0] = " 0 |"
        elif col == 2:
            board2[1] = " 0 |"
        elif col == 3:
            board2[3] = " 0 |"
    if row == 3:
        if col == 1:
            board3[0] = " 0 |"
        elif col == 2:
            board3[1] = " 0 |"
        elif col == 3:
            board3[3] = " 0 |"
    create__board()
player2()


def check_winner():
    if board1[0] == " x |":
        if board1[1] == " x |":
           if board1[2] == " x |":
                print("you win")
                return True
        elif board2[0] == " x |":
            print('hi')
