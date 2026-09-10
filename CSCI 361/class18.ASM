;Madison Grace Austin
;CSCI 361 spring 2025
;Programming Assignment #class 18
;I acknowledge that I have worked on this assignment independently, except where explicitly
;noted and referenced. Any collaboration or use of external resources has been properly cited.
;I am fully aware of the consequences of academic dishonesty and agree to abide by the university's
;academic integrity policy. I understand the importance and consequences of plagiarism.

org 100h
    global _start
    section .text
		_start:

			mov cl, 11
			_stackL:
				dec sp
				mov bp, sp		; filling stack with $
				mov al, '$'
				mov [bp],  al

			loop _stackL

			dec sp
			mov bp, sp
			xor al,al		; number of charactor written on our string on stack
			mov [bp], al

			dec sp
			mov bp, sp
			mov al, 11		; total numbers of characters 
			mov [bp], al


			; read input
			mov ah, 10
			mov dx, sp	; moving address of string off the stack in to dx
			int 21h

			mov bp, sp
			xor si, si
			xor bx, bx
			mov bl, [bp + 1]
			add si, bx
			add si, 2
			mov al, '$'
			mov [bp + si], al

			; validate input
			mov bp, sp
			mov bl, [bp + 1]
			cmp bl, 10
			jne _end

			; encryption

			call enc


			call printNL

			sub sp, 2
			mov [bp], dx

			call printO
			add sp, 2
			


		_end:
			mov ax, 4c00h
			int 21h

		enc:
			mov bp, sp
			add bp, 2
			mov cl, [bp + 1]
			mov si, 2
			_encry:
				mov al, [bp + si]
				ror al, 4
				xor al, 0AAh
				mov [bp + si], al
				inc si
			loop _encry
		ret

		printNL:
			mov ah,2
			mov dl, 10
			int 21h			; new line
			mov dl, 13
			int 21h
		ret
		
		printO:
			; print out
			mov ah, 9
			mov bp, sp
			add bp, 6 ;this is for moving past the intstructor pointer and the reading and writing of byte string
			mov dx, bp
			int 21h
		ret



;Write a program that encrypts a text string using two transformation steps:
; Rotate each character’s binary representation right by 4 bits.
; XOR the result with the value 0AAh.
; Read a 10-character ASCII string as input.
; If the input is not exactly 10 characters long, terminate immediately without displaying anything.
; Apply the encryption process to each character in the string.
; Store all input, intermediate values, and output in the STACK
; Display the encrypted output as a 10-character ASCII sequence in next line.