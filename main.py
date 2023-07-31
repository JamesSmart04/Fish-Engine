import Modules
from uci import Uci

class Main():
    def __init__(self, FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Kkq - 0 1") -> None:
        # setting the board
        # print(Modules.misc.convert_pos(Modules.misc.convert_pos_to_string(self.board.get_piece([0,0]).get_position())))
        # print(self.board)
        # print(self.board.get_turn())
        # white_king = self.board.get_piece([4,0])
        # print(white_king.get_legal_moves(self.board))
        #usinag a dictionary {key: position of piece: value legal_moves}
        #printing board initally
        
        mode = input("")
        
        if mode != "uci":
            self.board = Modules.board.Board(FEN)
            print(self.board)
            print(self.board._game_state)
            while True and self.board.get_game_state() == "active":

                legal_moves = self.board._legal_moves

                player_legal_moves = legal_moves
                #making player legal moves| algebraic notation  

                print("Select a piece to move: ", player_legal_moves)

                while True:
                    move = input("Please select a square: ")
                    if move in legal_moves:
                        break
                    pass

                self.board.update_position(move)
                print(self.board)
            print(self.board)
        
        elif mode == "uci":
            game = Uci()


    def __str__(self) -> str:
        pass

if __name__ == "__main__":
    game = Main("")

#TODO: fix bug causing legal moves to be arrays of values larger than 2, improve eval function to account for centre control, connectedness, pawn structures, set up playing against itself to tune eval factors, opening book

