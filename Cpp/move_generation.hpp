#include <bitset>
#include <iostream>
typedef unsigned long long U64;

U64 getFile(int cur_bit) {
    U64 file =  0ULL;
    int file_pointer = cur_bit;
    file |= (1ULL<<cur_bit);
    while((file_pointer+8)< 63){
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

