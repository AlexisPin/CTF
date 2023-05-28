#!/usr/bin/env python3

from pwn import *

context.binary = exe = ELF("./cache_cache_le_retour")

r = process([exe.path])
#r = remote("challenges.404ctf.fr", 31725)
gdb.attach(r)

        

def main():

	r.interactive()


if __name__ == "__main__":
    main()
