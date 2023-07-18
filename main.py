import Modules
import copy
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
        #printing board initally
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


    def __str__(self) -> str:
        pass

if __name__ == "__main__":
    game = main("6K1/8/8/8/8/8/RR6/7k w - - 0 1")

#TODO figure out how to feed AI, back of our mind (evaulate board, evaulate position); check en passant interactions w/ new legal move filtering, stalemate, checkmate, 50 move clock

