from Modules.misc import *
class Piece:
    def __init__(self, colour="white", pos=[0,0]) -> None:
        self._pos = pos
        self._colour = colour
        self._piece = ""
    
    def get_colour(cls) -> str:
        return cls._colour
    
    def get_position(cls) -> list:
        return cls._pos
    def set_colour(cls, colour) -> None:
        cls._colour = colour
    
    def set_pos(cls, pos:list[int]) -> None:
        cls._pos = pos

    def __str__(cls) -> str:
        if cls._colour == "black":
            return cls._piece.lower()
        else:
            return cls._piece.upper()

    
class Pawn(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "p"
        self.double_move = False

    def get_legal_moves(cls, board):

        legal_moves = []

        direction = 1
        if cls._colour == "white" : direction = -1

        # straight
        if isinstance(board._rep[cls._pos[1]+direction][cls._pos[0]], Empty):
            legal_moves.append([cls._pos[0],cls._pos[1]+direction])
            start_row = 6 if direction == -1 else 2 
            if cls._pos[1] == start_row  and isinstance(board._rep[cls._pos[1]+direction*2][cls._pos[0]], Empty):
                legal_moves.append([cls._pos[0],cls._pos[1]+direction*2])
                
        
        # not straight
        left_square = None
        right_square = None
        if cls._pos[0] > 0:
            left_square = board._rep[cls._pos[1]+direction][cls._pos[0]-1] 
            if not isinstance(left_square,Empty):
                legal_moves.append(left_square._pos)
        if cls._pos[0] < 7:
            right_square = board._rep[cls._pos[1]+direction][cls._pos[0]+1]
            if not isinstance(right_square,Empty):
                legal_moves.append(right_square._pos)
        
        return legal_moves
        

class Rook(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "r"
    
    def get_legal_moves(cls, board):
        #veritcal
        legal_moves = []

        #above
        i = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[1]+i > 0:
            i -= 1
            currentSquare = board._rep[cls._pos[1]+i][cls._pos[0]]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)


        #below
        i = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[1]+i < 7:
            i += 1
            currentSquare = board._rep[cls._pos[1]+i][cls._pos[0]]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)

    
        #horizontal left
        i = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[0]+i > 0:
            i -= 1
            currentSquare = board._rep[cls._pos[1]][cls._pos[0]+i]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)

        #right
        i = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[0]+i < 7:
            i += 1
            print(cls._pos[0]+i)
            currentSquare = board._rep[cls._pos[1]][cls._pos[0]+i]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)
            
            
        # if not isinstance(currentSquare, Empty):
        #     legal_moves.append(currentSquare._pos)
            
        return legal_moves



class Knight(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "n"
    
    def get_legal_moves(cls, board):
        legal_moves = []
        
        def horizontal_checker(direction):
            # -1 = right, 1 = left (ik its confusing lol shut up mosh go away)
            # checking horizontal to check if the knight can move far in that direction
            horizontal_limit = 2 if direction == 1 else -5
            if (cls._pos[0]*direction) >= horizontal_limit:
                # when both sides are multiplied by -1 the inequality is flipped
                if cls._pos[1] >= 1:
                    far_upper = board._rep[cls._pos[1]-1][cls._pos[0]-2*direction]
                    if isinstance(far_upper, Empty) or far_upper.get_colour() != cls._colour:
                        # far left upper square is either empty or an enemy piece
                        legal_moves.append(far_upper._pos)
                
                if cls._pos[1] <= 6:
                    far_lower = board._rep[cls._pos[1]+1*direction][cls._pos[0]-2*direction]
                    if isinstance(far_lower, Empty) or far_lower.get_colour() != cls._colour:
                        # far left lower square is either empty or an enemy piece
                        legal_moves.append(far_lower._pos)
        
        
        def vertical_checker(direction):
            vertical_limit = 2 if direction == 1 else -5
            if (cls._pos[1]*direction) >= vertical_limit:
                # when both sides are multiplied by -1 the inequality is flipped
                if cls._pos[0] >= 1:
                    left_square = board._rep[cls._pos[1]-2*direction][cls._pos[0]-1]
                    if isinstance(left_square, Empty) or left_square.get_colour() != cls._colour:
                        legal_moves.append(left_square._pos)
                
                if cls._pos[0] <= 6:
                    right_square = board._rep[cls._pos[1]-2*direction][cls._pos[0]+1]
                    if isinstance(right_square, Empty) or left_square.get_colour() != cls._colour:
                        legal_moves.append(right_square._pos)
        
        horizontal_checker(1)
        horizontal_checker(-1)
        vertical_checker(1)
        vertical_checker(-1)
        
        return legal_moves


class Bishop(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "b"
    
    def get_legal_moves(cls, board):
        legal_moves = []
        #top left
        i = 0
        j = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[1]+i > 0 and cls._pos[0]+j > 0:
            i -= 1
            j -= 1
            currentSquare = board._rep[cls._pos[1]+i][cls._pos[0]+j]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)


        #top right
        i = 0
        j = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[1]+i > 0 and cls._pos[0] + j < 7:
            i += -1
            j += 1
            currentSquare = board._rep[cls._pos[1]+i][cls._pos[0]+j]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)

    
        #bottom left
        i = 0
        j = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[0]+i > 0 and cls._pos[1]+j < 7 :
            i -= 1
            j += 1
            currentSquare = board._rep[cls._pos[1]][cls._pos[0]+i]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)

        #bottom right
        i = 0
        j = 0 
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[0]+i < 7 and cls._pos[1] < 7:
            i += 1
            j += 1
            print(cls._pos[0]+i)
            currentSquare = board._rep[cls._pos[1]][cls._pos[0]+i]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    legal_moves.append(currentSquare._pos)
                break
            legal_moves.append(currentSquare._pos)
            
            
        # if not isinstance(currentSquare, Empty):
        #     legal_moves.append(currentSquare._pos)
            
        return legal_moves


