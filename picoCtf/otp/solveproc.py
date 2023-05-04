from pwn import *
p = process(["gdb", "./otp"])
p.recvuntil("(gdb)")
p.sendline("break strncmp@plt")
p.recvuntil("(gdb)")
chars = "0123456789abcdef"
sofar=""

for j in range(100):
	for i in chars:
		p.sendline("run "+sofar+i+"1"*(99-j))
		p.recvuntil("(gdb)")
		p.sendline("x/s $rsi")
		first=(p.recvuntil("(gdb)")).decode()
		p.sendline("x/s $rdi")
		second=(p.recvuntil("(gdb)")).decode()
		if first[26+j]==second[26+j]:
			sofar += i
			print(sofar)
			break
