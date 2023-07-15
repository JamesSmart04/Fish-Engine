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
        while True:
            legal_moves = self.board.get_legal_moves()
            player_legal_moves = copy.deepcopy(legal_moves)
            #making player legal moves| algebraic notation  
            for i in player_legal_moves:
                for j in range(len(player_legal_moves[i])):                
                    player_legal_moves[i][j] = Modules.misc.convert_pos_to_string(player_legal_moves[i][j])


            print("Select a piece to move: ", player_legal_moves)

            while True:
                pos_of_moving_piece = input("Please select a square: ")
                if pos_of_moving_piece in legal_moves:
                    break
            piece_legal_moves = player_legal_moves[pos_of_moving_piece]
            print(f"legal moves: {piece_legal_moves}")
            
            moving_piece = self.board.get_piece(Modules.misc.convert_pos(pos_of_moving_piece))
            while True:
                target_piece = input("please select a square to move to: ")
                print(Modules.misc.convert_pos(target_piece))
                print(legal_moves[pos_of_moving_piece])
                if Modules.misc.convert_pos(target_piece) in legal_moves[pos_of_moving_piece]:
                    target_piece = self.board.get_piece(Modules.misc.convert_pos(target_piece))
                    break

            self.board.update_position(moving_piece,target_piece)



    def __str__(self) -> str:
        pass

if __name__ == "__main__":
    game = main("8/5r2/5N2/5K2/8/k7/8/8 w - - 0 1")

#TODO figure out how to feed AI, back of our mind (evaulate board, evaulate position); check en passant interactions w/ new legal move filtering, stalemate, checkmate, 50 move clock

