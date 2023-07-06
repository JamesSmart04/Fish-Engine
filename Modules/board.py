from Modules.Pieces import *
from Modules.misc import convert_pos, convert_pos_to_string

class Board:

    def __init__(self, FEN: str) -> None:
        self.set_board(FEN)
        self.en_passant_list = []


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
    

    def clear_en_passant_list(cls) -> None:
        cls.en_passant_list = []

    def get_en_passant_list(cls) -> list:
        return cls.en_passant_list

    def add_to_en_passanter_list(cls, pawn) -> None:
        cls.en_passant_list.append(pawn)
        

    def set_board(cls, FEN: str) -> None:
        rep = [[]]
        FEN_list = FEN.split(" ")
        FEN = FEN_list[0]
        castling_info = FEN_list[2]
        cls._white_castling_availibility = [int("K" in castling_info),int("Q" in castling_info)] 
        cls._black_castling_availibility = [int("k" in castling_info),int("q" in castling_info)]
        
        turn = -1 if FEN_list[1].lower() == "w" else 1 #0 means it is whites turn, 1 means it is black turn
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
                if isinstance(temp_piece, King): #storing king posito
                    if temp_piece._colour == "white":
                        cls._white_king_position = temp_piece._pos
                    else:
                        cls._black_king_position = temp_piece._pos

                rep[-1].append(temp_piece)
        cls._rep = rep
        cls._turn = turn
    
    def set_turn(cls, turn):
        cls._turn = turn

    def get_turn(cls):
        return "white" if cls._turn == -1 else "black"


    def get_legal_moves(cls):
        legal_moves = {}
        for i in range(len(cls._rep)):
            for j in range(len(cls._rep[0])):
                curPiece = cls._rep[i][j]              
                if not isinstance(curPiece, Empty) and curPiece.get_colour() == cls.get_turn():
                    legal_moves[convert_pos_to_string(curPiece.get_position())] = curPiece.get_legal_moves(cls)
        return legal_moves

    
    def update_position(cls) -> None:
        print(cls)
        legal_moves = cls.get_legal_moves()

        print("Select a piece to move: ", legal_moves)
        while True:
            movingPiece = input("Please select a square: ")                     
            if movingPiece in legal_moves:
                break
        piece_legal_moves = legal_moves[movingPiece]
        print(f"legal moves: {piece_legal_moves}")
        movingPiece = cls.get_piece(convert_pos(movingPiece))
        while True:
            targetPiece = input("please select a square to move to")
            if convert_pos(targetPiece) in piece_legal_moves:
                targetPiece = cls.get_piece(convert_pos(targetPiece))
                break
        targetPiecePositon = targetPiece.get_position()
        if isinstance(targetPiece, Empty):
            #adding to en passant list 
            if isinstance(targetPiece, Pawn) and abs(targetPiece.get_position()[1] - movingPiece.get_position()[1]) > 1:
                cls.add_to_en_passanter_list(movingPiece)
            cls._rep[targetPiecePositon[1]][targetPiecePositon[0]], cls._rep[movingPiece._pos[1]][movingPiece._pos[0]] = cls._rep[movingPiece._pos[1]][movingPiece._pos[0]],cls._rep[targetPiecePositon[1]][targetPiecePositon[0]]
            temp = targetPiecePositon
            targetPiece.set_pos([movingPiece._pos[0],movingPiece._pos[1]])
            movingPiece.set_pos([temp[0], temp[1]])
        else:
            tempPiece = Empty(pos=[movingPiece._pos[0],movingPiece._pos[1]])
            cls._rep[movingPiece._pos[1]][movingPiece._pos[0]] = tempPiece
            cls._rep[targetPiecePositon[1]][targetPiecePositon[0]] = movingPiece
            movingPiece.set_pos(targetPiecePositon)        
        cls._turn = cls._turn*-1
            
            
        


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
        elif piece.isupper():
            output.set_colour("white")
            return output
        else:
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
