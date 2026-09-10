;Madison Grace Austin
;CSCI 361 spring 2025
;Programmming Assignment #class 08
;I acknowledge that I have worked on this assignment independently, except where explicitly
;noted and referenced. Any collaboration or use of external resources has been properly cited.
;i am fully aware of the consequences of academic dishonesty an agree to abide by the university's
;academic intergrity policy. I understand the importance the consequences of plagiarism.
; with this assignment we will using jump to print our name based on key pressed

org 100h
    global _start
        ; ah,2 has dl displays char
        ; dl moves ASCII value M to dl
    section .text
            _start:
                mov ah, 1 ; waiting for input
                int 21h

                cmp al, 65
                jae which

            which:
                cmp al, 97
                jb fname

                cmp al 123
                jb lname

                mov ax, 4c00h ; just incase
                int 21h

            fname:
                mov ah, 2
                mov bx, _a
                mov dl, [bx]
                int 21h

                mov ah, 2
                add bx, 1
                mov dl, [bx]
                int 21h

                mov ah, 2
                add bx, 1
                mov dl, [bx]
                int 21h

                mov ah, 2
                add bx, 1
                mov dl, [bx]
                int 21h

                mov ah, 2
                add bx, 1
                mov dl, [bx]
                int 21h

                mov ah, 2
                add bx, 1
                mov dl, [bx]
                int 21h

                mov ah, 2
                add bx, 1
                mov dl, [bx]
                int 21h
                jmp end

            lname:
                mov ah, 2
                mov bx, _b
                mov dl, [bx]
                int 21h

                mov ah, 2
                add bx, 1
                mov dl, [bx]
                int 21h

                mov ah, 2
                add bx, 1
                mov dl, [bx]
                int 21h

                mov ah, 2
                add bx, 1
                mov dl, [bx]
                int 21h

                mov ah, 2
                add bx, 1
                mov dl, [bx]
                int 21h

                mov ah, 2
                add bx, 1
                mov dl, [bx]
                int 21h
            end:
                mov ax, 4c00h
                int 21h;exit(0)
    section .data
    ; Madison Austin
    _a db "Madison" ; 77,97,100,105,115,111,110
    _b db "Austin" ; 65,117,115,116,105,110
