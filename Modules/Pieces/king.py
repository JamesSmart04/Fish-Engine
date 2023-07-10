from .piece import Piece
from .queen import Queen
from .bishop import Bishop
from .knight import Knight
from .empty import Empty
from .rook import Rook
from .pawn import Pawn
from Modules.misc import convert_pos_to_string
def check_attacked_squares(pos,board, colour,isKing = True):
                cls  = board.get_piece(pos)
                def helper(directionX, directionY, board):
                    x = directionX
                    y = directionY
                    cls  = board.get_piece(pos)
                    current_piece = None
                    seen_friend = False
                    seen_enemy = False
                    file_squares = []
                    while cls._pos[1]+y >= 0 and cls._pos[1]+y <=7 and cls._pos[0]+x >= 0 and cls._pos[0]+ x <= 7:
                        current_piece : Piece = board._rep[cls._pos[1]+y][cls._pos[0]+x]
                        file_squares.append(current_piece.get_position())
                        isEmpty = isinstance(current_piece, Empty) 
                        
                        if not isEmpty and current_piece.get_colour() != colour:
                            seen_enemy = True

                        if seen_enemy == True: #if king is checked,
                            if isinstance(current_piece, Queen):
                                return file_squares
                            elif directionX != 0 and directionY != 0 and isinstance(current_piece, Bishop): 
                                return file_squares
                            elif isinstance(current_piece, Rook):
                                return file_squares
                            else:
                                return []
                            
                        elif not isEmpty and seen_friend == True and current_piece.get_colour() == colour: #two frinedly pieces
                            break

                        elif cls != current_piece and current_piece.get_colour()  == colour:
                            seen_friend = True
                            if isKing == False: #for checking castling squares
                                return []

                        x += directionX
                        y += directionY
                    return []
                horizontal_squares = []
                diagonal_squares = []
                #getting horizontal and diagnoal squares
                horizontal_squares += helper(0,-1,board) #above
                horizontal_squares += helper(0,1,board) #below 
                horizontal_squares += helper(-1,0,board) #left
                horizontal_squares += helper(1,0,board) #right
                diagonal_squares += helper(1,1,board) #bottom right
                diagonal_squares += helper(-1,1,board) #bottom left
                diagonal_squares += helper(1,-1,board) #top right
                diagonal_squares += helper(-1,-1,board) #top left
                
                attacked_squares=[]
                knight_moves = Knight(colour,pos).get_legal_moves(board)
                king_moves = King(colour,pos).get_legal_moves(board)
                for i in knight_moves:
                    if isinstance(board._rep[i[1]][i[0]], Knight):
                        attacked_squares.append(i)
                for i in king_moves:
                    if isinstance(board._rep[i[1]][i[0]], King):
                        attacked_squares.append(i)


                #checking the two pawn moves
                direction = -1 if colour == "white" else 1
                if pos[0] > 0: #check top left for pawn:
                    selected_piece = board._rep[pos[1]+direction][pos[0]-1]
                    if isinstance(selected_piece, Pawn) and colour != selected_piece.get_colour():
                        attacked_squares.append([pos[0]-1,pos[1]+direction])
                if pos[0] < 7: #check top right for pawn:
                    selected_piece = board._rep[pos[1]+direction][pos[0]+1]
                    if isinstance(selected_piece, Pawn) and colour != selected_piece.get_colour():
                        attacked_squares.append(selected_piece.get_position())
                #getitng other attacked squares e.g, kinghts and pawns and king
                return (horizontal_squares,diagonal_squares,attacked_squares)


class King(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "k"

    def set_attacked_squares(cls, board):
        #primarly used to check pinning and checking 
        cls.diagonal_squares = []
        cls.horizontal_squares = []
     
        # def checkLeft(direction)
        # print(cls._pos)
        # cls.horizontal_squares += King.check_attacked_squares(cls._pos,0,-1,board) #above
        # cls.horizontal_squares += King.check_attacked_squares(cls._pos,0,1,board) #below 
        # cls.horizontal_squares += King.check_attacked_squares(cls._pos,-1,0,board) #left
        # cls.horizontal_squares += King.check_attacked_squares(cls._pos,1,0,board) #right
        # cls.diagonal_squares += King.check_attacked_squares(cls._pos,1,1,board) #bottom right
        # cls.diagonal_squares += King.check_attacked_squares(cls._pos,-1,1,board) #bottom left
        # cls.diagonal_squares += King.check_attacked_squares(cls._pos,1,-1,board) #top right
        # cls.diagonal_squares += King.check_attacked_squares(cls._pos,-1,-1,board) #top left
        check = check_attacked_squares(cls._pos,board,cls.get_colour())
        cls.diagonal_squares = check[1]
        cls.horizontal_squares = check[0]

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

        #recording for player
        player_legal_moves = []

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
        if cls.get_position() == [4,7] or cls.get_position() == [4,0]:
        #castiling
            if cls.get_colour() == "white":
                king_side = bool(board._white_castling_availibility[0])
                queen_side = bool(board._white_castling_availibility[1])
            else:
                king_side = bool(board._black_castling_availibility[0])
                queen_side = bool(board._black_castling_availibility[1])

            # back_rank = 7 if cls.get_colour() == "white" else 0
            king_position = cls.get_position()
            
            if king_side:
                i = 0
                king_side_allowed = True #variable that shows if there are no friendly pieces between the king and the rook 
                while king_position[0] + i < 6: #don't need to check the 7th since the rook is there
                    i+= 1
                    current_square =  board._rep[king_position[1]][king_position[0]+i]
                    if not isinstance(current_square, Empty) or check_attacked_squares(current_square.get_position(),board,cls.get_colour(),False) != ([],[],[]): #([],[],[]) is the empty otuptu for check_attacked squares
                        king_side_allowed = False
                        break

                if king_side_allowed == True: #there are no pieces other than the rook so continue
                    #appenidng the king side castle position
                    legal_moves.append([king_position[0]+2,king_position[1]])
            
            if queen_side:
                i = 0
                queen_side_allowed = True #variable that shows if there are no friendly pieces between the king and the rook 
                while king_position[0] + i > 1: #don't need to check the 7th since the rook is there
                    i-= 1
                    current_square =  board._rep[king_position[1]][king_position[0]+i]
                    if not isinstance(current_square, Empty) or check_attacked_squares(current_square.get_position(),board,cls.get_colour(),False) != ([],[],[]): #([],[],[]) is the empty otuptu for check_attacked squares
                        queen_side_allowed = False
                        break
                if queen_side_allowed == True: #there are no pieces other than the rook so continue
                    #appenidng the king side castle position
                    
                    legal_moves.append([king_position[0]-2,king_position[1]])
        return legal_moves
    

    