section .text
    global _start

_start:

    ; PRINT PROMPT
    ; -----------------------------
    mov eax, 4          ; sys_write
    mov ebx, 1          ; stdout
    mov ecx, prompt
    mov edx, prompt_len
    int 0x80


    ; READ INPUT (11 characters)
    ; -----------------------------
    mov eax, 3          ; sys_read
    mov ebx, 0          ; stdin
    mov ecx, buffer
    mov edx, 11
    int 0x80


    ; GET SHIFT VALUE
    ; -----------------------------
    mov al, [buffer + 10] ; last character
    sub al, '0'         ; ASCII -> number
    mov bl, al          ; store shift in BL


    ; PROCESS 10 CHARACTERS
    ; -----------------------------
    mov ecx, 10
    mov esi, buffer

process_loop:

    mov al, [esi]


    ; CHECK lowercase a-z
    ; -----------------------------
    cmp al, 'a'
    jl check_upper
    cmp al, 'z'
    jg check_upper

    ; convert lowercase -> uppercase
    btc eax, 5

check_upper:


    ; CHECK uppercase A-Z
    ; -----------------------------
    cmp al, 'A'
    jl next_char
    cmp al, 'Z'
    jg next_char


    ; APPLY CAESAR SHIFT
    ; -----------------------------
    add al, bl

    cmp al, 'Z'
    jle store_char

    sub al, 26

store_char:
    mov [esi], al

next_char:
    inc esi
    loop process_loop

    ; PRINT RESULT (10 chars)
    ; -----------------------------
    mov eax, 4
    mov ebx, 1
    mov ecx, buffer
    mov edx, 10
    int 0x80

    ; EXIT
    ; -----------------------------
    mov eax, 1
    xor ebx, ebx
    int 0x80


section .data
    prompt db 'Enter 10 characters followed by a digit: ' ; this was in the esample code that was given to us and it looked nice so i kept it
    prompt_len equ $ - prompt

section .bss
    buffer resb 11

    ; how to run on virtual:
    ; open new terminal, make sure you are in codes, 
    ; cd into asm (where ever the code is written),
    ;./main