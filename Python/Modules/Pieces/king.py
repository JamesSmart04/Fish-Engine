from .piece import Piece
from .queen import Queen
from .bishop import Bishop
from .knight import Knight
from .empty import Empty
from .rook import Rook
from .pawn import Pawn
from Modules.misc import convert_pos_to_string
import copy

'''
for i in return:
    if i == []:
        i = pseudolegal_moves
for i in piecce_pseudolegal moves
    if i in horizontal_squares and i in diagonal_squares, and i in attacked_squares: 
        legal_moves.append(i)
    returun legal_moves



'''

class King(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "k"
        self._value = 20000
    
    def check_attacked_squares(cls,pos,board, colour,isKing = True):
                # counter = 0
                checked_list = []
                def helper(directionX, directionY, board):
                    # counter += 1
                    x = directionX
                    y = directionY
                    target_piece  = board.get_piece(pos)
                    current_piece = None
                    seen_friend = False
                    seen_enemy = False
                    file_squares = []
                    while target_piece._pos[1]+y >= 0 and target_piece._pos[1]+y <=7 and target_piece._pos[0]+x >= 0 and target_piece._pos[0]+ x <= 7:
                        current_piece = board._rep[target_piece._pos[1]+y][target_piece._pos[0]+x]
                        file_squares.append(current_piece.get_position())
                        isEmpty = isinstance(current_piece, Empty) 
                        
                        if not isEmpty and current_piece.get_colour() != colour:
                            seen_enemy = True

                        if seen_enemy == True:
                            # if seen_friend != True and counter%2 == 0 :
                            #     checked_list.append(True)
                            # else:
                            #     checked_list.append(False)
                        
                            if isinstance(current_piece, Queen):
                                return file_squares
                            elif directionX != 0 and directionY != 0 and isinstance(current_piece, Bishop): 
                                return file_squares
                            elif isinstance(current_piece, Rook) and (directionX == 0) ^ (directionY == 0):
                                return file_squares
                            else:
                                return []
                            
                        elif not isEmpty and seen_friend == True and current_piece.get_colour() == colour: #two frinedly pieces
                            break

                        elif target_piece != current_piece and current_piece.get_colour()  == colour and not isinstance(current_piece,King):
                            seen_friend = True
                            if isKing == False: #for checking castling squares
                                return []

                        x += directionX
                        y += directionY
                    return []
                vertical_squares = []
                horizontal_squares = []
                positive_diagonal_squares = []
                negative_diagonal_squares =[]
                #getting horizontal and diagnoal squares
                vertical_squares += helper(0,-1,board) #above
                vertical_squares += helper(0,1,board) #below 
                horizontal_squares += helper(-1,0,board) #left
                horizontal_squares += helper(1,0,board) #right
                negative_diagonal_squares += helper(1,1,board) #bottom right
                positive_diagonal_squares += helper(1,-1,board) #top right
                positive_diagonal_squares += helper(-1,1,board) #bottom left
                negative_diagonal_squares += helper(-1,-1,board) #top left
                
                attacked_squares=[]
                knight_moves = Knight(colour,pos).get_pseudo_legal_moves(board)
                king_moves = King(colour,pos).get_pseudo_legal_moves(board)
                for i in knight_moves:
                    if isinstance(board._rep[i[1]][i[0]], Knight):
                        attacked_squares.append(i)
                for i in king_moves:
                    if isinstance(board._rep[i[1]][i[0]], King):
                        attacked_squares.append(i)


                #checking the two pawn moves
                direction,backrank = (-1,0) if colour == "white" else (1,7)
                # if colour == "white":
                if pos[0] > 0  and pos[1]*-1*direction > backrank*-1*direction: #check top left for pawn:
                    # print([pos[1]+direction,pos[0]-1])
                    selected_piece = board._rep[pos[1]+direction][pos[0]-1]
                    if isinstance(selected_piece, Pawn) and colour != selected_piece.get_colour():
                        attacked_squares.append([pos[0]-1,pos[1]+direction])
                if pos[0] < 7 and pos[1]*-1*direction > backrank*-1*direction: #check top right for pawn:
                    selected_piece = board._rep[pos[1]+direction][pos[0]+1]
                    if isinstance(selected_piece, Pawn) and colour != selected_piece.get_colour():
                        attacked_squares.append(selected_piece.get_position())
            #getitng other attacked squares e.g, kinghts and pawns and king
                return [horizontal_squares,vertical_squares, negative_diagonal_squares,positive_diagonal_squares,attacked_squares]    

    def set_attacked_squares(cls, board):
        #primarly used to check pinning and checking 
        cls.diagonal_squares = []
        cls.horizontal_squares = []
     
        check = cls.check_attacked_squares(cls._pos,board,cls.get_colour())
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

    def get_pseudo_legal_moves(cls,board):
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
        cur_check = board._white_checked if cls._colour == "white" else board._black_checked

        if not cur_check and cls.get_position() == [4,7] or cls.get_position() == [4,0]:
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
                    if not isinstance(current_square, Empty) or cls.check_attacked_squares(current_square.get_position(),board,cls.get_colour(),False) != [[],[],[],[],[]]: #([],[],[]) is the empty otuptu for check_attacked squares
                        king_side_allowed = False
                        break

                if king_side_allowed == True: #there are no pieces other than the rook so continue
                    #appenidng the king side castle position
                    legal_moves.append([king_position[0]+2,king_position[1]])
            
            if queen_side:
                i = 0
                queen_side_allowed = True #variable that shows if there are no friendly pieces between the king and the rook 
                while king_position[0] + i > 2: #don't need to check the 6th or 7th since the furthest the king moves is the 5th     rook is there
                    i-= 1
                    current_square =  board._rep[king_position[1]][king_position[0]+i]
                    if not isinstance(current_square, Empty) or cls.check_attacked_squares(current_square.get_position(),board,cls.get_colour(),False) != [[],[],[],[],[]]: #([],[],[]) is the empty otuptu for check_attacked squares
                        queen_side_allowed = False
                        break
                if queen_side_allowed == True: #there are no pieces other than the rook so continue
                    #appenidng the king side castle position
                    
                    legal_moves.append([king_position[0]-2,king_position[1]])
        return legal_moves
    

    """Filters through pseudolegal moves"""
    def get_legal_moves(cls,board):
        #chekcing if the king is in check
        legal_moves = []
        psuedo_legal_moves =  cls.get_pseudo_legal_moves(board)
        attacked_squares  = cls.check_attacked_squares(cls.get_position(),board,cls._colour) 
        for i in psuedo_legal_moves:
            current_square = board._rep[i[1]][i[0]]
            if current_square.get_colour() != cls._colour and cls.check_attacked_squares(current_square.get_position(), board, cls.get_colour(), False) == [[],[],[],[],[]]: #going through the kings legal moves and seeing if it is attacked
                legal_moves.append(i)
        return legal_moves if legal_moves != [] else None
                
                            
    

    

    