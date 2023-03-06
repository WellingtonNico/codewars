# https://www.codewars.com/kata/5650f1a6075b3284120000c0

import sys

def checkered_board(n):
    BLACK_SQUARE = '\u25A1'
    WHITE_SQUARE = '\u25A0'
    
    return '\n'.join(
        # a primeira lista gerada é bem simples, separada por \n 
        [
            ' '.join(
                # as pequenas listas são simples também, basta fazer uma verificação no índice pra saber se condiz com a regra
                [
                    BLACK_SQUARE  if not (lineIndex+squareIndex+n)%2 else WHITE_SQUARE
                    for squareIndex in range(n)
                ]
            )
            for lineIndex in range(n)
        ]
    )

if __name__ == '__main__':
    try:
        print(checkered_board(int(sys.argv[1])))
    except (IndexError,ValueError):
        print('Deve ser informado um número inteiro como primeiro parâmetro')

