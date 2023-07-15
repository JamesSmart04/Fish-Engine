from .piece import Piece
from .empty import Empty


class Rook(Piece):
    def __init__(self, colour="white", pos=[0, 0]) -> None:
        super().__init__(colour, pos)
        self._piece = "r"
        self._value = 500
    
    def get_pseudo_legal_moves(cls, board):
        #veritcal
        pseudo_legal_moves = []

        #above
        i = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[1]+i > 0:
            i -= 1
            currentSquare = board._rep[cls._pos[1]+i][cls._pos[0]]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    pseudo_legal_moves.append(currentSquare._pos)
                break
            pseudo_legal_moves.append(currentSquare._pos)


        #below
        i = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[1]+i < 7:
            i += 1
            currentSquare = board._rep[cls._pos[1]+i][cls._pos[0]]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    pseudo_legal_moves.append(currentSquare._pos)
                break
            pseudo_legal_moves.append(currentSquare._pos)

    
        #horizontal left
        i = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[0]+i > 0:
            i -= 1
            currentSquare = board._rep[cls._pos[1]][cls._pos[0]+i]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    pseudo_legal_moves.append(currentSquare._pos)
                break
            pseudo_legal_moves.append(currentSquare._pos)

        #right
        i = 0
        currentSquare = Empty()
        while isinstance(currentSquare, Empty) and cls._pos[0]+i < 7:
            i += 1
            currentSquare = board._rep[cls._pos[1]][cls._pos[0]+i]
            if  not isinstance(currentSquare, Empty):
                if currentSquare.get_colour() != cls._colour:
                    pseudo_legal_moves.append(currentSquare._pos)
                break
            pseudo_legal_moves.append(currentSquare._pos)
            
            
        # if not isinstance(currentSquare, Empty):
        #     legal_moves.append(currentSquare._pos)
            
        return pseudo_legal_moves
    
    def get_legal_moves(cls,board):
        pseudo_legal_moves = cls.get_pseudo_legal_moves(board)
        king_checked = board._white_checked if cls._colour == "white" else board._black_checked
        attacked_squares = board.get_king_attacked_squares()
        #fixing attacked squares ([] = pseudolegalmoves)
        legal_moves = []

        #case 1: King is checked
        if king_checked == True:
            for i in range(len(attacked_squares)):

                if attacked_squares[i] == []:
                    attacked_squares[i] = pseudo_legal_moves
            if king_checked == True:
                for i in pseudo_legal_moves:
                    if i in attacked_squares[0] and i in attacked_squares[1] and i in attacked_squares[2]\
                    and i in attacked_squares[3] and i in attacked_squares[4]:
                        legal_moves.append(i)

        #case 2: piece is pinned to king
        elif attacked_squares != [[],[],[],[],[]]: #king is pinned
            for i in attacked_squares:
                if cls._pos in i:
                    for j in pseudo_legal_moves:
                        if j in i:
                            legal_moves.append(j)
                    return legal_moves      
                
        else:
            legal_moves =pseudo_legal_moves
        
        return legal_moves

        
            
            



        
        

            
