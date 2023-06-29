class Piece:
    def __init__(self, colour="W", pos=[0,0]) -> None:
        self._pos = pos
        self._colour = colour
        self._piece = ""
    
    def set_colour(cls, colour) -> None:
        cls._colour = colour
    
    def __str__(cls) -> str:
        if cls._colour == "black":
            return cls._piece.lower()
        else:
            return cls._piece.upper()

    
class Pawn(Piece):
    def __init__(self, colour="W", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "p"


class Rook(Piece):
    def __init__(self, colour="W", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "r"


class Knight(Piece):
    def __init__(self, colour="W", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "n"


class Bishop(Piece):
    def __init__(self, colour="W", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "b"


class Queen(Piece):
    def __init__(self, colour="W", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "q"


class King(Piece):
    def __init__(self, colour="W", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "k"