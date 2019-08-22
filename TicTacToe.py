
import itertools
from colorama import Fore, Back, Style, init

init()
def show(map, val = 0, row = 0, col = 0 ,onlyshow=False):
    try:
        if map[row][col]!=0:
            print("position already occupied! ")
            return map,False
        print("     C"+" C".join([str(i+1) for i in range(len(map))]))      #GIVES NAME LAYOUT OF COLUMNS
        if not onlyshow:
            map[row][col]=val
        for count, row in enumerate(map):
            colored_row=""
            for item in row:
                if item==0:
                    colored_row +="    "
                elif item==1:
                    colored_row += Fore.GREEN + " X " + Style.RESET_ALL
                elif item==2:
                    colored_row += Fore.MAGENTA + " O " + Style.RESET_ALL
            print("R",count+1, colored_row)

        return map, True

    except IndexError as e:
        print("Error: Row/Col out of range ",e)
        return map,False
    
    except Exception as e:
        print("DAmn You dummy!!", e)
        return map,False



#tictactoe =show(tictactoe , onlyshow=True)

def win(game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0]!= 0 :
            return True
        else:
            return False


#HORIZONTAL CHECK
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} wins horizontally")
            return True

#VERTICAL CHECK
    for col in range(len(game)):
        check=[]
        for row in game:
            check.append(row[col])
    if all_same(check):
        print(f"Player {check[0]} wins vertically")
        return True
#DIAGONAL CHECK
    '''
    cols=reversed(range(len(game)))
    rows=range(len(game))                       UPDATED CODE BELOW
    for col,row in zip(cols,rows):
        print(col,row)
    '''
    diags=[]
    for col,row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} wins diagonally")
        return True
    diags=[]
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} wins diagonally")
        return True

    return False

play=True

players=[1,2]

while play: 
    '''
    tictactoe= [[0,0,0],
                [0,0,0],
                [0,0,0]]
    '''
    size=int(input("Enter the size of game board: "))
    tictactoe=[[0 for i in range(size)]for i in range(size)]
    game_won= False
    tictactoe, _ =show(tictactoe , onlyshow=True)           # underscore: returned item is irrelevant
    player_choice=itertools.cycle([1,2])
    while not game_won:
        current_player=next(player_choice)
        played=False
        while not played:
            col_choice=int(input("Select a column ( 1 2 3 ): "))
            row_choice=int(input("Select a row ( 1 2 3 ): "))
            print("MOVE OF PLAYER ",current_player)
            tictactoe, played=show(tictactoe,current_player,row_choice-1,col_choice-1)

        if win(tictactoe):
            game_won=True
            again=input("Game Over. Play again? (y/n) ")
            if again.lower()=="y":
                print("Restarting ")
            elif again.lower()=="n":
                print("Exiting ")
                play=False
            else:
                print("Invalid answer ")
                play=False