import evaluation
import Modules.board


def minimax(myEval,board,depth,maxPlayer,alpha=[float('-inf'),1],beta=[float('inf'),1]):
    if depth == 0:
        return [myEval.evalPosition(board),board._most_recent_move]
    
    if maxPlayer:
        max_eval = [float('-inf'),1]
        for i in board._legal_moves:
            board.update_position(i)
            cur_eval = minimax(myEval,board,depth-1,False,alpha,beta)
            if max_eval < cur_eval:
                max_eval = cur_eval
                max_eval[1] = i 
            board.unmove()
            alpha = max(alpha, max_eval)
            if beta <= alpha:
               break
        return max_eval
    
    if not maxPlayer:
        min_eval = [float('inf'),1]
        for i in board._legal_moves:
            board.update_position(i)
            cur_eval = minimax(myEval,board,depth-1,True,alpha,beta)
            if min_eval > cur_eval:
                min_eval = cur_eval
                min_eval[1] = i 
            board.unmove()
            beta = min(beta,min_eval)
            if beta <= alpha: 
               break
        return min_eval


# myEval = evaluation.eval()
# print(minimax(myEval,Modules.board.Board(), 3, True))
#print(myEval.evalPosition(Modules.board.Board("r1bqkbnr/pppppppp/2n5/8/8/7N/PPPPPPPP/RNBQKB1R w KQkq - 0 1")))