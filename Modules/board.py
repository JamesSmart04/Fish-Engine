from Modules.pieces import *

class Board:

    def __init__(self, FEN: str) -> None:
        self.set_board(FEN)


    def __str__(cls) -> str: #prints board to console and returns FEN
        out = []
        #printing for console
        for i in range(len(cls._rep)):
            print(len(cls._rep)-1-i,[str(j) for j in cls._rep[i]],i) 
            out += cls._rep[i]
        return cls.export_FEN()


    def get_board(cls) -> list[list]:
        """Returns 2D array of objects used to represent the chess board"""
        return cls._rep
    

    def get_piece(cls, pos: list) -> Piece:
        #pos[0] == horizontal, pos[1] == vertical
        if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
            print(f'{pos} is invalid')
            return False
        return cls._rep[7-pos[1]][pos[0]]

    def set_board(cls, FEN: str) -> None:
        rep = [[]*8]
        FEN = FEN.split(" ")[0]
        for i in FEN:
            if i == "/":
                rep.append([])
            elif i in "1234567890":
                for _ in range(int(i)):
                    empty_piece = cls.generate_piece(i)
                    empty_piece.set_pos([len(rep[-1]),len(rep)-1])
                    rep[-1].append(empty_piece)
            else:
                temp_piece = cls.generate_piece(i)
                temp_piece.set_pos([len(rep[-1]),len(rep)-1])
                if isinstance(temp_piece, Bishop):
                    print(temp_piece._pos)
                rep[-1].append(temp_piece)
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
            case _ : output = Empty()
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
                while(j < len(cls._rep[i]) and  isinstance(cls._rep[i][j],Empty)):
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