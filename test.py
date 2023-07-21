import Modules
import copy
import time
first_board = Modules.board.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Kkq - 0 1")


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

generateTotalMoves(first_board,3)
print(time.time()-inital)
print(count)
