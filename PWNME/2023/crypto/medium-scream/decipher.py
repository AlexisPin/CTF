import pwn
from Crypto.Util.number import inverse, long_to_bytes, bytes_to_long
from Crypto.Util.Padding import pad
from sympy.ntheory.modular import crt
from math import gcd,sqrt,isqrt,exp, log
import gmpy2
from tqdm import tqdm
import os

e = 17
REMOTE = '51.68.95.78'
PORT = '32773'

def compute_n(ct_pt_arr):
	pt1, ct1 = ct_pt_arr[0]
	N = ct1 - pow(pt1, e)

	for pt,ct in ct_pt_arr:
		  N = gcd(ct - pow(pt, e), N)

	return N
  
N = []
C = []

while True:
  for _ in tqdm(range(3)):
    r = pwn.remote(REMOTE,PORT)

    ct_pt_arr = []
    for __ in range(20):
      r.recvuntil(b'> ')
      r.sendline(b'Encrypt')

      r.recvuntil(b'> ')
      m_ = os.urandom(32)

      r.sendline(str(bytes_to_long(m_)).encode())
      c = int(r.recvline())

      ct_pt_arr.append([bytes_to_long(pad(m_, 50)), c])


    r.recvuntil(b'> ')
    r.sendline(b'Flag')

    r.recvuntil(b':')
    flag_ = int(r.recvline())

    C.append(flag_)
    N.append(compute_n(ct_pt_arr))

    r.close()
  
  m = crt(N,C)[0]
  pt, _ = gmpy2.iroot(m, e)
  flag = long_to_bytes(pt)
  print(flag)


			
