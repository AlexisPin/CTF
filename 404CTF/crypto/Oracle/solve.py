#!/usr/bin/env python3

import pwn
from Crypto.Util.number import inverse, long_to_bytes, bytes_to_long
from sympy.ntheory.modular import crt
from math import gcd,sqrt,isqrt
import gmpy2
from tqdm import tqdm
import os
import re

e = 65537
REMOTE = 'challenges.404ctf.fr'
PORT = '31674'

N = []
C = []

while True:
  for _ in tqdm(range(3)):
    #r = pwn.remote(REMOTE,PORT)
    r = pwn.process('./oracle.py')
		
    r.recvuntil(b'l\'oracle!:\n')
    flag_ = int(r.recvline())

    n_line = r.recvline().decode('utf-8')
    n_match = re.search(r"n°(0x[0-9a-f]+)", n_line)
    n = int(n_match.group(1), 16)

    C.append(flag_)
    N.append(n)
    print(C)
    print('\n')
    print(N)
    r.close()

  m = crt(N,C)[0]
  pt, _ = gmpy2.iroot(m, e)
  flag = long_to_bytes(pt)
  print(flag)


			
