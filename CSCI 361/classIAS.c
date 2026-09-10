


#include <stdio.h>
// ----------------- MAIN PROGRAM -----------------
int main()
{
    // register
    int AC = 0;
    // data words
    int N = 3;
    int _const = 1;
    int i = 0;
    int Y = 0; //result
    //beginning
    AC = N;
    i = AC;
    //loop
    _loop:
        AC = i;
        AC = AC + Y;
        Y = AC;
        AC = i;
        AC = AC - _const;
        i = AC;
        AC = AC - _const;
        if(AC >= 0 )
    goto _loop;
    printf("Y = %d", Y);
    // 000 01 006 21 008 # _01 load m(6) N ;_21 store ac to m(8) # copy of input N # before loop
    // lopp
    // 001 01 008 05 009 # N ; _01 load counter add to ac Y m(9)
    // 002 21 009 01 008 # N ; _21 store temp_result and load counter
    // 003 06 007 21 008 # N ; _06 sub 1 from 007 and store dec counter
    // 004 06 007 0F 001 # N _sub 1 from ac and cj to 001 (ac>=0)
    // 005 0D 005 00 000 # N halt jump to 005L
    // 006 00 000 00 004 # N
    // 007 00 000 00 001 # 1 - const
    // 008 00 000 00 000 # i - counter
    // 009 00 000 00 000 # Y - result
    //if(ac>=0) L or R
    return 0;
}

// no use of constants, only memory adres
// cant go memory adres to memory you have to move it in to ac as a buffer
// study each instruction
// 