class Queen(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "q"
    
    def get_legal_moves(cls, board):
        straight_moves = Rook(cls._colour, cls._pos).get_legal_moves(board)
        diagonal_moves = Bishop(cls._colour, cls._pos).get_legal_moves(board)

        for move in straight_moves:
            diagonal_moves.append(move)
        return diagonal_moves


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
        def checkVertical(direction):
            i = direction
            current_piece = None
            seen_friend = False
            seen_enemy = False
            file_squares = []
            while cls._pos[1]+i >= 0 and cls._pos[1]+i <=7:
                current_piece : Piece = board._rep[cls._pos[1]+i][cls._pos[0]]
                file_squares.append(current_piece.get_position())
                isEmpty = isinstance(current_piece, Empty) 
                
                if not isEmpty and current_piece.get_colour() != cls._colour:
                    seen_enemy = True

                if seen_enemy == True: #if king is checked
                    if isinstance(current_piece, Rook) or isinstance(current_piece, Queen):
                        
                        cls.horizontal_squares.append(file_squares)
                        break
                elif not isEmpty and seen_friend == True and current_piece.get_colour() == cls._colour: #two frinedly pieces
                    break

                elif cls != current_piece and current_piece.get_colour()  == cls._colour:
                    seen_friend = True

                i += direction 

        def checkHorizontal(direction):
            i = direction
            current_piece = None
            seen_friend = False
            seen_enemy = False
            file_squares = []
            while cls._pos[0]+i >= 0 and cls._pos[0]+i <=7:
                current_piece : Piece = board._rep[cls._pos[1]][cls._pos[0]+i]
                file_squares.append(current_piece.get_position())
                isEmpty = isinstance(current_piece, Empty) 
                
                if not isEmpty and current_piece.get_colour() != cls._colour:
                    seen_enemy = True

                if seen_enemy == True: #if king is checked
                    if isinstance(current_piece, Rook) or isinstance(current_piece, Queen):
                        
                        cls.horizontal_squares += file_squares
                        break
                elif not isEmpty and seen_friend == True and current_piece.get_colour() == cls._colour: #two frinedly pieces
                    break

                elif cls != current_piece and current_piece.get_colour()  == cls._colour:
                    seen_friend = True

                i += direction 
        # def checkLeft(direction)
            
        checkVertical(-1) #above
        checkVertical(1) #below
        checkHorizontal(-1) #left
        checkHorizontal(1) #right
        

        
            

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
        
            

class Empty(Piece):
    def __init__(self,colour = "empty", pos=[0,0]) -> None:
        super().__init__(colour,pos)
        self._piece = "e"
    def __str__(cls) -> str:
        return " "