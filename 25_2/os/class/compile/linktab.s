linktab: 
    mov x1,x0
    cbz x1,.L1
    mov w0,0
.L3:
    ldr w2,[x1]
    add w0,w0,w2
    ldr x1,[x1,8]
    cbnz x1,.L3
.L2: 
    ret
.L1:
    mov w0,0
    b .L2