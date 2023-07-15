from .piece import Piece
from .rook import Rook
from .knight import Knight
class Queen(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "kn"
        self._value = 800
    
    def get_legal_moves(cls, board):
        knight_moves = Knight(cls._colour, cls._pos).get_legal_moves(board)
        rook_moves = Rook(cls._colour, cls._pos).get_legal_moves(board)

        for move in knight_moves:
            rook_moves.append(move)
        return rook_moves