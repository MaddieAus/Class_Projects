;Madison Grace Austin
;CSCI 361 spring 2025
;Programming Assignment #class 16
;I acknowledge that I have worked on this assignment independently, except where explicitly
;noted and referenced. Any collaboration or use of external resources has been properly cited.
;I am fully aware of the consequences of academic dishonesty and agree to abide by the university's
;academic integrity policy. I understand the importance and consequences of plagiarism.

org 100h
	global _start
	section .text
		_start:
		;reading in the number

		mov ah, 1 ; stores in al
		int 21h

		sub al, '0'
		cmp al, 0
		je _zero
		jmp _notzero


		_zero:
			inc al

		_notzero:
			

		sub sp, 1
		mov bp, sp
		mov [bp], al

		sub sp, 2
		mov bp, sp

		mov ax, 1

		mov [bp], ax

		call _fact
		call _div
		mov ah, 2
		mov dl, 10
		int 21h
		mov dl, 13
		int 21h

		call _print

		mov ax, 4c00h
		int 21h

		;finding the factorial

		_fact:
			mov bp, sp
			mov cl, [bp + 4]
			mov ax, [bp + 2]
			xor bh, bh

			.factorial:
				mov bl, cl
				mul bx
				loop .factorial

			mov [bp + 2], ax
		ret


		;finding each unit value

		_div:
			mov bp, sp
			mov si, [bp]
			mov ax, [bp + 2]
			inc bp
			xor cl, cl
			.divs:
				xor dx, dx
				mov bx, 10
				div bx
				mov [bp], dl
				dec bp
				inc cl
				cmp ax, 0
				je _exit
				jmp .divs

			_exit:

			dec bp
			mov [bp], cl
			sub bp, 2
			mov [bp], si
			mov sp, bp
		ret

		;printing
		_print:
			add bp, 2
			mov cl,[bp]
			inc bp

			mov ah, 2
			
			.loop:
				inc bp
				mov dl,[bp]
				add dl, '0'
				int 21h
			loop .loop
		ret



