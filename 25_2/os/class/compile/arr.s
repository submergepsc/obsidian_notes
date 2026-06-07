array_sum:
    cmp x1,0
    ble .L1
    mov x2,x0
    add x3,x0,x1,sxtw 2  
    mov w0,0
.L3:
    ldr w1,[x2],4
    add w0,w0,w1
    cmp x3,x2
    bne .L3
.L2 : 
    ret
.L1 :
    mov w0,0
    b .L2
