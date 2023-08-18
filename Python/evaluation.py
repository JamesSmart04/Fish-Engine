import Modules

class eval:
    def __init__(self) -> None:
        self.endgame = False
        
        self.valueTable = {
            "P" : ((0, 0, 0, 0, 0, 0, 0, 0),
                   (50, 50, 50, 50, 50, 50, 50, 50),
                   (10, 10, 20, 30, 30, 20, 10, 10),
                   (5,  5, 10, 26, 25, 10,  5,  5),
                   (0,  0,  0, 25, 20,  0,  0,  0),
                   (5, 5, -10,  0,  0, -10, 5, 5),
                   (5, 10, 10, -20, -20, 10, 10, 5),
                   (0, 0, 0, 0, 0, 0, 0, 0)
                ),

            "N" : ((-50,-40,-30,-30,-30,-30,-40,-50),
                   (-40,-20,  0,  0,  0,  0,-20,-40),
                   (-30,  0, 10, 15, 15, 10,  0,-30),
                   (-30,  5, 15, 16, 15, 15,  5,-30),
                   (-30,  0, 15, 15, 15, 15,  0,-30),
                   (-30,  5, 13, 11, 11, 15,  5,-30),
                   (-40,-20,  0,  5,  5,  0,-20,-40),
                   (-50,-40,-30,-30,-30,-30,-40,-50)
                ),
            "B" : ((-20,-10,-10,-10,-10,-10,-10,-20),
                   (-10,  0,  0,  0,  0,  0,  0,-10),
                   (-10,  0,  5, 10, 10,  5,  0,-10),
                   (-10,  5,  5, 10, 10,  5,  5,-10),
                   (-10,  0, 10, 10, 10, 10,  0,-10),
                   (-10, 10, 10, 10, 10, 10, 10,-10),
                   (-10,  11,  0,  0,  0,  0,  11,-10),
                   (-20,-10,-10,-10,-10,-10,-10,-20)
                ),
            "R" : ((0,  0,  0,  0,  0,  0,  0,  0),
                   (5, 10, 10, 10, 10, 10, 10,  5),
                   (-5,  0,  0,  0,  0,  0,  0, -5),
                   (-5,  0,  0,  0,  0,  0,  0, -5),
                   (-5,  0,  0,  0,  0,  0,  0, -5),
                   (-5,  0,  0,  0,  0,  0,  0, -5),
                   (-5,  0,  0,  0,  0,  0,  0, -5),
                   (0,  0,  0,  10,  5,  10,  0,  0)
                ),
            "Q" : ((-20,-10,-10, -5, -5,-10,-10,-20),
                   (-10,  0,  0,  0,  0,  0,  0,-10),
                   (-10,  0,  5,  5,  5,  5,  0,-10),
                   (-5,  0,  5,  5,  5,  5,  0, -5),
                   (0,  0,  5,  5,  5,  5,  0, -5),
                   (-10,  5,  5,  5,  5,  5,  0,-10),
                   (-10,  0,  5,  0,  0,  0,  0,-10),
                   (-20,-10,-10, -5, -5,-10,-10,-20)
                ),
            "K" : ((-30,-40,-40,-50,-50,-40,-40,-30),
                   (-30,-40,-40,-50,-50,-40,-40,-30),
                   (-30,-40,-40,-50,-50,-40,-40,-30),
                   (-30,-40,-40,-50,-50,-40,-40,-30),
                   (-20,-30,-30,-40,-40,-30,-30,-20),
                   (-10,-20,-20,-20,-20,-20,-20,-10),
                   (20, 20,  0,  0,  0,  0, 20, 20),
                   (20, 32, 30,  0,  0, 10, 35, 20)
                ),
            "Ke" : ((-50,-40,-30,-20,-20,-30,-40,-50),
                    (-30,-20,-10,  0,  0,-10,-20,-30),
                    (-30,-10, 20, 30, 30, 20,-10,-30),
                    (-30,-10, 30, 40, 40, 30,-10,-30),
                    (-30,-10, 30, 40, 40, 30,-10,-30),
                    (-30,-10, 20, 30, 30, 20,-10,-30),
                    (-30,-30,  0,  0,  0,  0,-30,-30),
                    (-50,-30,-30,-30,-30,-30,-30,-50)
                ),
            " " : ((0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))
        }

    def isEndGame(cls, Board : Modules.board.Board):
        # check if the game is now in an endgame
        # an endgame is defined as: both sides have no queen or, each side that has a queen only has queen + 1 minor piece
        white_queen_counter = 0
        black_queen_counter = 0
        white_minor_counter = 0
        black_minor_counter = 0
        
        # checking if both sides have a queen:
        for row in Board._rep:
            for square in row:
                if isinstance(square, Modules.Queen):
                    # the piece is a queen
                    if square.get_colour() == "white":
                        white_queen_counter += 1
                    else:
                        black_queen_counter += 1
                
                if white_queen_counter >= 1 and black_queen_counter >= 1:
                    # both sides have a queen
                    return False

                if square._value > 100 and square._value < 900:
                    # this means it is a minor piece: bishop, knight, rook
                    if square.get_colour() == "white":
                        white_minor_counter += 1
                    else:
                        black_minor_counter += 1

        if white_queen_counter >= 1 and white_minor_counter > 1:
            return False
        elif black_queen_counter >= 1 and black_minor_counter > 1:
            return False
        return True

    
    def materialEval(cls, Board : Modules.board.Board):
        sum_of_position = 0
        
        if not cls.endgame:
            cls.endgame = cls.isEndGame(Board)
        
        # evaluating material
        for row in Board._rep:
            for square in row:
                piece_char = "Ke" if str(square).upper() == "K" and cls.endgame else str(square).upper()
                # getting the valueTable for the piece:
                piece_value_table = cls.valueTable[piece_char]
                
                # flips the value table if the piece colour is black, and grabs the position bonus based on the pieces pos
                position_bonus = piece_value_table[::-1][square._pos[1]][square._pos[0]] if square._colour == "black" else piece_value_table[square._pos[1]][square._pos[0]]
                      
                square_val = ((square._value+position_bonus)*-1) if square.get_colour() == "black" else (square._value+position_bonus)
                    
                
                sum_of_position += square_val
        return sum_of_position

        
    def evalPosition(cls, Board : Modules.board.Board):
        finished_eval = 0
        finished_eval += cls.materialEval(Board)
        
        # evaluating mobility (how many legal moves each side has)
        white_mobility_score = Board.get_legal_moves()
        white_checked = Board.get_white_checked()
        Board.change_turn()
        black_mobility_score = Board.get_legal_moves()
        black_checked = Board.get_black_checked()
        Board.change_turn()
        
        finished_eval += 0.2 * (len(white_mobility_score) - len(black_mobility_score))
        
        cur_state = Board.get_game_state()
        if cur_state != "active":
            cur_turn  = Board.get_turn()
            if cur_turn == 'white':
                if Board.get_game_state() == "Checkmate":
                    return float('-inf')
                else:
                    return 0
            else:
                if Board.get_game_state() == "Checkmate":
                    return float('inf')
                else:
                    return 0

        # if white_mobility_score == 0:
        #     if white_checked:
        #         # black wins from checkmate:
        #         return float("-inf")
        #     else:
        #         return 0
        
        # elif black_mobility_score == 0:
        #     if black_checked:
        #         # white wins from checkmate:
        #         return float("inf")
        #     else:
        #         return 0
        return finished_eval