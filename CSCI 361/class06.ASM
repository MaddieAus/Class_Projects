;Madison Grace Austin
;CSCI 361 spring 2025
;Programmming Assignment #class06
;I acknowledge that I have worked on this assignment independently, except where explicitly
;noted and referenced. Any collaboration or use of external resources has been properly cited.
;i am fully aware of the consequences of academic dishonesty an agree to abide by the university's
;academic intergrity policy. I understand the importance the consequences of plagiarism.
; with this assignment we are writing our name in ASCII but using bx

org 100h
    global _start
    ; ah,2 has dl displays char
    ; dl moves ASCII value M to dl
    section .text
        _start:
            mov bx,_a ; this is going in to the array
            mov dl, [bx]
            mov ah, 2
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

            mov ah, 2
            add bx, 1
            mov dl, [bx]
            int 21h
            
            mov ah,2
            mov ax, 4c00h
            int 21h;exit(0)

    section .data
    ; Madison Austin
    _a db 77,97,100,105,115,111,110,32,65,117,115,116,105,110 ;the array
    ;M a d i s o n space A u t
