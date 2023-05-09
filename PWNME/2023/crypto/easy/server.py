from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

FLAG = "PWNME{redacted}"
KEY = os.urandom(16)
iv = os.urandom(16)
print(str(iv))
print(len(os.urandom(2).hex()))

def encrypt_data(data):
    padded = pad(FLAG.encode(), 16)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(padded)
    return encrypted.hex()


def encrypt_flag():
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(FLAG.encode(), 16))
    signature = [hex(a ^ b)[2:].zfill(2) for a, b in zip(iv, KEY[::-1])]
    signature = "".join(signature)
    ciphertext = iv.hex()[4:] + encrypt_data(FLAG) + signature
    return {"ciphertext": ciphertext}
    

