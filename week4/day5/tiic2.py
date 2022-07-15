#from day5.tictactoe import player2


moves = [0,1,2,3,4,5,6,7,8,9]

WINNER_MOVES = [(0,1,2),(0,3,6),(3,4,5),(6,7,8),(0,4,8),(2,4,6),(1,4,7),(2,5,8)]

def print_board(moves):
    board = f"""
    {moves[0]}|{moves[1]}|{moves[2]}
    {moves[3]}|{moves[4]}|{moves[5]}
    {moves[6]}|{moves[7]}|{moves[8]}
    """
    print(board)
def player_one():
    x = input("player one, place a spot on the board you would like to go")
    x = int(x)
    moves[x] = 'X'
def player_two():
    o = input("player 2, place a spot on the board you would like to go")
    o = int(o)
    moves[o] = 'O'





random_num = 0
def check_winner():
    for combo in WINNER_MOVES:
        0, 4 ,8 
        moves_combo = [moves[combo[0]], moves[combo[1]], moves[combo[2]]]
        if all(moves_combo[0] == element for element in moves_combo):
            print("we have a winner!")
            random_num = 1
            


def game():
    """this is the final game"""
    print_board(moves)
    while random_num == 0:
        player_one()
        print_board(moves)
        check_winner()
        player_two()
        print_board(moves)
        check_winner()
        if random_num == 1:
            break
game()

