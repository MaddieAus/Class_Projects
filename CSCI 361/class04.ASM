;Madison Grace Austin
;CSCI 361 spring 2025
;Programmming Assignment #class04
;I acknowledge that I have worked on this assignment independently, except where explicitly
;noted and referenced. Any collaboration or use of external resources has been properly cited.
;i am fully aware of the consequences of academic dishonesty an agree to abide by the university's
;academic intergrity policy. I understand the importance the consequences of plagiarism.
; with this assignment we are writing our name in ASCII
org 100h
    global _start
    section .text
        _start:
            mov ah,2 ; ah,2 has dl displays char
            mov dl,77 ; dl moves ASCII value M to dl
            int 21h

            mov ah,2
            mov dl,97
            int 21h

            mov ah,2
            mov dl,100
            int 21h

            mov ah,2
            mov dl,105
            int 21h

            mov ah,2
            mov dl,115
            int 21h

            mov ah,2
            mov dl,111
            int 21h

            mov ah,2
            mov dl,110
            int 21h

            mov ah,2
            mov dl,32
            int 21h

            mov ah,2
            mov dl,65
            int 21h

            mov ah,2
            mov dl,117
            int 21h

            mov ah,2
            mov dl,115
            int 21h

            mov ah,2
            mov dl,116
            int 21h

            mov ah,2
            mov dl,105
            int 21h

            mov ah,2
            mov dl,110
            int 21h
            
            mov ax, 4c00h
            int 21h;exit(0)
    section .data
