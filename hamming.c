#include <stdio.h>
#include <stdint.h>

uint32_t shr(uint32_t v){
    int c = 0;

    //if(v != ){
    //    return c;
    //}
    c += v & 0x1;
    while(v != 0){
        v = v >> 1;
        c += v & 0x1;
    }
    return c;
}

//https://stackoverflow.com/questions/14555607/number-of-bits-set-in-a-number
uint32_t hakmem(uint32_t v){
    v = v - ((v >> 1) & 0x55555555);                    // reuse input as temporary
    v = (v & 0x33333333) + ((v >> 2) & 0x33333333);     // temp
    return ((v + (v >> 4) & 0xF0F0F0F) * 0x1010101) >> 24; // count
}
