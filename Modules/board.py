from Modules.Pieces import *
from Modules.misc import convert_pos, convert_pos_to_string
import copy

class Board:

    def __init__(self, FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Kkq - 0 1") -> None:
        self._white_checked = False
        self._black_checked = False
        self.black_en_passant_list = []
        self.white_en_passant_list = []
        self._game_state = "active"
        self.set_board(FEN)




    def __str__(cls) -> str: #prints board to console and returns FEN
        out = []
        #printing for console
        for i in range(len(cls._rep)):
            print(len(cls._rep)-i,[str(j) for j in cls._rep[i]],i) 
            out += cls._rep[i]
        return cls.export_FEN()


    def export_FEN(cls) -> str: #TODO update w/ castling availbility and turn, not quite halfmove clock yet, also need to read possible en-passant squares
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
    

    def get_board(cls) -> list[list]:
        """Returns 2D array of objects used to represent the chess board"""
        return cls._rep
    

    def get_piece(cls, pos: list) -> Piece:
        """Takes an input of position (pos[0] = x, pos[1] = y) and returns piece object from board"""
        #pos[0] == horizontal, pos[1] == vertical
        if pos[0] < 0 or pos[0] > 7 or pos[1] < 0 or pos[1] > 7:
            return False
        return cls._rep[pos[1]][pos[0]]


    def get_black_en_passant_list(cls) -> list:
        return cls.black_en_passant_list
    
    def get_white_en_passant_list(cls) -> list:
        return cls.white_en_passant_list
    
    def get_white_checked(cls) -> bool:
        return cls._white_checked
    
    def get_black_checked(cls) -> bool:
        return cls._black_checked
    
    def get_turn(cls):
        return "white" if cls._turn == -1 else "black"
    
    def get_game_state(cls):
        return cls._game_state
    
    def set_game_state(cls,state):
        cls._game_state = state


    def get_legal_moves(cls):
        cls.set_king_attacked_squares()
        #checking if the king is in check
        cur_king = cls._white_king if cls._turn == -1 else cls._black_king
        if cur_king.check_attacked_squares(cur_king._pos,cls, cur_king._colour, False) != [[],[],[],[],[]]:
            if cls._turn == -1:
                cls._white_checked = True
            else:
                cls._black_checked = True 
        legal_moves = {}
        for i in range(len(cls._rep)):
            for j in range(len(cls._rep[0])):
                curPiece = cls._rep[i][j]              
                if not isinstance(curPiece, Empty) and curPiece.get_colour() == cls.get_turn():
                    legal_moves[convert_pos_to_string(curPiece.get_position())] = curPiece.get_legal_moves(cls)
        temp = []
        for i in legal_moves:
            if legal_moves[i]:
                for j in legal_moves[i]:
                    temp.append(i+convert_pos_to_string(j))
            else:
                continue
        legal_moves = temp
        return legal_moves

    def set_king_attacked_squares(cls) -> None:
        if cls.get_turn() == "white":
            cls._king_attacked_squares = cls._white_king.check_attacked_squares(cls._white_king.get_position(),cls,cls._white_king.get_colour())
        else:
            cls._king_attacked_squares = cls._black_king.check_attacked_squares(cls._black_king.get_position(),cls,cls._black_king.get_colour())
    
    def get_king_attacked_squares(cls):
        return cls._king_attacked_squares
    
    def clear_white_en_passant_list(cls) -> None:
        cls.white_en_passant_list = []
    
    def clear_black_en_passant_list(cls) -> None:
        cls.black_en_passant_list = []


    def add_to_black_en_passant_list(cls, pawn_pos) -> None:
        cls.black_en_passant_list.append(pawn_pos)


    def add_to_white_en_passant_list(cls, pawn_pos) -> None:
        cls.white_en_passant_list.append(pawn_pos)


    def set_turn(cls, turn):
        cls._turn = turn


    def set_board(cls, FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Kkq - 0 1") -> None:
        """iterates through the FEN string generating piece objects based on the current
        character of an FEN string. Then stores the board as cls.board and stores castling info
        """
        rep = [[]]
        FEN_parts = FEN.split(" ")
        FEN = FEN_parts[0]
        castling_info = FEN_parts[2]
        cls._white_castling_availibility = [int("K" in castling_info),int("Q" in castling_info)] 
        cls._black_castling_availibility = [int("k" in castling_info),int("q" in castling_info)]
        
        turn = -1 if FEN_parts[1].lower() == "w" else 1 #0 means it is whites turn, 1 means it is black turn
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
                        cls._white_king = temp_piece
                    else:
                        cls._black_king  = temp_piece

                rep[-1].append(temp_piece)
        cls._rep = rep
        cls._turn = turn
        cls._legal_moves = cls.get_legal_moves()


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


    def update_position(cls,moveString) -> None: 
        moving_piece = moveString[0:2]
        target_piece = moveString[2:4]
        if len(moveString) > 4:
            promo = moveString[4]


        moving_piece = cls.get_piece(convert_pos(moving_piece))
        target_piece = cls.get_piece(convert_pos(target_piece))
        target_piece_position = target_piece.get_position()
        if not isinstance(target_piece, Empty):
            # if the targetted piece is not empty (it is an enemy piece) then replace it with an empty piece
            temp_piece = Empty(pos=[moving_piece._pos[0],moving_piece._pos[1]])
            cls._rep[target_piece_position[1]][target_piece_position[0]] = temp_piece


        direction = 1 if cls.get_turn() == "black" else -1
        en_passant_list = cls.get_black_en_passant_list() if direction == -1 else cls.get_white_en_passant_list()
        en_passant_piece = cls.get_piece([target_piece_position[0], target_piece_position[1]-direction])
        if isinstance(moving_piece, Pawn) and en_passant_piece.get_position() in en_passant_list:
            # this means the pawn performed en passant
            temp_piece = Empty(pos=en_passant_piece.get_position())
            cls._rep[en_passant_piece._pos[1]][en_passant_piece._pos[0]] = temp_piece


        if isinstance(moving_piece, Pawn) and abs(target_piece.get_position()[1] - moving_piece.get_position()[1]) > 1:
            #adding to en passant list if the piece moves 2 squares forward
            temp = [moving_piece.get_position()[0], moving_piece.get_position()[1]+(direction*2)]
            cls.add_to_black_en_passant_list(temp) if direction == 1 else cls.add_to_white_en_passant_list(temp)

        # swapping the target square (empty piece) with moving piece (actually moving)
        cls._rep[target_piece_position[1]][target_piece_position[0]], cls._rep[moving_piece._pos[1]][moving_piece._pos[0]] \
            = \
        cls._rep[moving_piece._pos[1]][moving_piece._pos[0]],cls._rep[target_piece_position[1]][target_piece_position[0]]

        #logic for castling
        if isinstance(moving_piece, King):
            difference = target_piece.get_position()[0] - moving_piece.get_position()[0]
            if abs(difference)>1: #king is trying to castle
                if difference < 0: #Queen side castling, only need to update the position of the rook
                    rook_to_move = cls._rep[moving_piece.get_position()[1]][0]
                    rook_to_move.set_pos([3,moving_piece.get_position()[1]])
                    cls._rep[moving_piece.get_position()[1]][0], cls._rep[moving_piece.get_position()[1]][3] = cls._rep[moving_piece.get_position()[1]][3], cls._rep[moving_piece.get_position()[1]][0]
                    cls._rep[moving_piece.get_position()[1]][0].set_pos([0,moving_piece.get_position()[1]])

                else: #king side castling
                    rook_to_move = cls._rep[moving_piece.get_position()[1]][7]
                    rook_to_move.set_pos([5,moving_piece.get_position()[1]])
                    cls._rep[moving_piece.get_position()[1]][7], cls._rep[moving_piece.get_position()[1]][5] = cls._rep[moving_piece.get_position()[1]][5], cls._rep[moving_piece.get_position()[1]][7]
                    cls._rep[moving_piece.get_position()[1]][7].set_pos([7,moving_piece.get_position()[1]])
            
            
            #amking castiling unavaialbe for colour as the king has moved
            if cls.get_turn() == "white":
                cls._white_castling_availibility = [0,0]
            else: 
                cls._black_castling_availibility =[0,0]

        
        #chaninging castling availibility

        if isinstance(moving_piece,Rook):
                
                index =-1
                if moving_piece.get_position()[0] == 0:
                    index = 1
                elif moving_piece.get_position()[0] == 7:
                    index =  0
                if index != -1:
                    if cls.get_turn() == "white":
                        cls._white_castling_availibility[index] = 0
                    else:
                        cls._black_castling_availibility[index] = 0
        # changing the stored positions of the pieces involved in the move :)
        temp = target_piece_position
        target_piece.set_pos([moving_piece._pos[0],moving_piece._pos[1]])
        moving_piece.set_pos([temp[0], temp[1]])


        promoRank = 7 if cls._turn == 1 else 0

        if isinstance(moving_piece, Pawn) and moving_piece.get_position()[1] == promoRank:
            cls.pawn_promotion(moving_piece,promo)


        cls._turn = cls._turn*-1 #changing to opposite turn
        cls._white_checked = False
        cls._black_checked = False

        cls._legal_moves = cls.get_legal_moves()   
        #print(cls._legal_moves)  
        #chekcing if the game should end 
        cur_check = cls._white_checked if cls._turn == -1 else cls._black_checked
        game_over = True
        if cls._legal_moves != []:
                game_over = False
                
                
        cur_king = cls._white_king if cls._turn == -1 else cls._black_king
        if cur_king.check_attacked_squares(cur_king._pos,cls, cur_king._colour, False) != [[],[],[],[],[]]:
            if cls._turn == -1:
                cls._white_checked = True
            else:
                cls._black_checked = True    

        if game_over:
            if cur_check:
                cls.set_game_state("Checkmate")
            else:
                cls.set_game_state("Stalemate")
        
        if cls._game_state != "active":
            return
        
        # if the next turn is black then the black pawn list needs to be cleared, else clear the other one
        if cls.get_turn() == "black":
            cls.clear_black_en_passant_list()
        else:
            cls.clear_white_en_passant_list()
    
    
    def pawn_promotion(cls, promotion_pawn,promoTo):
        #please select a piece
        
        promo_dict = {
            "q" : Queen(colour=promotion_pawn.get_colour(), pos = promotion_pawn.get_position()),
            "r" : Rook(colour=promotion_pawn.get_colour(), pos = promotion_pawn.get_position()),
            "b" : Bishop(colour=promotion_pawn.get_colour(), pos = promotion_pawn.get_position()),
            "n ": Knight(colour=promotion_pawn.get_colour(), pos = promotion_pawn.get_position())
        }
        cls._rep[promotion_pawn.get_position()[1]][promotion_pawn.get_position()[0]] = promo_dict[promoTo.lower()]
        return


            