def chk(game,case):
    #1가로
    if game[0] == case and game[0] == game[1] == game[2]:
        return True
    #1세로
    elif game[0] == case and game[0] == game[3] == game[6]:
        return True
    #2가로
    elif game[4] == case and game[3] == game[4] == game[5]:
        return True
    #2세로
    elif game[4] == case and game[1] == game[4] == game[7]:
        return True
    #3가로
    elif game[8] == case and game[6] == game[7] == game[8]:
        return True
    #3세로
    elif game[8] == case and game[2] == game[5] == game[8]:
        return True
    #대각
    elif game[4] == case and game[0] == game[4] == game[8]:
        return True
    #역대각
    elif game[4] == case and game[2] == game[4] == game[6]:
        return True
    else:
        return False

while True:
    game = input()
    if game == 'end':
        break
    X_cnt = game.count('X')
    O_cnt = game.count('O')

    if X_cnt == O_cnt+1 or X_cnt == O_cnt:
        if X_cnt == O_cnt+1:
            case1,case2 = 'X','O'
        else:
            case1,case2 = 'O','X'
        game_res1 = chk(game,case1)
        game_res2 = chk(game,case2)
        
        if game_res2:
            print('invalid')
        elif not game_res1:
            if game.count('.') == 0:
                print('valid')
            else:
                print('invalid')
        else:
            print('valid')
    else:
        print('invalid')
                    