import Modules
class main():
    def __init__(self, FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Kkq - 0 1") -> None:
        # setting the board
        self.board = Modules.board.Board(FEN)
        # print(Modules.misc.convert_pos(Modules.misc.convert_pos_to_string(self.board.get_piece([0,0]).get_position())))
        # print(self.board)
        # print(self.board.get_turn())
        # white_king = self.board.get_piece([4,0])
        # print(white_king.get_legal_moves(self.board))
        #usinag a dictionary {key: position of piece: value legal_moves}

        while True:
            self.board.update_position()
            print(self.board)
            print("white: ",self.board._white_castling_availibility)
            print("black: ",self.board._black_castling_availibility)


    def __str__(self) -> str:
        pass
    #yes i do 
        
if __name__ == "__main__":
    game = main("r3k2r/71/8/8/8/8/B7/R3K2R w KQkq - 0 1")

#TODO Make gameplay loop, and figure out how to feed AI, back of our mind (castling, evaulate board, evaulate position)