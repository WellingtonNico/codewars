def snakes_and_ladders(board, dice):
    finalBoardIndex = len(board) - 1
    currentBoardIndex = 0
    for diceThrow in enumerate(dice) :
        currentBoardIndex += diceThrow
        if currentBoardIndex > finalBoardIndex:
            currentBoardIndex -= diceThrow
        else:
            currentBoardIndex += board[currentBoardIndex] 
        if currentBoardIndex == finalBoardIndex:
            break
    return currentBoardIndex


dice = [2, 1, 5, 1, 5, 4]
board = [0, 0, 3, 0, 0, 0, 0, -2, 0, 0, 0]
if snakes_and_ladders(board,dice) == 10:
    print('ok')
else:
    print('errado')

dice = [2, 1, 2, 2, 3, 2, 6]
board = [0, 2, 0, 0, 0, 2, 8, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0]
if snakes_and_ladders(board,dice) == 14:
    print('ok')
else:
    print('errado')

dice = [4, 4, 1, 6, 3, 1, 3]
board = [0, 0, 4, 0, 0, 0, 0, 2, 0, 0, 0]
if snakes_and_ladders(board,dice) == 10:
    print('ok')
else:
    print('errado')

dice = [6, 6, 6, 6, 6, 6]
board = [0, 0, 0, 0, 0]
if snakes_and_ladders(board,dice) == 0:
    print('ok')
else:
    print('errado')
