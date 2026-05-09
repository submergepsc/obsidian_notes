	.arch armv8.1-a+crc
	.file	"counter_atomic.c"
	.text
	.align	2
	.p2align 4,,11
	.type	worker, %function
worker:
.LFB40:
	.cfi_startproc
	adrp	x3, .LANCHOR0
	ldr	x0, [x3, #:lo12:.LANCHOR0]
	cmp	x0, 0
	ble	.L2
	add	x3, x3, :lo12:.LANCHOR0
	mov	x0, 0
	add	x1, x3, 8
	mov	x4, 1
	.p2align 3,,7
.L3:
	ldadd	x4, x2, [x1]
	ldr	x2, [x3]
	add	x0, x0, 1
	cmp	x2, x0
	bgt	.L3
.L2:
	mov	x0, 0
	ret
	.cfi_endproc
.LFE40:
	.size	worker, .-worker
	.section	.rodata.str1.8,"aMS",@progbits,1
	.align	3
.LC0:
	.string	"usage: %s <n_threads> <iters_per_thread>\n"
	.align	3
.LC1:
	.string	"malloc"
	.align	3
.LC2:
	.string	"expected = %ld, counter = %ld, lost = %ld, time = %.6f\n"
	.section	.text.startup,"ax",@progbits
	.align	2
	.p2align 4,,11
	.global	main
	.type	main, %function
main:
.LFB41:
	.cfi_startproc
	sub	sp, sp, #128
	.cfi_def_cfa_offset 128
	adrp	x2, :got:__stack_chk_guard
	ldr	x2, [x2, :got_lo12:__stack_chk_guard]
	stp	x29, x30, [sp, 48]
	.cfi_offset 29, -80
	.cfi_offset 30, -72
	add	x29, sp, 48
	stp	x19, x20, [sp, 64]
	.cfi_offset 19, -64
	.cfi_offset 20, -56
	mov	x19, x1
	ldr	x1, [x2]
	str	x1, [sp, 40]
	mov	x1, 0
	cmp	w0, 3
	beq	.L7
	adrp	x0, :got:stderr
	ldr	x0, [x0, :got_lo12:stderr]
	adrp	x2, .LC0
	ldr	x3, [x19]
	add	x2, x2, :lo12:.LC0
	ldr	x0, [x0]
	mov	w1, 2
	bl	__fprintf_chk
	mov	w0, 1
	b	.L6
.L7:
	ldr	x0, [x19, 8]
	mov	w2, 10
	mov	x1, 0
	stp	x21, x22, [sp, 80]
	.cfi_offset 22, -40
	.cfi_offset 21, -48
	stp	x23, x24, [sp, 96]
	.cfi_offset 24, -24
	.cfi_offset 23, -32
	str	x25, [sp, 112]
	.cfi_offset 25, -16
	bl	strtol
	mov	x20, x0
	mov	w23, w0
	sxtw	x24, w0
	mov	x1, 0
	ldr	x0, [x19, 16]
	mov	w2, 10
	adrp	x25, .LANCHOR0
	bl	strtol
	mov	x1, x0
	sbfiz	x0, x20, 3, 32
	str	x1, [x25, #:lo12:.LANCHOR0]
	bl	malloc
	mov	x21, x0
	cbz	x0, .L18
	add	x1, sp, 8
	mov	w0, 1
	bl	clock_gettime
	cmp	w20, 0
	ble	.L11
	sub	w20, w20, #1
	add	x0, x21, 8
	adrp	x22, worker
	mov	x19, x21
	add	x20, x0, w20, uxtw 3
	add	x22, x22, :lo12:worker
	.p2align 3,,7
.L12:
	mov	x0, x19
	mov	x2, x22
	mov	x3, 0
	mov	x1, 0
	add	x19, x19, 8
	bl	pthread_create
	cmp	x19, x20
	bne	.L12
	mov	x19, 0
	.p2align 3,,7
.L13:
	ldr	x0, [x21, x19, lsl 3]
	mov	x1, 0
	add	x19, x19, 1
	bl	pthread_join
	cmp	w23, w19
	bgt	.L13
.L11:
	add	x1, sp, 24
	mov	w0, 1
	bl	clock_gettime
	add	x0, x25, :lo12:.LANCHOR0
	add	x0, x0, 8
	ldr	x3, [x0]
	ldp	x2, x4, [sp, 8]
	mov	x1, 225833675390976
	ldp	x5, x0, [sp, 24]
	movk	x1, 0x41cd, lsl 48
	fmov	d1, x1
	adrp	x1, .LC2
	add	x1, x1, :lo12:.LC2
	sub	x0, x0, x4
	sub	x5, x5, x2
	ldr	x2, [x25, #:lo12:.LANCHOR0]
	scvtf	d0, x0
	mov	w0, 2
	mul	x2, x24, x2
	fdiv	d0, d0, d1
	scvtf	d1, x5
	sub	x4, x2, x3
	fadd	d0, d0, d1
	bl	__printf_chk
	mov	x0, x21
	bl	free
	ldp	x21, x22, [sp, 80]
	.cfi_restore 22
	.cfi_restore 21
	mov	w0, 0
	ldp	x23, x24, [sp, 96]
	.cfi_restore 24
	.cfi_restore 23
	ldr	x25, [sp, 112]
	.cfi_restore 25
.L6:
	adrp	x1, :got:__stack_chk_guard
	ldr	x1, [x1, :got_lo12:__stack_chk_guard]
	ldr	x3, [sp, 40]
	ldr	x2, [x1]
	subs	x3, x3, x2
	mov	x2, 0
	bne	.L19
	ldp	x29, x30, [sp, 48]
	ldp	x19, x20, [sp, 64]
	add	sp, sp, 128
	.cfi_remember_state
	.cfi_restore 29
	.cfi_restore 30
	.cfi_restore 19
	.cfi_restore 20
	.cfi_def_cfa_offset 0
	ret
.L19:
	.cfi_restore_state
	stp	x21, x22, [sp, 80]
	.cfi_offset 22, -40
	.cfi_offset 21, -48
	stp	x23, x24, [sp, 96]
	.cfi_offset 24, -24
	.cfi_offset 23, -32
	str	x25, [sp, 112]
	.cfi_offset 25, -16
	bl	__stack_chk_fail
.L18:
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	perror
	ldp	x21, x22, [sp, 80]
	.cfi_restore 22
	.cfi_restore 21
	mov	w0, 1
	ldp	x23, x24, [sp, 96]
	.cfi_restore 24
	.cfi_restore 23
	ldr	x25, [sp, 112]
	.cfi_restore 25
	b	.L6
	.cfi_endproc
.LFE41:
	.size	main, .-main
	.bss
	.align	3
	.set	.LANCHOR0,. + 0
	.type	iters_per_thread, %object
	.size	iters_per_thread, 8
iters_per_thread:
	.zero	8
	.type	counter, %object
	.size	counter, 8
counter:
	.zero	8
	.ident	"GCC: (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0"
	.section	.note.GNU-stack,"",@progbits
