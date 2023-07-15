import Modules.misc

class Piece:
    def __init__(self, colour="white", pos=[0,0]) -> None:
        self._pos = pos
        self._colour = colour
        self._piece = ""
    
    def get_colour(cls) -> str:
        return cls._colour
    
    def get_position(cls) -> list:
        return cls._pos         

    def set_colour(cls, colour) -> None:
        cls._colour = colour
    
    def set_pos(cls, pos:list[int]) -> None:
        cls._pos = pos

    def __str__(cls) -> str:
        if cls._colour == "black":
            return cls._piece.lower()
        else:
            return cls._piece.upper()
