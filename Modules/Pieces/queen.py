from .piece import Piece
from .bishop import Bishop
from .rook import Rook

class Queen(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "q"
        self._value = 900
    
    def get_legal_moves(cls, board):
        straight_moves = Rook(cls._colour, cls._pos).get_legal_moves(board)
        diagonal_moves = Bishop(cls._colour, cls._pos).get_legal_moves(board)

        for move in straight_moves:
            diagonal_moves.append(move)
        return diagonal_moves

