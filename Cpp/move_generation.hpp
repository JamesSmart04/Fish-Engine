#include <bitset>
#include <iostream>
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

            knight_attacks[i] = current_attack;
        }
    }
}
