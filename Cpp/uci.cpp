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

int main(){
    std::unordered_map<char,U64> board = readFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");
    // outputBitBoards(board);
    outputBoard(board);                     
    std::cout << exportFEN(board) << "\n";  
    // generateKnightAttackTable();
    // printBitboard(std::bitset<std::numeric_limits<U64>::digits>(knight_attacks[63]).to_string());
    
    
    //std::cout << std::bitset<std::numeric_limits<U64>::digits>(w_pawn_any_attacks(board['P'])).to_string() << "\n";
    return 0;
}