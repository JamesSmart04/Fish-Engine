from .piece import Piece
from .empty import Empty

class Pawn(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "p"
        self._value = 100

    def get_pseudo_legal_moves(cls, board):

        legal_moves = []

        direction = 1
        if cls._colour == "white" : direction = -1

        # straight
        if isinstance(board._rep[cls._pos[1]+direction][cls._pos[0]], Empty):
            legal_moves.append([cls._pos[0],cls._pos[1]+direction])
            start_row = 6 if direction == -1 else 1
            if cls._pos[1] == start_row  and isinstance(board._rep[cls._pos[1]+direction*2][cls._pos[0]], Empty):
                legal_moves.append([cls._pos[0],cls._pos[1]+direction*2])
                
        
        # not straight
        left_square = None
        right_square = None
        if cls._pos[0] > 0:
            left_square = board._rep[cls._pos[1]+direction][cls._pos[0]-1] 
            if not isinstance(left_square,Empty) and left_square.get_colour() != cls._colour:
                legal_moves.append(left_square._pos)
        if cls._pos[0] < 7:
            right_square = board._rep[cls._pos[1]+direction][cls._pos[0]+1]
            if not isinstance(right_square,Empty) and right_square.get_colour() != cls._colour:
                legal_moves.append(right_square._pos)
        
        # en passant:
        left_square = None
        right_square = None
        en_passant_list = board.get_white_en_passant_list() if cls._colour == "black" else board.get_black_en_passant_list()
        
        if cls._pos[0] > 0:
            left_square = board._rep[cls._pos[1]][cls._pos[0]-1]
            if isinstance(left_square, Pawn) and left_square.get_position() in en_passant_list:
                legal_moves.append(board._rep[cls._pos[1]+direction][cls._pos[0]-1].get_position())
        
        if cls._pos[0] < 7:
            right_square = board._rep[cls._pos[1]][cls._pos[0]+1]
            if isinstance(right_square, Pawn) and right_square.get_position() in en_passant_list:
                legal_moves.append(board._rep[cls._pos[1]+direction][cls._pos[0]+1].get_position())
        
        return legal_moves
    
    def get_legal_moves(cls,board):
        pseudo_legal_moves = cls.get_pseudo_legal_moves(board)
        king_checked = board._white_checked if cls._colour == "white" else board._black_checked
        attacked_squares = board.get_king_attacked_squares()
        #fixing attacked squares ([] = pseudolegalmoves)
        legal_moves = []

        #case 1: King is checked
        if king_checked == True:
            for i in range(len(attacked_squares)):

                if attacked_squares[i] == []:
                    attacked_squares[i] = pseudo_legal_moves
            if king_checked == True:
                for i in pseudo_legal_moves:
                    if i in attacked_squares[0] and i in attacked_squares[1] and i in attacked_squares[2]\
                    and i in attacked_squares[3] and i in attacked_squares[4]:
                        legal_moves.append(i)

        #case 2: piece is pinned to king
        elif attacked_squares != [[],[],[],[],[]]: #king is pinned
            for i in attacked_squares:
                if cls._pos in i:
                    for j in pseudo_legal_moves:
                        if j in i:
                            legal_moves.append(j)
                    return legal_moves if legal_moves != [] else None      
                
        else:
            legal_moves = pseudo_legal_moves
        
        return legal_moves if legal_moves != [] else None
