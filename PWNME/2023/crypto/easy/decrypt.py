from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad,pad


cyphertext = "ec99a438e52de135ad277039ce232c148aedd7c3f9a0688a3c95b6de4b4c35acca54edced84032f70c8ea88a1338d361b0fec7861c2eb26c244b99de45e60f9c361b0e2a7331b40cdf3df7bb2d4c"

cypher_len = len(cyphertext)
iv = bytes.fromhex("0000" + cyphertext[:28])
encrypted = bytes.fromhex(cyphertext[28:(cypher_len-32)])
signature = bytes.fromhex(cyphertext[(cypher_len-32):])

for i in range(256):
    for j in range(256):
        iv = bytes.fromhex(hex(i)[2:].zfill(2) + hex(j)[2:].zfill(2) + cyphertext[:28])
        KEY = bytes.fromhex("".join([hex(a ^ b)[2:].zfill(2) for a, b in zip(iv, signature)]))
        cipher = AES.new(KEY[::-1], AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(encrypted)
        if b'PWNME' in decrypted:
           print(str(decrypted))
  
  
