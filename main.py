import Modules

class main():
    def __init__(self, FEN="rnbqkbnr/pppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b Kkq - 0 1") -> None:
        # setting the board
        self.board = Modules.board.Board(FEN)
        print(self.board)
        print(self.board.get_piece([6,7]).get_legal_moves(self.board))
    def __str__(self) -> str:
        pass
        

if __name__ == "__main__":
    game = main("6K1/8/8/8/8/8/8/8 w - - 0 1")