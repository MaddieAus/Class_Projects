; Madison Grace Austin
; CSCI 361 Spring 2025
; Programming Assignment #class 21
; I acknowledge that I have worked on this assignment independently, except where explicitly
; noted and referenced. Any collaboration or use of external resources has been properly cited.
; I am fully aware of the consequences of academic dishonesty and agree to abide by the university's
; academic integrity policy. I understand the importance and consequences of plagiarism.


; I feel like this could have been shorter on my part but it just made since for me to do the code in pieces 

section .text
    global _start

_start:

    ; READ FIRST 8-BIT INPUT
    ; -----------------------------
    mov eax, 3          ; sys_read
    mov ebx, 0          ; stdin
    mov ecx, input1
    mov edx, 9
    int 0x80

    
    ; READ SECOND 8-BIT INPUT
    ; -----------------------------
    mov eax, 3
    mov ebx, 0
    mov ecx, input2
    mov edx, 9
    int 0x80


    ; CONVERT FIRST ASCII → BYTE
    ; -----------------------------
    mov esi, input1
    call ascii_to_byte
    mov bl, al          ; store first number

    
    ; CONVERT SECOND ASCII → BYTE
    ; -----------------------------
    mov esi, input2
    call ascii_to_byte
    mov bh, al          ; store second number

    

    ; CALL ADDITION PROCEDURE
    ; -----------------------------
    push bx
    call add_proc
    add esp, 2

    ; CONVERT RESULT → ASCII
    call byte_to_ascii

    ; PRINT RESULT (8 chars)
    mov eax, 4
    mov ebx, 1
    mov ecx, output
    mov edx, 9
    int 0x80
    ; CONVERT FIRST ASCII → BYTE
    ; -----------------------------
    mov esi, input1
    call ascii_to_byte
    mov bl, al          ; store first number

    
    ; CONVERT SECOND ASCII → BYTE
    ; -----------------------------
    mov esi, input2
    call ascii_to_byte
    mov bh, al          ; store second number
    
    ; CALL SUBTRACTION PROCEDURE
    ; -----------------------------
    push bx
    call sub_proc
    add esp, 2

    ; CONVERT RESULT → ASCII
    call byte_to_ascii

    ; PRINT RESULT (8 chars)
    mov eax, 4
    mov ebx, 1
    mov edx, 9
    mov ecx, output
    int 0x80

    
    ; EXIT PROGRAM
    ; -----------------------------
    mov eax, 1
    xor ebx, ebx
    int 0x80



; ASCII TO BYTE
; ==================================================
ascii_to_byte:
    xor al, al
    mov ecx, 8

convert_loop:
    shl al, 1
    mov dl, [esi]
    sub dl, '0'         ; convert ASCII → 0 or 1
    or al, dl
    inc esi
    loop convert_loop

    ret



; BYTE TO ASCII
; ==================================================
byte_to_ascii:
    mov ecx, 8
    mov edi, output

print_loop:
    shl al, 1
    jc print1
    mov dl, '0'
    mov [edi], dl
    jnc next_bit
    print1:
    mov dl, '1'
    mov [edi], dl

next_bit:
    inc edi
    loop print_loop
    mov byte [edi], 0xa

    ret



; ADDITION (SIGNED MAGNITUDE)
; BX contains inputs: BL is first number, BH is second number, Returns result in AX
; ==================================================
add_proc:
    mov al, bh
    xor al, bl
    bt ax, 7
    jc notsame

    mov al, bh
    add al, bl
    bt bx, 15
    jnc positive
    bts ax, 7
    jmp skip2

    positive:
    btr ax, 7

    skip2:
    jmp skip

    notsame:
    mov al,bh
    mov dx, bx
    btr ax, 7
    btr bx, 7
    btr bx, 15
    cmp al, bl
    jb bigger

    sub al, bl
    bt dx, 15
    jnc positive2
    bts ax, 7
    jmp skip3

    positive2:
    btr ax, 7

    skip3:
    jmp skip

    bigger:
    mov al, bl
    sub al, bh
    bt dx, 7
    jnc positive3
    bts ax, 7
    jmp skip4

    positive3:
    btr ax, 7

    skip4:

    skip:

    ret
; SUBTRACTION
; A - B = A + (-B)
; ==================================================
sub_proc:
    mov cx, 8
    neg:
    add cx, 7
    btc bx, cx
    sub cx, 7
    loop neg
    call add_proc    
    ret

section .bss
    input1 resb 8
    input2 resb 8
    output resb 8
