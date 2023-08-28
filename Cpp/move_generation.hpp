#include <bitset>
#include <iostream>
#include <string>
#include <vector>
typedef unsigned long long U64;

U64 getFile(int cur_bit) {
    U64 file =  0ULL;
    int file_pointer = cur_bit;
    file |= (1ULL<<cur_bit);
    while((file_pointer+8)<= 63){
        file_pointer += 8;
        file |= (1ULL<<file_pointer);
    }
    file_pointer = cur_bit;
    while((file_pointer-8) > 0){
        file_pointer -= 8;
        file |= (1ULL<<file_pointer);
    }
    
    return file;
}

U64 getRank(int cur_bit) {
    U64 piece = (1ULL<<cur_bit);
    U64 rank = 0xFFULL;
    int multiplyer = 0;
    while(multiplyer < 8){
        U64 cur_rank = (rank << (multiplyer*8));
        if ((piece & cur_rank) != 0ULL){
            return cur_rank;
        }
        multiplyer++;
    }
    return 0;
}
std::string convertToNotation(int cur_bit){
    char file_list[8] = {'a','b','c','d','e','f','g','h'};
    int cur_rank = 8-(cur_bit/8);
    char cur_file = file_list[cur_bit%8];
    std::string output = "";
    output += cur_file;
    output += std::to_string(cur_rank);
    return output;
}


std::vector<std::string> getMoves(int current_pos, U64 moving_pos){
   std::vector<std::string> output = std::vector<std::string>();
   std::string orgin = convertToNotation(current_pos);
   //finding moves from bitboard
   for(int i = 0; i < 64; i++){
        if (((1ULL << i) & moving_pos)!= 0ULL){
            output.push_back(orgin+convertToNotation(63-i));
        }
   }
   return output;

}
/***
 * 
 * 
 * Knight !
 * 
*/
U64 knight_right_horiozntal_mask = 4557430888798830399ULL;
U64 knight_left_horizontal_mask = 18229723555195321596ULL;

extern U64 knight_attacks[64] =  {0ULL}; 


// Generating kinght attacks
void generateKnightAttackTable () {
    for (int i = 0; i < sizeof(knight_attacks)/sizeof(knight_attacks[0]); i++){
        U64 current_attack = 0ULL; // current attack bitboard to be modified below
        int knight_attack_values[8] =  {i+6,i+15, i-10,i-17,i+10,i+17,i-6,i-15};
        for (int j = 0; j < sizeof(knight_attack_values)/sizeof(knight_attack_values[0]); j++){   
            if (knight_attack_values[j] < 0 ||  knight_attack_values[j] > 63){
                continue;
            }
            else{
                current_attack |= ((1ULL<<knight_attack_values[j]));
        }
        if ((i%8) > 5){
            current_attack &= knight_left_horizontal_mask;
        }
        if ((i%8) < 2){
            current_attack &= knight_right_horiozntal_mask;
        }
        knight_attacks[63-i] = current_attack;
        }
    }
}



/***
 * 
 * 
 * Pawn !
 * (save me)
*/

extern U64 pawn_forward_attacks[2][64] = {{0ULL},{0ULL}}; // 0 = White; 1 = Black
U64 en_passant_list = 0ULL;  

void generateForwardAttacks() {
    for(int i = 0; i < sizeof(pawn_forward_attacks)/sizeof(pawn_forward_attacks[0]);i++){
        int shift = 8  + 16*(i*-1);
        for (int j = 0; j < sizeof(pawn_forward_attacks[0])/sizeof(pawn_forward_attacks[0][0]); j++){
            U64 current_attack_board = 0ULL;
            if ( shift > 0 && j >= 8 && j <= 15){ //double pushing
                int double_push = j+shift*2;
                current_attack_board |= (1ULL <<double_push);
            } 
            else if(shift < 0 && j >= 48 && j <= 55)  {
                int double_push = j+shift*2;
                current_attack_board |= (1ULL<<double_push);
            }
            int single_push = j+shift;
            if (single_push < 64){
                current_attack_board |= (1ULL<<single_push);
            }
            pawn_forward_attacks[i][63-j] = current_attack_board;
        }
    }
}

U64 w_pawn_east_attacks(U64 wPawns){
    // removes the H file to get pawns that can attack east
    U64 east_possible_pawns = ((~getFile(0)) & wPawns);
    return (east_possible_pawns << 7);
}

U64 w_pawn_west_attacks(U64 wPawns){
    // removes the A file to get pawns that can attack west
    U64 west_possible_pawns = ((~getFile(7)) & wPawns);
    return (west_possible_pawns << 9);
}

U64 w_pawn_any_attacks(U64 wpawns) {
   return w_pawn_west_attacks(wpawns) | w_pawn_east_attacks(wpawns);
}

U64 w_pawn_dbl_attacks(U64 wpawns) {
   return w_pawn_west_attacks(wpawns) & w_pawn_east_attacks(wpawns);
}

U64 w_pawn_single_attacks(U64 wpawns) {
   return w_pawn_west_attacks(wpawns) ^ w_pawn_east_attacks(wpawns);
}



U64 b_pawn_east_attacks(U64 bPawns){
    // removes the H file to get pawns that can attack east
    U64 east_possible_pawns = ((~getFile(0)) & bPawns);
    return (east_possible_pawns >> 9);
}

U64 b_pawn_west_attacks(U64 bPawns){
    // removes the A file to get pawns that can attack west
    U64 west_possible_pawns = ((~getFile(7)) & bPawns);
    return (west_possible_pawns >> 7);
}

U64 b_pawn_any_attacks(U64 bpawns) {
   return b_pawn_west_attacks(bpawns) | b_pawn_east_attacks(bpawns);
}

U64 b_pawn_dbl_attacks(U64 bpawns) {
   return b_pawn_west_attacks(bpawns) & b_pawn_east_attacks(bpawns);
}

U64 b_pawn_single_attacks(U64 bpawns) {
   return b_pawn_west_attacks(bpawns) ^ b_pawn_east_attacks(bpawns);
}


