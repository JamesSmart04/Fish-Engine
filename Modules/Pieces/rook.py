from .piece import Piece
from .empty import Empty


class Rook(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "r"
        self._value = 500
    
    def get_legal_moves(cls, board):
        #veritcal
        legal_moves = []

        #above
        i = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[1]+i > 0:
            i -= 1
            currentSquare = board._rep[cls._pos[1]+i][cls._pos[0]]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)


        #below
        i = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[1]+i < 7:
            i += 1
            currentSquare = board._rep[cls._pos[1]+i][cls._pos[0]]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)

    
        #horizontal left
        i = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[0]+i > 0:
            i -= 1
            currentSquare = board._rep[cls._pos[1]][cls._pos[0]+i]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)

        #right
        i = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[0]+i < 7:
            i += 1
            print(cls._pos[0]+i)
            currentSquare = board._rep[cls._pos[1]][cls._pos[0]+i]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)
            
            
        # if not isinstance(currentSquare, Empty):
        #     legal_moves.append(currentSquare._pos)
            
        return legal_moves
