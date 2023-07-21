from .piece import Piece
from .empty import Empty
import copy


class Knight(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "n"
        self._value = 300
    
    def get_pseudo_legal_moves(cls,board):# def get_pseudo_legal_moves(cls, board):
        legal_moves = []
        
        def horizontal_checker(direction):
            # -1 = right, 1 = left (ik its confusing lol shut up mosh go away)
            # checking horizontal to check if the knight can move far in that direction
            horizontal_limit = 2 if direction == 1 else -5

            if (cls._pos[0]*direction) >= horizontal_limit:
                # when both sides are multiplied by -1 the inequality is flipped
                if cls._pos[1] >= 1:
                    far_upper = board._rep[cls._pos[1]-1][cls._pos[0]-2*direction]
                    if isinstance(far_upper, Empty) or far_upper.get_colour() != cls._colour:
                        # far left upper square is either empty or an enemy piece
                        legal_moves.append(far_upper._pos)
                
                if cls._pos[1] >= 0 and cls._pos[1] <= 6:    
                    far_lower = board._rep[cls._pos[1]+1][cls._pos[0]-2*direction]
                    if isinstance(far_lower, Empty) or far_lower.get_colour() != cls._colour:
                        # far left lower square is either empty or an enemy piece
                        legal_moves.append(far_lower._pos)
        
        def vertical_checker(direction):
            vertical_limit = 2 if direction == 1 else -5
            if (cls._pos[1]*direction) >= vertical_limit:
                # when both sides are multiplied by -1 the inequality is flipped
                if cls._pos[0] >= 1:
                    left_square = board._rep[cls._pos[1]-2*direction][cls._pos[0]-1]
                    if isinstance(left_square, Empty) or left_square.get_colour() != cls._colour:
                        legal_moves.append(left_square._pos)
                
                if cls._pos[0] <= 6:
                    right_square = board._rep[cls._pos[1]-2*direction][cls._pos[0]+1]
                    if isinstance(right_square, Empty) or right_square.get_colour() != cls._colour:
                        legal_moves.append(right_square._pos)
        
        horizontal_checker(1)
        horizontal_checker(-1)
        vertical_checker(1)
        vertical_checker(-1)
        
        return legal_moves
    

    def get_legal_moves(cls,board):
        pseudo_legal_moves = cls.get_pseudo_legal_moves(board)
        king_checked = board._white_checked if cls._colour == "white" else board._black_checked
        attacked_squares = copy.deepcopy(board.get_king_attacked_squares())
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
                     
            legal_moves = pseudo_legal_moves  
                
                
        else:
            legal_moves =pseudo_legal_moves
        
        return legal_moves if legal_moves != [] else None

    
    