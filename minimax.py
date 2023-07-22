import Modules
import copy
import evaluation
import time
first_board = Modules.board.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Kkq - 0 1")
myEval = evaluation.eval()

# depth1= []
# for i in first_board._legal_moves:
#     new_board = copy.deepcopy(first_board)
#     new_board.update_position(i)
#     depth1.append(new_board)

# depth2 = []
# for i in depth1:
#     for j in i._legal_moves:
#         new_board = copy.deepcopy(first_board)
#         new_board.update_position(j)
#         depth2.append(new_board)

# print(len(depth2))

# get legal moves for board
# create boards with those positions
inital = time.time()
def generateTotalMoves(board, depth):
    global count
    if depth == 0:
        count += 1
        return 0
    else:
        for i in board._legal_moves:
            board.update_position(i)
            generateTotalMoves(board, depth-1)
            board.unmove()

count = 0

# generateTotalMoves(first_board,3)
# print(time.time()-inital)
# print(count)

inital = time.time()
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
            
print(minimax(first_board,2,True))
print(time.time()-inital)
            