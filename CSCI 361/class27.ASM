; Madison Grace Austin
; CSCI 361 Spring 2025
; Programming Assignment #class 27
; I acknowledge that I have worked on this assignment independently, except where explicitly
; noted and referenced. Any collaboration or use of external resources has been properly cited.
; I am fully aware of the consequences of academic dishonesty and agree to abide by the university's
; academic integrity policy. I understand the importance and consequences of plagiarism.


%define int_21h call _interupt_21h
global _main
extern _interupt_21h

section .text

; ============================================
; calling 
; ============================================
_main:
    call read_input        
    call validate_input    
    call parse_binary      
    call extract_fields    
    call compute_value     
    call print_result      
    jmp exit_program       

; ============================================
; READ INPUT 
; ============================================
read_input:
    mov ah, 10
    mov edx, buf
    int_21h
    ret

; ============================================
; VALIDATE INPUT
; ============================================
validate_input:
    mov al, [buf+1]        ; actual number of chars entered
    cmp al, 32
    jne exit_program       ; exit if not exactly 32

    mov ecx, 32
    mov esi, buf+2         ; start of actual input

check_loop:
    mov al, [esi]
    cmp al, '0'
    je valid_char
    cmp al, '1'
    je valid_char
    jmp exit_program       ; invalid character → exit

valid_char:
    inc esi
    loop check_loop        ; repeat for all 32 characters
    ret

; ============================================
; PARSE ASCII → BINARY
; ============================================
parse_binary:
    xor eax, eax           ; clear result register
    mov ecx, 32
    mov esi, buf+2

parse_loop:
    shl eax, 1             ; shift left (make room for next bit)

    mov bl, [esi]
    cmp bl, '1'
    jne skip_set
    or eax, 1              ; if '1', set lowest bit

skip_set:
    inc esi
    loop parse_loop

    mov [binary_value], eax
    ret

; ============================================
; EXTRACT
; ============================================
extract_fields:
    mov eax, [binary_value]

    ; extract sign (bit 31)
    mov ebx, eax
    shr ebx, 31
    mov [sign], bl

    ; extract exponent (bits 30–23)
    mov ebx, eax
    shr ebx, 23
    and ebx, 0FFh
    mov [exponent], ebx

    ; extract mantissa (bits 22–0)
    mov ebx, eax
    and ebx, 7FFFFFh
    mov [mantissa], ebx

    ret

; ============================================
; COMPUTE VALUE MATH
; ============================================
compute_value:

mov ebx, [mantissa]
mov [fraction], ebx
mov eax, [exponent]
cmp eax, 127

ja leftsh

mov [shift], eax
mov eax, 127
sub eax, [shift]
mov [shift], eax
mov cl, [shift]
mov esi, 1 ; int_part currently
mov edx, [mantissa]
shl edx, 9

_rightsh:

loop _rightsh
        shr edx, 1
        shr esi, 1

        jnc checkhigh1
        bts edx, 31

checkhigh1:

jmp skipleft


leftsh:
    sub eax, 127
    mov [shift], eax
    mov ecx, ecx
    mov cl, [shift]
    mov esi, 1 ; int_part currently
    mov edx, [mantissa]
    shl edx, 9

    _loopleft:
        shl esi, 1
        shl edx, 1

        jnc checkhigh
        bts esi, 0

checkhigh:

loop _loopleft

skipleft:


mov [int_part], esi
shr edx, 16
mov [fraction], edx

ret

; ============================================
; PRINT INTEGER
; ============================================
print_int:

    mov ebx, 10000
    divLoop:
        xor edx, edx
        div ebx

        mov esi, edx
        mov edx, eax
        add dl, '0'
        mov ah, 2
        int_21h

        xor edx, edx
        mov eax, ebx
        mov ebx, 10
        div ebx
        mov ebx, eax
        mov eax, esi
        cmp ebx, 1

        ja divLoop

        mov edx, esi
        add dl, '0'
        mov ah, 2
        int_21h
        
        ret



; ============================================
; PRINT FINAL 
; ============================================
print_result:

    ; ----- print sign -----
    mov al, [sign]
    cmp al, 0
    je positive

    mov dl, '-'
    jmp print_sign

positive:
    mov dl, '+'

print_sign:
    mov ah, 2
    int_21h

    ; ----- print integer part -----
    mov eax, [int_part]
    call print_int

    ; ----- print decimal point -----
    mov dl, '.'
    mov ah, 2
    int_21h

    ; ----- print fraction -----
    mov eax, [fraction]
    call print_int

    ; ----- print "/65535" -----
    mov edx, frac_str
    mov ah, 9
    int_21h

    ret

; ============================================
; EXIT PROGRAM
; ============================================
exit_program:
    mov ah, 0
    mov al, 0
    int_21h

section .data

; input buffer (DOS format)
buf db 33                  ; max length
    db 0                   ; actual length entered
times 33 db 0              ; storage

; IEEE fields
binary_value dd 0
sign         db 0
exponent     dd 0
mantissa     dd 0
shift       db 0

; computed values
fraction dd 0
int_part dd 0
exp_val  dd 0

; buffer for printing numbers
digit_buffer times 12 db 0

; output string
frac_str db "/65535", 0