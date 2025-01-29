import chess
import math
import time
def evaluate(board, isWhite = False) -> int: 
    
    piece_vals = {
        chess.PAWN: 100,
        chess.KNIGHT: 320,
        chess.BISHOP: 330,
        chess.ROOK: 500,
        chess.QUEEN: 900,
        chess.KING: 20000
    }
    piece_table = {
        chess.PAWN: [
            0,  0,  0,  0,  0,  0,  0,  0,
            50, 50, 50, 50, 50, 50, 50, 50,
            10, 10, 20, 30, 30, 20, 10, 10,
            5,  5, 10, 25, 25, 10,  5,  5,
            0,  0,  0, 20, 20,  0,  0,  0,
            5, -5,-10,  0,  0,-10, -5,  5,
            5, 10, 10,-20,-20, 10, 10,  5,
            0,  0,  0,  0,  0,  0,  0,  0
        ],
        chess.KNIGHT: [
            -50,-40,-30,-30,-30,-30,-40,-50,
-40,-20,  0,  0,  0,  0,-20,-40,
-30,  0, 10, 15, 15, 10,  0,-30,
-30,  5, 15, 20, 20, 15,  5,-30,
-30,  0, 15, 20, 20, 15,  0,-30,
-30,  5, 10, 15, 15, 10,  5,-30,
-40,-20,  0,  5,  5,  0,-20,-40,
-50,-40,-30,-30,-30,-30,-40,-50,
        ],
        chess.BISHOP: [-20,-10,-10,-10,-10,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5, 10, 10,  5,  0,-10,
-10,  5,  5, 10, 10,  5,  5,-10,
-10,  0, 10, 10, 10, 10,  0,-10,
-10, 10, 10, 10, 10, 10, 10,-10,
-10,  5,  0,  0,  0,  0,  5,-10,
-20,-10,-10,-10,-10,-10,-10,-20,],
        chess.ROOK: [0,  0,  0,  0,  0,  0,  0,  0,
  5, 10, 10, 10, 10, 10, 10,  5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
 -5,  0,  0,  0,  0,  0,  0, -5,
  0,  0,  0,  5,  5,  0,  0,  0],
        chess.QUEEN: [-20,-10,-10, -5, -5,-10,-10,-20,
-10,  0,  0,  0,  0,  0,  0,-10,
-10,  0,  5,  5,  5,  5,  0,-10,
 -5,  0,  5,  5,  5,  5,  0, -5,
  0,  0,  5,  5,  5,  5,  0, -5,
-10,  5,  5,  5,  5,  5,  0,-10,
-10,  0,  5,  0,  0,  0,  0,-10,
-20,-10,-10, -5, -5,-10,-10,-20],
        chess.KING: [-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-30,-40,-40,-50,-50,-40,-40,-30,
-20,-30,-30,-40,-40,-30,-30,-20,
-10,-20,-20,-20,-20,-20,-20,-10,
 20, 20,  0,  0,  0,  0, 20, 20,
 20, 30, 10,  0,  0, 10, 30, 20]
    }



    score = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)

        if piece:
            
            value = piece_vals[piece.piece_type]
            valArr = piece_table[piece.piece_type]
            if not isWhite: 
                if piece.color ==chess.BLACK:
                    score += value + valArr[square]
                    
                else:
                    score -= value - valArr[::-1][square]
            else:
                if piece.color == chess.WHITE:
                    score += value + valArr[::-1][square]

                else:
                    score -= value - valArr[square]
    return score 

def miniMax(board, depth, alpha, beta, isMax, isWhite):
    if depth == 0 or board.is_game_over():
        return evaluate(board, isWhite)

    if isMax:
        max_score = -math.inf
        for move in board.legal_moves:
            board.push(move)
            score = miniMax(board, depth - 1, alpha, beta, False, isWhite)
            board.pop()
            high_score = max(max_score, score)
            alpha = max(alpha, score)
            if beta<=alpha:
                break
        return high_score

    else:
        min_score = math.inf
        for move in board.legal_moves:
            board.push(move)
            score = miniMax(board, depth - 1, alpha, beta,True,isWhite)
            board.pop()
            min_score =min(score, min_score) 
            beta = min(beta, score)
            if beta<=alpha:
                break
        return min_score 
    

    if isMax: return maxi(depth) 
    else: return mini(depth)

def find_move(board, depth, isWhite = False):
    bestMove = None
    bestValue = -math.inf
    alpha = -math.inf
    beta = math.inf


    for move in board.legal_moves:
        board.push(move)
        boardVal = miniMax(board, depth - 1, alpha, beta, False, isWhite)
        board.pop()
        
        if boardVal > bestValue:
            bestValue = boardVal
            bestMove = move
    return bestMove
if __name__=="__main__":
    board = chess.Board()
    print("Welcome to your demise! Type your move to play:")

    while not board.is_game_over():
        print(board)
        myMove = None
        move = None
        while move == None:
            try:
                myMove = input("Your move in UCI format: ")
                move = chess.Move.from_uci(myMove)
                while move not in board.legal_moves:
                    print("illegal move, input again:")
                    myMove = input()
                    move = chess.Move.from_uci(myMove)
            except:
                print("Error")
        
        board.push(move)

        # bot_move = find_move(board, 4, False)
        # board.push(bot_move)
        # time.sleep(1)
        bot_move = find_move(board, 5, False)
        board.push(bot_move)
        print(bot_move)
        # time.sleep(1)