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
            if max_eval[0] < cur_eval[0]:
                max_eval = cur_eval
                max_eval[1] = i 
            # print(cur_eval)
            board.unmove()
            alpha = max(alpha, max_eval)
            if beta[0] <= alpha[0]:
                break
        return max_eval
    

    if not maxPlayer:
        min_eval = [float('inf'),1]
        for i in board._legal_moves:
            board.update_position(i)
            cur_eval = minimax(myEval,board,depth-1,True,alpha,beta)
            if min_eval[0] > cur_eval[0]:
                min_eval = cur_eval
                min_eval[1] = i 
               
            board.unmove()
            beta = min(beta,min_eval)
            if beta[0] <= alpha[0]: 
                break
        return min_eval


# myEval = evaluation.eval()
# myBoard = Modules.board.Board()
# print(myBoard)
# print(minimax(myEval,myBoard, 3, True))
