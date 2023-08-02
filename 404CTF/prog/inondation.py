#!/usr/bin/env python3

from pwn import *
import time

pattern = "~c`°^)"

io = remote("challenges.404ctf.fr", 31420)

io.recvline()
io.recvline()

for i in range(100):
	rhino = io.recvuntil(b'Combien')
	n = rhino.decode().count(pattern)
	io.sendlineafter(b'> ', str(n).encode())

print(io.recv().decode())

io.interactive()
