;Madison Grace Austin
;CSCI 361 spring 2025
;Programmming Assignment #class 10
;I acknowledge that I have worked on this assignment independently, except where explicitly
;noted and referenced. Any collaboration or use of external resources has been properly cited.
;i am fully aware of the consequences of academic dishonesty an agree to abide by the university's
;academic intergrity policy. I understand the importance the consequences of plagiarism.
; with this assignment is a simple calculator


org 100h
    global _start
    section .text
        _start:
            mov ah, 1
            int 21h
            _input_1:
                sub al, '0' ; input 1
                mov [_I], al
            mov ah, 1
            int 21h

            _input_2:
                sub al, '0' ; input 2
                mov [_B], al

            ;_newline:
                mov ah, 2
                mov dl, 13
                int 21h ; this makes a new line
                mov ah, 2
                mov dl, 10
                int 21h

            ;;;;;;;;;;;;;;;;addition;;;;;;;;;;;;;;;;;;;;;;;;;;;
            mov bl, [_I]
            add bl, [_B] ; addition and moving that into val
            mov [val], bl

            mov al, [val]
            mov ah, 0
            mov bx, 0a00h ; his divides by 10 (val is in between 1-10)

            div bh

            mov [_Rem], ah ; the _Rem gets moved to _Stor
            mov [_Stor], al

            mov ah, 2
            mov dl, [_Stor] ; this adds 0 to get the ascii and prints
            add dl, '0'
            int 21h

            mov ah, 2
            mov dl, [_Rem]
            add dl, '0'
            int 21h

            mov ah, 2
            mov dl, 32 ;space
            int 21h

            ;;;;;;;;;;;;;;;;subtraction;;;;;;;;;;;;;;;;;;;;;;;;;;;
            mov bl, [_I]
            sub bl, [_B]
            mov [val], bl

            jb check

            mov al, [val]
            mov ah, 0
            mov bx, 0a00h ; this divides by 10 (val is in between1-10)

            div bh

            mov [_Rem], ah ; the _Rem gets moved to _Stor
            mov [_Stor], al

            mov ah, 2
            mov dl, [_Stor] ; this adds 0 to get the ascii and prints
            add dl, '0'
            int 21h

            mov ah, 2
            mov dl, [_Rem]
            add dl, '0'
            int 21h

            jmp nah

            check:
            mov ah,2
            mov dl, 'N'
            int 21h
            mov ah,2
            mov dl, 'R'
            int 21h
            
            nah:
            mov ah, 2
            mov dl, 32 ;space
            int 21h

            ;;;;;;;;;;;;;mult.;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            mov al, [_I]
            mov ah, [_B]
            mul ah
            mov [val], al
            mov al, [val]
            mov ah, 0
            mov bx, 0a00h ; this divides by 10 (val is in between1-10)

            div bh

            mov [_Rem], ah ; the _Rem gets moved to _Stor
            mov [_Stor], al

            mov ah, 2
            mov dl, [_Stor] ; this adds 0 to get the ascii and prints
            add dl, '0'
            int 21h

            mov ah, 2
            mov dl, [_Rem]
            add dl, '0'
            int 21h

            mov ah, 2
            mov dl, 32 ;space
            int 21h

            ;;;;;;;;;;;;;div.;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            mov ax, 0

            mov al, [_B]
            cmp al, 0

            jnz check2
            mov ah,2
            mov dl, 'N'
            int 21h

            mov ah,2
            mov dl, 'N'
            int 21h

            jmp stop

            check2:
            mov al, [_I]
            mov bh, [_B]
            div bh
            mov [van], al
            mov [val], ah
            mov al, [van]
            mov ah, 0
            mov bx, 0a00h ; this divides by 10 (val is in between1-10)

            div bh

            mov [_Rem], ah ; the _Rem gets moved to _Stor
            mov [_Stor], al

            mov ah, 2
            mov dl, [_Stor] ; this adds 0 to get the ascii and prints
            add dl, '0'
            int 21h

            mov ah, 2
            mov dl, [_Rem]
            add dl, '0'
            int 21h

            mov al, [val]
            mov ah, 0
            mov bx, 0a00h ; this divides by 10 (val is in between1-10)

            div bh

            mov [_Rem], ah ; the _Rem gets moved to _Stor
            mov [_Stor], al

            mov ah, 2
            mov dl, [_Stor] ; this adds 0 to get the ascii and prints
            add dl, '0'
            int 21h

            mov ah, 2
            mov dl, [_Rem]
            add dl, '0'
            int 21h
            mov ah, 2
            mov dl, 32 ;space
            int 21h
            
            stop:
            mov ax, 4c00h
            int 21h;exit(0)

    section .data
    val db 0
    van db 0
    _I db 0 ; first number
    _B db 0 ; second number
    _Stor db 0
    _Rem db 0
