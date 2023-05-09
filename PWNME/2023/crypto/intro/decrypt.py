import random
from itertools import cycle

# Load the encrypted message and key
encrypted = [int(x) for x in open('./message-encrypted.txt', 'r').read().split(',')]
key = open("./secret-key.txt", "r").read().strip()

# Decrypt the message
decrypted = ''.join([chr(int(a) ^ ord(b)) for a, b in zip(encrypted, cycle(key))])

# Print the decrypted message
print(decrypted)
