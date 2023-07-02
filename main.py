import Modules
class main():
    def __init__(self, FEN="rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Kkq - 0 1") -> None:
        # setting the board
        self.board = Modules.board.Board(FEN)
        print(self.board)
        cur_piece = self.board.get_piece([4,5])
        cur_piece.update_position(cur_piece.get_legal_moves(self.board),self.board)

        print(self.board)
        
    def __str__(self) -> str:
        pass
    #yes i do 
        
if __name__ == "__main__":
    game = main("8/4r3/2b1K3/8/8/8/8/8 w - - 0 1") 
 
