#!/usr/bin/env python3

from sympy import symbols, Eq, solve
import hashlib
from egcd import egcd
from Crypto.Cipher import AES
from Crypto.Util.number import inverse

p = 231933770389389338159753408142515592951889415487365399671635245679612352781
mod = p
a, b = symbols('a b')
Gx, Gy = 93808707311515764328749048019429156823177018815962831703088729905542530725, 144188081159786866301184058966215079553216226588404139826447829786378964579
Hx, Hy = 139273587750511132949199077353388298279458715287916158719683257616077625421, 30737261732951428402751520492138972590770609126561688808936331585804316784


def find_a_and_b(x1, y1, x2, y2, n):
    x_diff = x1 - x2

    if x_diff == 0:
        print("No inverse exists.")
        return None

    gcd, inverse, _ = egcd(x_diff, n)

    if gcd == 1:
        a = (y1**2 - y2**2) * inverse % n
        b = (y1**2 - (x1**3 + a * x1)) % n
        return a, b
    else:
        print("No inverse exists.")
        return None

n = p  # Modulus

a, b = find_a_and_b(Gx, Gy, Hx, Hy, n)

print("Retrieved a:", a)
print("Retrieved b:", b)

key = str(a) + str(b)

cipher = bytes.fromhex("8233d04a29befd2efb932b4dbac8d41869e13ecba7e5f13d48128ddd74ea0c7085b4ff402326870313e2f1dfbc9de3f96225ffbe58a87e687665b7d45a41ac22")
iv = bytes.fromhex("00b7822a196b00795078b69fcd91280d")
aes = AES.new(hashlib.sha1(key.encode()).digest()[:16], AES.MODE_CBC, iv=iv)
flag = aes.decrypt(cipher)
print(flag)

