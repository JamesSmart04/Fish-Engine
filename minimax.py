import evaluation
import Modules.board
myEval = evaluation.eval()

first_board = Modules.board.Board()


def minimax(board,depth,alpha,beta,maxPlayer):
    if depth == 0:
        return [myEval.evalPosition(board),board._most_recent_move]
    
    if maxPlayer:
        max_eval = [float('-inf'),1]
        for i in board._legal_moves:
            board.update_position(i)
            cur_eval = minimax(board,depth-1,alpha,beta,False)
            max_eval = max(max_eval,cur_eval)
            board.unmove()
            if cur_eval[0] == max_eval[0]:
                max_eval[1] = i
            alpha = max(alpha, cur_eval)
            if beta <= alpha:
                break            

        return max_eval
    
    if not maxPlayer:
        min_eval = [float('inf'),1]
        for i in board._legal_moves:
            board.update_position(i)
            cur_eval = minimax(board,depth-1,alpha,beta,True)
            min_eval = min(min_eval,cur_eval)
            board.unmove()
            if cur_eval[0] == min_eval[0]:
                min_eval[1] = i
            beta = min(beta,cur_eval)
            if beta <= alpha:
                break
        return min_eval

turn = True 
while True:

    first_board.update_position(minimax(first_board,3,[float('-inf'),1],[float('inf'),1],turn)[1])
    print(first_board)
    turn = not turn




            