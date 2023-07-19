from .piece import Piece
from .empty import Empty  
import copy
class Bishop(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "b"
        self._value = 320
    
    def get_pseudo_legal_moves(cls, board):
        legal_moves = []
        #top left
        i = 0
        j = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[1]+i > 0 and cls._pos[0]+j > 0:
            i -= 1
            j -= 1
            currentSquare = board._rep[cls._pos[1]+i][cls._pos[0]+j]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)


        #top right
        i = 0
        j = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[1]+i > 0 and cls._pos[0] + j < 7:
            i += -1
            j += 1
            currentSquare = board._rep[cls._pos[1]+i][cls._pos[0]+j]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)

    
        #bottom left
        i = 0
        j = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[0]+i > 0 and cls._pos[1]+j < 7 :
            i -= 1
            j += 1
            currentSquare = board._rep[cls._pos[1]+j][cls._pos[0]+i]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)

        #bottom right
        i = 0
        j = 0 
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[0]+i < 7 and cls._pos[1]+j < 7:
            i += 1
            j += 1
            currentSquare = board._rep[cls._pos[1]+j][cls._pos[0]+i]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)
            
            
        # if not isinstance(currentSquare, Empty):
        #     legal_moves.append(currentSquare._pos)
            
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
