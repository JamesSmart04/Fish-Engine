class Piece:
    def __init__(self, colour="W", pos=[0,0]):
        self._pos = pos
        self._colour = colour
    
    def set_colour(cls, colour):
        cls._colour = colour

    
class Pawn(Piece):
    def __str__(cls):
        if cls._colour == "black":
            return "p"
        else:
            return "P"
        
class Rook(Piece):
    def __str__(cls):
        if cls._colour == "black":
            return "r"
        else:
            return "R"
        
class Knight(Piece):
    def __str__(cls):
        if cls._colour == "black":
            return "n"
        else:
            return "N"
        
class Bishop(Piece):
    def __str__(cls):
        if cls._colour == "black":
            return "b"
        else:
            return "B"
        
class Queen(Piece):
    def __str__(cls):
        if cls._colour == "black":
            return "q"
        else:
            return "Q"
        
class King(Piece):
    def __str__(cls):
        if cls._colour == "black":
            return "k"
        else:
            return "K"

