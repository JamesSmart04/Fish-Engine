#include <bits/stdc++.h>
#include <algorithm>
#include "board.hpp"
#include "evaluation.hpp"
#include "minimax.hpp"
#include "move_generation.hpp"

void printBitboard(std::string bitstring){
    for(int i = 0; i < 8; i++){
        std::cout << bitstring.substr(i*8,8) << "\n";
    }
    return;
}


std::vector<std::string> split_by_space(std::string s){
    std::vector<std::string> outputArr; 


    std::stringstream ss(s);
    std::string word;
    while (ss >> word) {
        outputArr.push_back(word);
    }
    return outputArr;
}



void output(std::string var) {std::cout << var << std::endl;}
void uci_communications(){
    output("id name fish-engine");
    output("id author Cinna & Mosh");

    // sending options that can be adjusted
    // format: option name {thing} type {thing} default {defVal} min {val} max {val}
    // TODO: add parameters
    output("option name Hash type spin default 1 min 1 max 128");
    output("option name Depth type spin default 3 min 1 max 3");
    
    // engine has sent all parameters and is ready to do stuff
    output("uciok");
}


void handling_commands(){
    std::unordered_map<char,U64> board = readFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");
    bool continued_game = false;
    
    while(true){
        std::string command = "";
        std::cin >> command;

        std::vector<std::string> split_command = split_by_space(command);

        std::vector<std::string> options_to_be_changed;

        if(split_command[0] == "d"){
            outputBoard(board);
        }

        else if(split_command[0] == "getlegal"){
            output("legal moves:");
            output("king attacked:");
            output("nodes checked:");
        }

        else if(split_command[0] == "setoption"){
            break;
        }

        else if(split_command[0] == "isready"){
            // initialise engine with changed settings
            output("readyok");
        }

        else if(split_command[0] == "testing"){
            break;
        }

        else if(split_command[0] == "ucinewgame"){
            continued_game = false;
            board = readFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");
        }

        else if(split_command[0] == "position"){
            if(split_command[1] == "startpos" && !continued_game){
                board = readFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");
                continued_game = true;
            }

            else if(split_command[1] == "fen" && !continued_game){
                // if moves is in command:
                if(std::find(split_command.begin(), split_command.end(), "moves") != split_command.end()){
                    break;
                }
                else{
                    break;
                }
            }
        }

        else if(split_command[1] == "go"){
            break;
        }

        else if(split_command[1] == "getEval"){
            break;
        }

        else if(split_command[1] == "quit"){
            break;
        }

        else if(split_command[1] == "debug"){
            break;
        }

        else if(split_command[1] == "stop"){
            break;
        }
    }
}

int main(){
    // std::unordered_map<char,U64> board = readFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");
    // U64 en_passant_list = 0ULL;
    
    // outputBitBoards(board);
    // outputBoard(board);                     
    // std::cout << exportFEN(board) << "\n";  
    // printBitboard(std::bitset<std::numeric_limits<U64>::digits>(pawn_forward_attacks[1][8]).to_string());

    // std::vector<std::string> knight_moves_uwu = getMoves(8,pawn_forward_attacks[1][8]);
    // for (auto i :  knight_moves_uwu){
    //     std::cout << i << ", ";
    // }
    
    // std::cout << std::bitset<std::numeric_limits<U64>::digits>(w_pawn_any_attacks(board['P'])).to_string() << "\n";
    // std::cout << std::bitset<std::numeric_limits<U64>::digits>(generate_king_attack(board['k'])).to_string();
    
    generateForwardAttacks();
    generateKnightAttackTable();
    uci_communications();
    handling_commands();
    return 0;
}