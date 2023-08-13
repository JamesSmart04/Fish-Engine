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
    std::vector<std::string> rank_list = split(pieces,'/');
    count = 0;
    for(std::string cur_rank : rank_list){
        std::cout << cur_rank << "\n";
        for(int i = cur_rank.length()-1; i >= 0; i--){
            // a number
            if ((int)cur_rank[i] < 65){
            count += (int)cur_rank[i]-48;   
            }
            // a piece
            else{
                int shift = count;
                pieceDictionary[cur_rank[i]] |= (1ULL<<shift);
                count++;
            }
        }
    }   
    std::cout << count << "\n";
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
    pieceDictionary['w'] = white;
    pieceDictionary['b'] = black;  
    return pieceDictionary;   
}



int main(){
    std::unordered_map<char,U64> myDict = readFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR");
    U64 binary = 0ULL;
    binary |= (1ULL<<32);
    
    std::string out = std::bitset<std::numeric_limits<U64>::digits>(myDict['k']).to_string();
    // std::cout << binary << "\n";
    for(auto i : myDict)
    {
        std::string out = std::bitset<std::numeric_limits<U64>::digits>(i.second).to_string();
        std::cout << i.first << "   " << out << "\n";
    }    
    
    return 0;
}


