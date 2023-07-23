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
            max_eval = max(max_eval,cur_eval)
            board.unmove()
            if cur_eval[0] == max_eval[0]:
                max_eval[1] = i
            #alpha = max(alpha, cur_eval)
            #if beta <= alpha:
            #    break
        return max_eval
    
    if not maxPlayer:
        min_eval = [float('inf'),1]
        for i in board._legal_moves:
            board.update_position(i)
            cur_eval = minimax(myEval,board,depth-1,True,alpha,beta)
            min_eval = min(min_eval,cur_eval)
            board.unmove()
            if cur_eval[0] == min_eval[0]:
                min_eval[1] = i
            #beta = min(beta,cur_eval)
            #if beta <= alpha:
            #    break
        return min_eval

#print(minimax(Modules.board.Board(), 2, True))
#print(myEval.evalPosition(Modules.board.Board("r1bqkbnr/pppppppp/2n5/8/8/7N/PPPPPPPP/RNBQKB1R w KQkq - 0 1")))