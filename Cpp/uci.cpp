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
    U64 en_passant_list = 0ULL;
    
    // outputBitBoards(board);
    outputBoard(board);                     
    std::cout << exportFEN(board) << "\n";  
    generateForwardAttacks();
    generateKnightAttackTable();
    // printBitboard(std::bitset<std::numeric_limits<U64>::digits>(pawn_forward_attacks[1][8]).to_string());

    // std::vector<std::string> knight_moves_uwu = getMoves(8,pawn_forward_attacks[1][8]);
    // for (auto i :  knight_moves_uwu){
    //     std::cout << i << ", ";
    // }
    
    // std::cout << std::bitset<std::numeric_limits<U64>::digits>(w_pawn_any_attacks(board['P'])).to_string() << "\n";
    // std::cout << std::bitset<std::numeric_limits<U64>::digits>(generate_king_attack(board['k'])).to_string();
    
    
    return 0;
}