import Modules

class main():
    def __init__(self, FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Kkq - 0 1") -> None:
        # setting the board
        self.board = Modules.board.Board(FEN)
        print(self.board)
        self.board.get_piece([4,4]).set_attacked_squares(self.board)
        print(self.board.get_piece([4,4]).get_horizontal_attacked_squares())
        
    def __str__(self) -> str:
        pass
        

if __name__ == "__main__":
    game = main("4r3/4P3/1N6/r3K3/8/8/8/4P3 w - - 0 1")