; Madison Grace Austin
; CSCI 361 Spring 2025
; Programming Assignment #class 31
; I acknowledge that I have worked on this assignment independently, except where explicitly
; noted and referenced. Any collaboration or use of external resources has been properly cited.
; I am fully aware of the consequences of academic dishonesty and agree to abide by the university's
; academic integrity policy. I understand the importance and consequences of plagiarism.

extern _printf
extern _exit

global _main

section .data

    input_text db 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
        db ' Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
        db ' Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'
        db ' Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 0

    shift db 2

section .text
_main:

    push input_text
    push shift
    call _cipher
    add esp, 8
    push input_text
    call _printf

    ; display the encoded string using printf
    ;


    push 0
    call _exit

_cipher:
    ; encode using caesar cipher with fixed of 2
    push ebp
    push ebx
    push esi
    push ecx
    push edx
    push eax

    xor eax, eax
    xor ecx, ecx
    xor edx, edx

    mov ebp, esp
    mov ebx, [ebp + 32]
    xor esi, esi
    loop:
        movq mm0, [ebx + esi]   ; mm2 is uppercase mask and mm4 is lowercase mask
        mov eax, 'A'
        movd mm1, dword eax
        punpcklbw mm1, mm1
        punpcklwd mm1, mm1  ;mask 1
        punpckldq mm1, mm1

        movq mm2, mm1
        pcmpgtb mm2, mm0    ;comparing

        mov eax, 'Z'
        movd mm1, dword eax
        punpcklbw mm1, mm1
        punpcklwd mm1, mm1  ;mask 2
        punpckldq mm1, mm1

        movq mm3, mm0
        pcmpgtb mm3, mm1

        pxor mm2, mm3

        mov eax, 'a'
        movd mm1, dword eax
        punpcklbw mm1, mm1
        punpcklwd mm1, mm1  ;mask 1
        punpckldq mm1, mm1

        movq mm4, mm1
        pcmpgtb mm4, mm0    ;comparing

        mov eax, 'z'
        movd mm1, dword eax
        punpcklbw mm1, mm1
        punpcklwd mm1, mm1  ;mask 2
        punpckldq mm1, mm1

        movq mm3, mm0
        pcmpgtb mm3, mm1

        pxor mm4, mm3

        pxor mm2, mm4

        mov ebx, [ebp + 28]
        mov eax, [ebx]

        movd mm1, dword eax
        punpcklbw mm1, mm1
        punpcklwd mm1, mm1  ;mask 3
        punpckldq mm1, mm1

        movq mm3, mm2
        pand mm3, mm0   ; mm3 holds shift 
        paddb mm3, mm1
        pand mm3, mm2

        mov eax, 'Z'
        add eax, 1

        movd mm1, dword eax
        punpcklbw mm1, mm1
        punpcklwd mm1, mm1  ;mask 4 z + 1
        punpckldq mm1, mm1

        movq mm5, mm3
        pcmpeqb mm5, mm1

        mov eax, 'Z'
        add eax, 2

        movd mm1, dword eax
        punpcklbw mm1, mm1
        punpcklwd mm1, mm1  ;mask 5 z + 2
        punpckldq mm1, mm1

        movq mm6, mm3
        pcmpeqb mm6, mm1

        por mm5, mm6

        ; lowercase 
        mov eax, 'z'
        add eax, 1

        movd mm1, dword eax
        punpcklbw mm1, mm1
        punpcklwd mm1, mm1  ;mask 6 z + 1
        punpckldq mm1, mm1

        movq mm6, mm3
        pcmpeqb mm6, mm1

        por mm5, mm6

        mov eax, 'z'
        add eax, 2

        movd mm1, dword eax
        punpcklbw mm1, mm1
        punpcklwd mm1, mm1  ;mask 7 z + 2
        punpckldq mm1, mm1

        movq mm6, mm3
        pcmpeqb mm6, mm1

        por mm5, mm6
        movq mm6, mm3
        pand mm6, mm5

        mov eax, 26

        movd mm1, dword eax
        punpcklbw mm1, mm1
        punpcklwd mm1, mm1  ;mask 8
        punpckldq mm1, mm1

        psubb mm6, mm1 ; mm6 has the overflow
        pand mm6, mm5

        mov eax, 0xFF

        movd mm1, dword eax
        punpcklbw mm1, mm1
        punpcklwd mm1, mm1  ;mask 9
        punpckldq mm1, mm1

        pandn mm5, mm1
        pand mm3, mm5
        por mm3, mm6

        pandn mm2, mm1
        movq mm4, mm0
        pand mm4, mm2
        por mm3, mm4

        mov ebx, [ebp + 32]
        movq  [ebx + esi], mm3

        mov ecx, 8
        loop2:
            mov dl, [ebx + esi]
            inc esi
            cmp dl, 0
            jz endloop
            loop loop2

        jmp loop
        endloop:

        pop eax
        pop edx
        pop ecx
        pop esi
        pop ebx
        pop ebp

        ret


;Use MMX instructions only for text transformation
;Do not use standard scalar loops for shifting characters
;You may use a loop only for iterating over memory blocks (8 bytes at a time)
;Must use:
;   printf for output
;   exit for program termination
;Do not use int 21h