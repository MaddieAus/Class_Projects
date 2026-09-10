; Madison Grace Austin
; CSCI 361 Spring 2025
; Programming Assignment #class 29
; I acknowledge that I have worked on this assignment independently, except where explicitly
; noted and referenced. Any collaboration or use of external resources has been properly cited.
; I am fully aware of the consequences of academic dishonesty and agree to abide by the university's
; academic integrity policy. I understand the importance and consequences of plagiarism.

%define int_21h call _interupt_21h
global _main
extern _interupt_21h
extern _printf
extern _scanf

section .data

x dq 1.0 ;inital guess

s dq 0.0 ;input value

half dq 0.5

fmt db "%lf",0

section .text

_main
    push s
    push fmt
    call _scanf

    add esp, 8
    push x
    push s
    push half

    call heron
    add esp, 12

    push [x + 4]
    push [x]
    push fmt

    call _printf
    add esp, 12

    mov ah,0
    mov al,0
    int_21h

    heron:
        push ecx
        push ebp
        push edx

        mov ebp, esp
        mov ecx, 10

    counter:
        mov edx, [ebp + 20]
        fld qword [edx]

        mov edx, [ebp + 24]
        fld qword [edx]

        fdiv st1, st0 

        faddp st1, st0

        mov edx, [ebp + 16]
        fld qword [edx]

        fmulp 

        mov edx, [ebp + 24]
        fstp qword [edx]

loop counter
        pop edx
        pop ebp
        pop ecx
    ret
