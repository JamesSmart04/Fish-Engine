import Modules

class main():
    def __init__(self, FEN="rnbqkbnr/pppppp/8/8/8/8/PPPPPPPP/RNBQKBNR b Kkq - 0 1") -> None:
        # setting the board
        self.board = Modules.board.Board(FEN)
        print(self.board)
        print(self.board.get_piece([7,0]).get_legal_moves(self.board))
    def __str__(self) -> str:
        pass
        

if __name__ == "__main__":
    game = main("8/8/8/8/8/8/6K1/7B w - - 0 1")