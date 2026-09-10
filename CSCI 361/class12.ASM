;Madison Grace Austin
;CSCI 361 spring 2025
;Programming Assignment #class 12
;I acknowledge that I have worked on this assignment independently, except where explicitly
;noted and referenced. Any collaboration or use of external resources has been properly cited.
;I am fully aware of the consequences of academic dishonesty and agree to abide by the university's
;academic integrity policy. I understand the importance and consequences of plagiarism.

org 100h
    global _start
    section .text
        _start:
            mov ah, 1 ; input
            int 21h

            _input_1:
                sub al, '0' ; convert ASCII to number
                cmp al, 0
                
                je _equalZ

            _notZ:
                jmp _endif

            _equalZ:
                add al, 1

            _endif:
                mov [_I], al ; moving al in to _I

                call factorial
                mov ah, 2
                mov dl, 10
                int 21h
                mov dl, 13
                int 21h

            after_factorial:

                ; Ten-thousands place
                mov ax, [_F]
                mov bx, 10000
                xor dx, dx
                div bx
                mov [_A], ax
                mov [_F], dx
                mov al, [_A]
                add al, '0'
                mov dl, al
                mov ah, 2
                int 21h
                mov ax, dx

                ; Thousands place
                mov ax, [_F]
                mov bx, 1000
                xor dx, dx
                div bx
                mov [_A], ax
                mov [_F], dx
                mov al, [_A]
                add al, '0'
                mov dl, al
                mov ah, 2
                int 21h
                mov ax, dx

                ; Hundreds place
                mov ax, [_F]
                mov bx, 100
                xor dx, dx
                div bx
                mov [_A], ax
                mov [_F], dx
                mov al, [_A]
                add al, '0'
                mov dl, al
                mov ah, 2
                int 21h
                mov ax, dx

                ; Tens place
                mov ax, [_F]
                mov bx, 10
                xor dx, dx
                div bx
                mov [_A], ax
                mov [_F], dx
                mov al, [_A]
                add al, '0'
                mov dl, al
                mov ah, 2
                int 21h
                mov ax, dx

                ; Ones place
                mov ax, [_F]
                mov bx, 1
                xor dx, dx
                div bx
                mov [_A], ax
                mov [_F], dx
                mov al, [_A]
                add al, '0'
                mov dl, al
                mov ah, 2
                int 21h
                mov ax, dx
                mov ax, 4c00h ; stop
                int 21h

            factorial:
                mov bl, [_I] ; moving in to bl
                mov cl, bl

                _math: ; math for the factorial
                    mov ax, [_F] ; ax "auto" goes against bx
                    mul bx
                    mov [_F], ax
                    dec bl
                    loop _math
                    ret

            _print:

    section .data
    _I db 0
    _F dw 1
    _A db 0
