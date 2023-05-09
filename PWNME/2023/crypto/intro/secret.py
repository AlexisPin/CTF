import random
from itertools import cycle

# Load the encrypted message and known part of the plaintext
encrypted = [int(x) for x in open('./message-encrypted.txt', 'r').read().split(',')]
known_plaintext = open("./intercepted-original-message.txt", "r").read().strip()

# split the known plaintext into chunks of 16 bytes
known_plaintext_chunks = [known_plaintext[i:i+16] for i in range(0, len(known_plaintext), 16)]
# split the encrypted message into chunks of 16 bytes
encrypted_chunks = [encrypted[i:i+16] for i in range(0, len(encrypted), 16)]

# xor the known plaintext with the encrypted message to get the secret key
secret_key = ['*' for i in range(16)]
for i in range(len(encrypted_chunks)):
    for j in range(len(encrypted_chunks[i])):
        if known_plaintext_chunks[i][j] != '*':
        	secret_key[j] = chr(int(encrypted_chunks[i][j]) ^ ord(known_plaintext_chunks[i][j]))

with open('./secret-key.txt', 'w') as f:
    f.write(''.join(secret_key))
