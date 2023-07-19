from functools import partial
import Modules
#https://stackoverflow.com/questions/17003561/using-the-universal-chess-interface#17006540
#https://nocheto.sallyx.org/doc/nocheng/

def uciCommunication():
    printa = partial(print, flush=True)
    
    # sending engine identity and author
    printa("id name fish-engine")
    printa("id author Mosh & Cinna")
    
    # sending options that can be adjusted
    # format: option name {thing} type {thing} default {defVal} min {val} max {val}
    # TODO: add parameters
    
    # engine has sent all parameters and is ready now
    printa("uciok")
    
    while True:
        GUI_command = input("")
        possible_command = GUI_command.split(" ")[0]
        
        match possible_command:
            case "setoption":
                # this means a parameter is being edited:
                pass
            
            case "isready":
                # this means the GUI is ready and is now waiting for the engine to initialise
                # TODO: initialise here
                printa("readyok")
            
            case "ucinewgame":
                # a new game is being started
                printa("bestmove e2e4")                 


if input("") == "uci":
    uciCommunication()
    
    
    
    
    
    
    
     
    