; Madison Grace Austin
; CSCI 361 Spring 2025
; Programming Assignment #class 33
; I acknowledge that I have worked on this assignment independently, except where explicitly
; noted and referenced. Any collaboration or use of external resources has been properly cited.
; I am fully aware of the consequences of academic dishonesty and agree to abide by the university's
; academic integrity policy. I understand the importance and consequences of plagiarism.

extern _printf
extern _exit

global _main
section .data

vector_a dd 1.0,2.0,3.0,4.0, 5.0,6.0,7.0,8.0, 9.0,10.0,11.0,12.0
vector_b dd 1.0,1.0,1.0,1.0, 2.0,2.0,2.0,2.0, 3.0,3.0,3.0,3.0
result dq 0.0
fmt db "%lf",10,13,0

section .text
_main:
    push vector_a
    push vector_b
    push result

    call dot

    add esp, 12
    push dword [result + 4]
    push dword [result]
    push fmt
    call _printf
    add esp, 8

    push 0
    call _exit
    dot: 
        push ebp
        push ebx
        push ecx
        push esi

        mov ecx, 3
        xor esi, esi
        mov ebp, esp

        .loop:
            mov ebx, [ebp + 28]
            movups xmm0, [ebx + esi]

            mov ebx, [ebp + 24]
            movups xmm1, [ebx + esi]

            mulps xmm0 ,xmm1
            movaps xmm1, xmm0
            shufps xmm1, xmm1, 0b00011011
            addps xmm0, xmm1
            movaps xmm1, xmm0
            shufps xmm1, xmm1, 0b01001110
            addps xmm0, xmm1

            addps xmm3, xmm0
            add esi, 16

        loop .loop

        mov ebx, [ebp + 20]
        xorps xmm1, xmm1
        movss xmm1, xmm3
        cvtps2pd xmm1, xmm1
        movsd [ebx], xmm1

        pop esi
        pop ecx
        pop ebx
        pop ebp
    ret