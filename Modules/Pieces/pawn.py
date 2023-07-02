from .piece import Piece #no glue

class Pawn(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "p"
        self.double_move = False

    def get_legal_moves(cls, board):

        legal_moves = []

        direction = 1
        if cls._colour == "white" : direction = -1

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