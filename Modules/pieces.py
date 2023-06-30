from Modules.misc import *
class Piece:
    def __init__(self, colour="white", pos=[0,0]) -> None:
        self._pos = pos
        self._colour = colour
        self._piece = ""
    
    def set_colour(cls, colour) -> None:
        cls._colour = colour
    
    def set_pos(cls, pos:list[int]) -> None:
        cls._pos = pos

    def __str__(cls) -> str:
        if cls._colour == "black":
            return cls._piece.lower()
        else:
            return cls._piece.upper()

    
class Pawn(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "p"
        self.double_move = False

    def get_legal_moves(cls, board):

        legal_moves = []

        direction = 0
        if cls._colour == "white":
            direction = -1
        else:
            direction = 1
        # straight
        if isinstance(board._rep[cls._pos[1]+direction][cls._pos[0]], Empty):
            legal_moves.append([cls._pos[0],cls._pos[1]+direction])
            start_row = 6 if direction == -1 else 2 
            if cls._pos[1] == start_row  and isinstance(board._rep[cls._pos[1]+direction*2][cls._pos[0]], Empty):
                legal_moves.append([cls._pos[0],cls._pos[1]+direction*2])
                
        
        # not straight
        left_square = None
        right_square = None
        if cls._pos[0] > 0:
            left_square = board._rep[cls._pos[1]+direction][cls._pos[0]-1] 
            if not isinstance(left_square,Empty):
                legal_moves.append(left_square._pos)
        if cls._pos[0] < 7:
            right_square = board._rep[cls._pos[1]+direction][cls._pos[0]+1]
            if not isinstance(right_square,Empty):
                legal_moves.append(right_square._pos)
        
        return legal_moves      

class Rook(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "r"
    
    def get_legal_moves(cls, board):
        #veritcal
        legal_moves = []
        #above
        i = 0
        currentSquare = board._rep[cls._pos[1]-1][cls._pos[0]]
        while isinstance(currentSquare, Empty) and cls._pos[1]+i > 0:
            i -= 1
            currentSquare = board._rep[cls._pos[1]+i][cls._pos[0]]
            legal_moves.append(currentSquare._pos)
        # if not isinstance(currentSquare, Empty):
        #     legal_moves.append(currentSquare._pos)

        #below
        i = 0
        currentSquare = board._rep[cls._pos[1]+1][cls._pos[0]]
        while isinstance(currentSquare, Empty) and cls._pos[1]+i < 7:
            i += 1
            currentSquare = board._rep[cls._pos[1]+i][cls._pos[0]]
            legal_moves.append(currentSquare._pos)
        # if not isinstance(currentSquare, Empty):
        #     legal_moves.append(currentSquare._pos)
    
        #horizontal left
        i = 0
        currentSquare = board._rep[cls._pos[1]][cls._pos[0]-1]
        while isinstance(currentSquare, Empty) and cls._pos[0]+i > 0:
            i -= 1
            currentSquare = board._rep[cls._pos[1]][cls._pos[0]+i]
            legal_moves.append(currentSquare._pos)
        # if not isinstance(currentSquare, Empty):
        #     legal_moves.append(currentSquare._pos)

        #right
        i = 0
        currentSquare = board._rep[cls._pos[1]][cls._pos[0]+1]
        while isinstance(currentSquare, Empty) and cls._pos[0]+i < 7:
            i += 1
            currentSquare = board._rep[cls._pos[1]][cls._pos[0]+i]
            legal_moves.append(currentSquare._pos)
            
            
        # if not isinstance(currentSquare, Empty):
        #     legal_moves.append(currentSquare._pos)
            
        return legal_moves



class Knight(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "n"


class Bishop(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "b"


class Queen(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "q"


class King(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "k"

class Empty(Piece):
    def __init__(self,colour = "", pos=[0,0]) -> None:
        super().__init__(colour,pos)
        self._piece = "e"
    def __str__(cls) -> str:
        return " "