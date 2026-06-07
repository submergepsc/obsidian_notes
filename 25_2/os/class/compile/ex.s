	.arch armv8-a
	.file	"ex.c"
	.text
	.align	2
	.global	square
	.type	square, %function
square:
.LFB0:
	.cfi_startproc
	sub	sp, sp, #16
	.cfi_def_cfa_offset 16
	str	w0, [sp, 12]
	ldr	w0, [sp, 12]
	mul	w0, w0, w0
	add	sp, sp, 16
	.cfi_def_cfa_offset 0
	ret
	.cfi_endproc
.LFE0:
	.size	square, .-square
	.section	.rodata
	.align	3
.LC0:
	.string	"result = %d\n"
	.text
	.align	2
	.global	print_result
	.type	print_result, %function
print_result:
.LFB1:
	.cfi_startproc
	stp	x29, x30, [sp, -32]!
	.cfi_def_cfa_offset 32
	.cfi_offset 29, -32
	.cfi_offset 30, -24
	mov	x29, sp
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	nop
	ldp	x29, x30, [sp], 32
	.cfi_restore 30
	.cfi_restore 29
	.cfi_def_cfa_offset 0
	ret
	.cfi_endproc
.LFE1:
	.size	print_result, .-print_result
	.section	.rodata
	.align	3
.LC1:
	.string	"before printf"
	.align	3
.LC2:
	.string	"after printf"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
.LFB2:
	.cfi_startproc
	stp	x29, x30, [sp, -32]!
	.cfi_def_cfa_offset 32
	.cfi_offset 29, -32
	.cfi_offset 30, -24
	mov	x29, sp
	mov	w0, 3
	str	w0, [sp, 24]
	ldr	w0, [sp, 24]
	bl	square
	str	w0, [sp, 28]
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	puts
	ldr	w0, [sp, 28]
	bl	print_result
	adrp	x0, .LC2
	add	x0, x0, :lo12:.LC2
	bl	puts
	mov	w0, 0
	ldp	x29, x30, [sp], 32
	.cfi_restore 30
	.cfi_restore 29
	.cfi_def_cfa_offset 0
	ret
	.cfi_endproc
.LFE2:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0"
	.section	.note.GNU-stack,"",@progbits
