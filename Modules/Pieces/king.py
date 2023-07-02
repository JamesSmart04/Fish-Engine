from .piece import Piece
from .queen import Queen
from .bishop import Bishop
from .empty import Empty
from .rook import Rook
import Modules.misc
class King(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "k"
    def set_attacked_squares(cls, board):
        #primarly used to check pinning and checking 
        cur_colour = ""
        cls.diagonal_squares = []
        cls.horizontal_squares = []
        #checking above
        def checkDirection(directionX, directionY):
            x = directionX
            y = directionY
            current_piece = None
            seen_friend = False
            seen_enemy = False
            file_squares = []
            while cls._pos[1]+y >= 0 and cls._pos[1]+y <=7 and cls._pos[0]+x >= 0 and cls._pos[0]+ x <= 7:
                current_piece : Piece = board._rep[cls._pos[1]+y][cls._pos[0]+x]
                file_squares.append(current_piece.get_position())
                isEmpty = isinstance(current_piece, Empty) 
                
                if not isEmpty and current_piece.get_colour() != cls._colour:
                    seen_enemy = True

                if seen_enemy == True: #if king is checked, #why ?
                    if isinstance(current_piece, Queen):
                        return file_squares
                    elif directionX != 0 and directionY != 0 and isinstance(current_piece, Bishop): #ye I saw kinda cringe tbh  
                        return file_squares
                    elif isinstance(current_piece, Rook): #that's really dumb reddit and twitter are going dumb "going dumb"
                        return file_squares
                    else:
                        return []
                     
                elif not isEmpty and seen_friend == True and current_piece.get_colour() == cls._colour: #two frinedly pieces
                    break

                elif cls != current_piece and current_piece.get_colour()  == cls._colour:
                    seen_friend = True

                x += directionX
                y += directionY
            return []

     
        # def checkLeft(direction)
            #where did I try to iterate ???
        cls.horizontal_squares += checkDirection(0,-1) #above
        cls.horizontal_squares += checkDirection(0,1) #below 
        cls.horizontal_squares += checkDirection(-1,0) #left
        cls.horizontal_squares += checkDirection(1,0) #right
        cls.diagonal_squares += checkDirection(1,1) #bottom right
        cls.diagonal_squares += checkDirection(-1,1) #bottom left
        cls.diagonal_squares += checkDirection(1,-1) #top right
        cls.diagonal_squares += checkDirection(-1,-1) #top left

        #adding in the kings position for checking purposes
        if cls.horizontal_squares != []:
            cls.horizontal_squares += [cls._pos]
        if cls.diagonal_squares != []:
            cls.diagonal_squares += [cls._pos]
        
               

    def get_diagonal_attacked_squares(cls):
        return cls.diagonal_squares

    def get_horizontal_attacked_squares(cls):
        return cls.horizontal_squares

    def get_legal_moves(cls,board):
        #top row
        #making sure the king isn't at the top of the board
        legal_moves = []

        for i in [-1,1]:
            if ((cls._pos[0]+i >= 0 and cls._pos[0]+i <= 7) 
            and (isinstance(board._rep[cls._pos[1]][cls._pos[0]+i], Empty) 
            or board._rep[cls._pos[1]][cls._pos[0]+i].get_colour() != cls._colour)):
                legal_moves.append(board._rep[cls._pos[1]][cls._pos[0]+i].get_position())
                
        if cls._pos[1] > 0:
            for i in [-1,0,1]:
                if ((cls._pos[0]+i >= 0 and cls._pos[0]+i <= 7) 
                and (isinstance(board._rep[cls._pos[1] - 1][cls._pos[0]+i], Empty) 
                or board._rep[cls._pos[1] - 1][cls._pos[0]+i].get_colour() != cls._colour)):
                    legal_moves.append(board._rep[cls._pos[1] - 1][cls._pos[0]+i].get_position())



        if cls._pos[1] < 7:
            for i in [-1,0,1]:
                if ((cls._pos[0]+i >= 0 and cls._pos[0]+i <= 7) 
                and (isinstance(board._rep[cls._pos[1] + 1][cls._pos[0]+i], Empty) 
                or board._rep[cls._pos[1] + 1][cls._pos[0]+i].get_colour() != cls._colour)):
                    legal_moves.append(board._rep[cls._pos[1] + 1][cls._pos[0]+i].get_position())
        

        return legal_moves
    

    def update_position(cls, legal_moves, board) -> None:
        print("Select move: ", legal_moves)
        while True:
            selected_move_x = input("Please select a x: ")
            selected_move_y = input("please, select a y: ")
            
            selected_move = Modules.misc.convert_pos([selected_move_x,int(selected_move_y)])
            if selected_move in legal_moves:
                break
        targetPiece = board._rep[selected_move[1]][selected_move[0]]
        targetPiecePositon = targetPiece.get_position()
        if isinstance(targetPiece, Empty):
            board._rep[targetPiecePositon[1]][targetPiecePositon[0]], board._rep[cls._pos[1]][cls._pos[0]] = board._rep[cls._pos[1]][cls._pos[0]],board._rep[targetPiecePositon[1]][targetPiecePositon[0]]
            temp = targetPiecePositon
            targetPiece.set_pos(cls._pos)
            cls.set_pos([temp[0], temp[1]])
        else:
            tempPiece = Empty(pos=[cls._pos[0],cls._pos[1]])
            board._rep[cls._pos[1]][cls._pos[0]] = tempPiece
            board._rep[targetPiecePositon[1]][targetPiecePositon[0]] = cls
            cls.set_pos(targetPiecePositon)        
            
            
        