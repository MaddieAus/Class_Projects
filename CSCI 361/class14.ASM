;Madison Grace Austin
;CSCI 361 spring 2025
;Programming Assignment #class 14
;I acknowledge that I have worked on this assignment independently, except where explicitly
;noted and referenced. Any collaboration or use of external resources has been properly cited.
;I am fully aware of the consequences of academic dishonesty and agree to abide by the university's
;academic integrity policy. I understand the importance and consequences of plagiarism.
org 100h
    global _start
    section .text
        _start:
            mov cx, 8
            mov dx, buffer
            call _readin

            mov cx, 8
            mov dx, buffer
            call _convert

            mov al, [t]
            mov [a], al
            call _newline

            mov cx, 8
            mov dx, buffer
            call _readin

            mov cx, 8
            mov dx, buffer
            call _convert

            mov al, [t]
            mov [b], al

            ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            call _newline
            mov cl, [a]
            mov dl, [b]

            call _and
            mov cx, 8
            mov dl, al
            call _print
            call _newline ;;;

            mov cl, [a]
            mov dl, [b]
            call _or
            mov cx, 8
            mov dl, al
            call _print
            call _newline ;;;

            mov cl, [a]
            mov dl, [b]
            call _xor
            mov cx, 8
            mov dl, al
            call _print
            call _newline ;;;

            mov cl, [a]
            call _not
            mov cx, 8
            mov dl, al
            call _print
            call _newline ;;;

            mov cl, [b]
            call _not
            mov cx, 8
            mov dl, al
            call _print
            call _newline ;;;

            mov cl, [a]
            mov dl, [b]
            call _nand
            mov cx, 8
            mov dl, al
            call _print
            call _newline ;;;

            mov cl, [a]
            mov dl, [b]
            call _nor
            mov cx, 8
            mov dl, al
            call _print
            call _newline ;;;

            mov cl, [a]
            mov dl, [b]
            call _xnor
            mov cx, 8
            mov dl, al
            call _print

            ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
            mov ax, 4c00h
            int 21h
            ;reading input


            _readin:
                xor di, di ; DI is used as the destination index
                mov bx, dx ; Copy of the destination address
                mov ah, 1
                .loop: ; Local label instead of a global one
                    cmp di, cx ; Check condition
                    je .end1 ; like di < cx
                    int 21h ; Read key into AL
                    sub al, '0' ; this converts into decimal
                    mov [bx + di], al
                    inc di
                    jmp .loop
                    .end1:
                 ret
            ;converting binary into byte


            _convert:
                mov bx, dx
                xor si, si
                mov al, 128
                mov [af], al
                mov al, 0
                mov [t], al
                .loop:
                    mov al, [bx + si]
                    inc si
                    mov [t2], bx
                    cmp al, 0
                    jz .jumpz
                    mov dl,[af]
                    add [t], dl

                    .jumpz:
                    mov al, [af]
                    xor ah, ah
                    mov bl, 2
                    div bl
                    mov bx, [t2]
                    mov [af], al
                loop .loop
                ret

            _newline:
                mov ah, 2
                mov dl, 10
                int 21h
                mov dl, 13
                int 21h
            ret
            ;printing the byte as binary


            _print:
                mov al, 128
                mov [af], al
                mov [t], dl
                .loop:
                    mov al, [af]
                    cmp [t], al
                    jb .printz
                    mov ah, 2
                    mov dl, '1'
                    int 21h

                    mov al, [af]
                    sub [t], al
                    jmp .end
                .printz:
                    mov ah, 2
                    mov dl, '0'
                    int 21h
                .end:
                    xor ah, ah
                    mov al, [af]
                    mov bl, 2
                    div bl
                    mov [af], al
                    loop .loop
                ret


            ;funtion for each logic operator
            _and:
                mov al, cl
                and al, dl
            ret

            _or:
                mov al, cl
                or al, dl
            ret

            _xor:
                mov al, cl
                xor al, dl
            ret

            _not:
                mov al, cl
                not al
            ret

            _nand:
                call _and
                not al
            ret

            _nor:
                call _or
                not al
            ret

            _xnor:
                call _xor
                not al
            ret

    section .bss
        buffer resb 8
        a resb 1
        b resb 1
        t resb 1
        af resb 1
        t2 resb 2
