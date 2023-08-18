#include "board.hpp"
#include "evaluation.hpp"
#include "minimax.hpp"
#include "move_generation.hpp"


int main(){
    std::unordered_map<char,U64> board = readFEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1");
    outputBitBoards(board);
    outputBoard(board);
    std::cout << exportFEN(board) << "\n";  
    U64 out = getRank(8);
    std::cout << std::bitset<std::numeric_limits<U64>::digits>(out).to_string();  
    return 0;
}