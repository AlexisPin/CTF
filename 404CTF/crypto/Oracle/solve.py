#!/usr/bin/env python3

import pwn
from Crypto.Util.number import inverse, long_to_bytes, bytes_to_long
from sympy.ntheory.modular import crt
from math import gcd,sqrt,isqrt
import gmpy2
from tqdm import tqdm
import os
import re
import time
from factordb.factordb import FactorDB
e = 0x10001
REMOTE = 'challenges.404ctf.fr'
PORT = '31674'

N = []
C = []

while True:
  for _ in tqdm(range(1)):
    r = pwn.remote(REMOTE,PORT)
    #r = pwn.process('./oracle.py')
		
    r.recvuntil(b'l\'oracle!:\n')
    flag_ = r.recvline().rstrip()
    

    n_line = r.recvline().decode('utf-8')
    n_match = re.search(r"n°(0x[0-9a-f]+)", n_line)
    n = int(n_match.group(1), 16)
    
    f = FactorDB(n)
    primes = f.get_factor_list()
    while primes == []:
     r = pwn.remote(REMOTE,PORT)
     #r = pwn.process('./oracle.py')
		
     r.recvuntil(b'l\'oracle!:\n')
     flag_ = r.recvline().rstrip()
    

     n_line = r.recvline().decode('utf-8')
     n_match = re.search(r"n°(0x[0-9a-f]+)", n_line)
     n = int(n_match.group(1), 16)
     f = FactorDB(n)
     primes = f.get_factor_list()
     r.close()
    
    print(n)
    print(flag_)
    
    i = 1
    r.sendlineafter(b"oracle?\n", flag_[i:])
    ct = int(r.recvline().rstrip())
    pt = long_to_bytes(ct)
    while b"404CTF" not in pt:
     r.sendlineafter(b"oracle?\n", flag_[i:])
     ct = int(r.recvline().rstrip())
     i = i + 1
     pt = long_to_bytes(ct)
     
     
    print(pt)

    C.append(int(flag_))
    N.append(n)
    r.close()

  m = crt(N,C)[0]
  pt, _ = gmpy2.iroot(m, e)
  flag = long_to_bytes(pt)
  print(flag)


			
