import evaluation
myEval = evaluation.eval()

def minimax(board,depth,maxPlayer):
    if depth == 0:
        return [myEval.evalPosition(board),board._most_recent_move]
    
    if maxPlayer:
        max_eval = [float('-inf'),1]
        for i in board._legal_moves:
            board.update_position(i)
            cur_eval = minimax(board,depth-1,False)
            max_eval = max(max_eval,cur_eval)
            max_eval[1] = i
            board.unmove()
            
        return max_eval
    
    if not maxPlayer:
        min_eval = [float('inf'),1]
        for i in board._legal_moves:
            board.update_position(i)
            cur_eval = minimax(board,depth-1,True)
            min_eval = min(min_eval,cur_eval)
            board.unmove()
        return min_eval

            