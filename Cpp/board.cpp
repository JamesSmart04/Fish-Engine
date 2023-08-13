#include <iostream>
#include <unordered_map>
#include <bitset>
#include <limits>
#include "./misc/misc.h"
typedef unsigned long long U64;
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
    

std::unordered_map<char, U64> exportFEN(std::string FEN);
std::string exportFEN(std::unordered_map<char,U64> board){
    std::unordered_map<std::string,std::string> stringBoard = std::unordered_map<std::string,std::string>();
    std::string outputFEN = "";
    
    // making a "complete" bitboard
    std::string completeBitBoard = std::bitset<std::numeric_limits<U64>::digits>(board['e'] | board['f']).to_string();

    for (auto curPiece : board){
        if (!(curPiece.first == 'f' || curPiece.first == 'e')){
            stringBoard[std::string(1, curPiece.first)] = std::bitset<std::numeric_limits<U64>::digits>(curPiece.second).to_string();
        }
    }

    
    int counter = 1;
    for (int i = 0; i < 64; i++){
        if (completeBitBoard[i] == '0'){
            // std::cout << i << "\n";

            while(completeBitBoard[i] == '0')
            {
                std::cout << i << "\n";
                counter += 1;
                i+=1;
                if (i%8 == 0){
                    break;
                }
            }
            std::cout << "Finished" << "\n";
            outputFEN.append(std::to_string(counter));
            counter =1;
        }
        else{
            for (auto curPiece : stringBoard){
                if (curPiece.second[i] == '1'){
                    outputFEN.append(curPiece.first);
                    break;
                }
        }
    }
    if ((i+1) % 8 == 0 && i != 0){
        outputFEN.append("/");
    }
    // loops through all squares in the chess board
    // for(int i = 0; i < 64; i++){
    //     // reached the end of a row so a / is added to the fen

    //     if (i % 8 == 0){
    //         outputFEN.append("/");
    //     }
    //     if (completeBitBoard[i] != '1'){
    //         // square is empty
    //         counter++;
    //         i++;
    //         while (completeBitBoard[i] != '1'){
    //             counter++;
    //             i++;
    //             std::cout << i << "\n";
    //             if (i%8 ==  0){
    //                 break;
    //             }
    //         }
    //         std::cout << counter << "\n";
    //         outputFEN.append(std::to_string(counter));
    //         counter = 0;
    //     }
                


        // check each bitboard to see if there is a piece is in that location
        // for (auto curPiece : stringBoard){
        //     if (curPiece.second[i] == '1'){
        //         outputFEN.append(curPiece.first);
        //         break;
        //     }
        // }


        
    }
    return outputFEN.substr(0);
}

void outputBoard(std::unordered_map<char,U64> board);

void outputBoard(std::unordered_map<char,U64> board){
    for(auto i : board)
    {
        std::string out = std::bitset<std::numeric_limits<U64>::digits>(i.second).to_string();
        std::cout << i.first << "   " << out << "\n";
    }
}


int main(){
    std::unordered_map<char,U64> board = readFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");
    outputBoard(board);
    std::cout << exportFEN(board) << "\n";
    return 0;
}


