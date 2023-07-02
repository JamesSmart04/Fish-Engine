from .piece import Piece

#cinna what aren't you tell
class Empty(Piece):
    def __init__(self,colour = "empty", pos=[0,0]) -> None:
        super().__init__(colour,pos)
        self._piece = "e"
    def __str__(cls) -> str:
        return " "