import Modules
from functools import partial
import minimax
import evaluation


class Uci:
    def __init__(self) -> None:
        self.Board = Modules.board.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w Kkq - 0 1")
        self.continued_game = False
        self.Depth = 3
        self.uci_communications()
    
    def uci_communications(cls):
        output = partial(print, flush=True)
        
        output("id name fish-engine")
        output("id author Cinna & Mosh")
        
        # sending options that can be adjusted
        # format: option name {thing} type {thing} default {defVal} min {val} max {val}
        # TODO: add parameters
        output("option name Hash type spin default 1 min 1 max 128")
        output("option name Depth type spin default 3 min 1 max 3")
        
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
                    print("legal moves: ",cls.Board.get_legal_moves())
                    print("king attacked: ",cls.Board._king_attacked_squares)
                    print("nodes checked: ", len(cls.Board.get_legal_moves()))
                
                case "setoption":
                    option = command[1:]
                    options_to_be_changed.append(option)
                
                case "isready":
                    # initialise engine with changed settings
                    for i in options_to_be_changed:
                        if i[0] == "Depth":
                            cls.Depth = i[1]
                    output("readyok")
                
                case "testing":
                    cls.testing_generation()
                
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
                    maxPlayer = True if cls.Board.get_turn() == "white" else False
                    evalClass = evaluation.eval()
                    best_move = minimax.minimax(evalClass, cls.Board, cls.Depth, maxPlayer)
                    output("bestmove", best_move[1])
                    output("info string", str(cls.Board.get_turn()))
                    cls.Board.update_position(best_move[1])
                
                case "getEval":
                    evalClass = evaluation.eval()
                    print(evalClass.evalPosition(cls.Board))
                
                case "quit":
                    break
                
                case "debug":
                    pass
                
                case "stop":
                    pass
        
    def testing_generation(cls):
        # 1. take the final uci message sent before the error (position startpos moves e2e4 ....)
        # 2. make the moves on the board and print out all legal moves generated and how many there are
        # 3. compare the numbers given to what stockfish finds with the same positions
        # 4. ???? profit ????
        uci_message = input("Enter moves made (e2e4, d7d5 ...)")
        uci_message = uci_message.split(" ")
        cls.Board.set_board()
        
        
        # initial move for white (20 nodes)
        print(cls.Board.get_legal_moves())
        print(len(cls.Board.get_legal_moves()))
        
        for move in uci_message:
            cls.Board.update_position(move)
            print(cls.Board.get_legal_moves())
            print(len(cls.Board.get_legal_moves()))
            
        cls.Board.change_turn()
        
        print(cls.Board.get_legal_moves())
        print(len(cls.Board.get_legal_moves()))