#include <iostream>
#include <unordered_map>
#include <bitset>
#include <limits>
#include "./misc/misc.h"
typedef unsigned long long U64;

std::unordered_map<std::string,std::string> convertStringBoard(std::unordered_map<char, U64> board);
std::unordered_map<std::string,std::string> convertToStringBoard(std::unordered_map<char, U64> board){
    //making a string board to use indexes
    std::unordered_map<std::string,std::string> stringBoard = std::unordered_map<std::string,std::string>();
    for (auto curPiece : board){
        if (!(curPiece.first == 'f' || curPiece.first == 'e')){
            stringBoard[std::string(1, curPiece.first)] = std::bitset<std::numeric_limits<U64>::digits>(curPiece.second).to_string();
        }
    }
    return stringBoard;
}


std::unordered_map<char, U64> readFEN(std::string FEN);
std::unordered_map<char, U64> readFEN(std::string FEN){
    std::unordered_map<char, U64> pieceDictionary = std::unordered_map<char, U64>();

    char keys[12] = {'p','P','n','N','b','B','r','R','q','Q','k','K'};

    // Initializing blank bitboards
    for (int i = 0; i < 12; i++){
        
        pieceDictionary[keys[i]] = 0ULL;
    }

    int count = 0 ;
    std::vector<std::string> FENlist = split(FEN,' ');
    std::string pieces = FENlist[0];
    count = 0;
    for(int i = pieces.length()-1; i >= 0; i--){

            if ((int)pieces[i] == 47){
                continue;
            }
            // a number
            else if ((int)pieces[i] < 65){
            count += (int)pieces[i]-48;   
            }
            // a piece
            else{
                int shift = count;
                pieceDictionary[pieces[i]] |= (1ULL<<shift);
                count++;
            }
        }
        U64 white = 0ULL;
        U64 black = 0ULL;

        for(auto i : pieceDictionary){
            if (int(i.first) < 91){
                white |= i.second;
            }
            else{
                black |= i.second;
            }
        }
        pieceDictionary['f'] = white;
        pieceDictionary['e'] = black;  
        return pieceDictionary;  
    }


std::string exportFEN(std::unordered_map<char,U64> board){
    std::unordered_map<std::string,std::string> stringBoard = convertToStringBoard(board);
    std::string outputFEN = "";
    
    // making a "complete" bitboard
    std::string completeBitBoard = std::bitset<std::numeric_limits<U64>::digits>(board['e'] | board['f']).to_string();

    for (auto curPiece : board){
        if (!(curPiece.first == 'f' || curPiece.first == 'e')){
            stringBoard[std::string(1, curPiece.first)] = std::bitset<std::numeric_limits<U64>::digits>(curPiece.second).to_string();
        }
    }

    
    int counter =1;
    for (int i = 0; i < 64; i++){
        if (completeBitBoard[i] == '1'){
            for (auto cur_piece : stringBoard){
                if (cur_piece.second[i] == '1'){
                    outputFEN.append(cur_piece.first);
                    break;
                }
            }
        }
        else{
            while(completeBitBoard[i+1] == '0' && (i+1) % 8 != 0){
                counter++; 
                if ((i+2)%8== 0){
                    i+=1;
                    break;
                }
                i++;
            }
            outputFEN.append(std::to_string(counter));
            counter = 1;
        }

        if ((i+1) % 8 == 0 && (i+1) != 64){
            outputFEN.append("/");
        }
    } 
    return outputFEN.substr(0);  
}


void outputBitBoards(std::unordered_map<char,U64> board);
void outputBitBoards(std::unordered_map<char,U64> board){
    for(auto i : board){
        std::string out = std::bitset<std::numeric_limits<U64>::digits>(i.second).to_string();
        std::cout << i.first << "   " << out << "\n";
    }
}


void outputBoard(std::unordered_map<char,U64> board){
    std::unordered_map<std::string,std::string> stringBoard = convertToStringBoard(board);

    for(int i = 0; i <= 63; i++){
        bool pieceFound = false;
        // loop through the 64 squares of the board
        
        if((i)%8 == 0 && i != 0){
            // new line needed
            std::cout << " |\n";
        }

        for(auto j : stringBoard){
            // checking the bitboards to see what piece is in that position
            if(j.second[i] == '1'){
                std::cout << " | " << j.first;
                pieceFound = true;
                break;
            }
        }
        if(!pieceFound){
            std::cout << " |  ";
        }
    }
    std::cout << " |\n";
}


int main(){
    std::unordered_map<char,U64> board = readFEN("rnbqkbnr/pp2pppp/8/2p5/1PPp4/4PN2/P2P1PPP/RNBQKB1R w KQkq - 0 1");
    outputBitBoards(board);
    outputBoard(board);
    
    
    std::cout << exportFEN(board) << "\n";  
    return 0;
}