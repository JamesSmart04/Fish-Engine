import Modules

class main():
    def __init__(self, FEN="rnbqkbnr/pppppppp/8/8/3R4/8/PPPPPPPP/1NBQKBNR b Kkq - 0 1") -> None:
        # setting the board
        self.board = Modules.board.Board(FEN)
        print(self.board)
        print(self.board.get_piece([3,3]).get_legal_moves(self.board))
    def __str__(self) -> str:
        pass
        

if __name__ == "__main__":
    game = main()