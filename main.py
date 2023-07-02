import Modules
class main():
    def __init__(self, FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Kkq - 0 1") -> None:
        # setting the board
        self.board = Modules.board.Board(FEN)
        print(self.board)
        self.board.get_piece([4,3]).set_attacked_squares(self.board)
        print(self.board.get_piece([4,3]).get_horizontal_attacked_squares()) 
        print(self.board.get_piece([4,3]).get_diagonal_attacked_squares())  
        
    def __str__(self) -> str:
        pass
    #yes i do 
        
if __name__ == "__main__":
    game = main("8/4r3/2b5/8/4K3/8/8/8 w - - 0 1") 
 
