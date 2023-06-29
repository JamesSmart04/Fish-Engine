from Modules.pieces import *

class Board:

    def __init__(self, FEN: str) -> None:
        self.set_board(FEN)


    def __str__(cls) -> str: #prints board to console and returns FEN
        out = []
        #printing for console
        for i in range(len(cls._rep)):
            print([str(j) for j in cls._rep[i]]) 
            out += cls._rep[i]
        return cls.export_FEN()


    def get_board(cls) -> list[list]:
        """Returns 2D array of objects used to represent the chess board"""
        return cls._rep


    def set_board(cls, FEN: str) -> None:
        rep = [[]]
        FEN = FEN.split(" ")[0]
        for i in FEN:
            if i == "/":
                rep.append([])
            elif i in "1234567890":
                for _ in range(int(i)):
                    rep[-1].append(" ")
            else:
                rep[-1].append(cls.generate_piece(i))
        cls._rep = rep


    def generate_piece(cls, piece: str) -> Piece:
        output = None
        match piece.lower():
            case "p" : output = Pawn()
            case "r" : output = Rook()
            case "n" : output = Knight()
            case "b" : output = Bishop()
            case "q" : output = Queen()
            case "k" : output = King()  
        if piece.islower():
            output.set_colour("black")
            return output
        else:
            output.set_colour("white")
            return output


    def export_FEN(cls) -> str:
        FEN = ""
        for i in range(len(cls._rep)):
            j = 0
            while j < len(cls._rep[i]):
                count = 0
                while(j < len(cls._rep[i]) and cls._rep[i][j] == " " ):
                    count+= 1
                    j += 1
                if count != 0:
                    FEN += str(count)
                else:
                    FEN += str(cls._rep[i][j])
                    j+= 1

            if i != len(cls._rep)-1:
                FEN += "/"
        return FEN
