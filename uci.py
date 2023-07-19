import Modules
from functools import partial
from random import randint


class Uci:
    def __init__(self) -> None:
        self.Board = Modules.board.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Kkq - 0 1")
        self.continued_game = False
        self.uci_communications()
    
    def uci_communications(cls):
        output = partial(print, flush=True)
        
        output("id name fish-engine")
        output("id author Cinna & Mosh")
        
        # sending options that can be adjusted
        # format: option name {thing} type {thing} default {defVal} min {val} max {val}
        # TODO: add parameters
        output("option name Hash type spin default 1 min 1 max 128")
        
        # engine has sent all parameters and is ready to do stuff
        output("uciok")
        cls.handling_commands()
        
    
    
    def handling_commands(cls):
        output = partial(print, flush=True)
        
        while True:
            command = input("").split(" ")
            command_word = command[0]
            
            options_to_be_changed = []
            match command_word:
                
                case "d":
                    print(cls.Board)
                
                case "getlegal":
                    print(cls.Board.get_legal_moves())
                    print(cls.Board._king_attacked_squares)
                
                case "setoption":
                    options_to_be_changed.append(command[1:])
                
                case "isready":
                    # initialise engine with changed settings
                    for i in options_to_be_changed:
                        # TODO: change the options
                        pass
                    output("readyok")
                
                case "ucinewgame":
                    cls.continued_game = False
                    cls.Board.set_board()
                    
                case "position":
                    if command[1] == "startpos" and not cls.continued_game:
                        cls.Board.set_board()
                        cls.continued_game = True
                    
                    elif command[1] == "fen" and not cls.continued_game:
                        if "moves" not in command:
                            fen = " ".join(command[2:])
                        
                        else:
                            fen = " ".join(command[2:command.index("moves")])
                            
                        cls.Board.set_board(fen)
                        cls.continued_game = True

                    if "moves" in command:
                        Lastmove = command[-1]
                        cls.Board.update_position(Lastmove)
                
                case "go":
                    legal_moves = cls.Board.get_legal_moves()
                    random_move = legal_moves[randint(0, len(legal_moves)-1)]
                    cls.Board.update_position(random_move)
                    output("bestmove", random_move)
                
                case "quit":
                    pass
                
                case "debug":
                    pass
                
                case "stop":
                    pass
                    