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
			mov ah, 1
			int 21h

			; read input


			; validate input


			; encryption


			; display


			; exit

			



		mov ax, 4c00h
		int 21h
	section .data

;Write a program that encrypts a text string using two transformation steps:
; Rotate each character’s binary representation right by 4 bits.
; XOR the result with the value 0AAh.
; Read a 10-character ASCII string as input.
; If the input is not exactly 10 characters long, terminate immediately without displaying anything.
; Apply the encryption process to each character in the string.
; Store all input, intermediate values, and output in the STACK
; Display the encrypted output as a 10-character ASCII sequence in next line.