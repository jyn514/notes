from hashlib import sha512
from string import printable

hashes = {}
phrase = ""
for i in range(1, int(100E30)):
    hash = sha512(bytes(i)).digest()
    if hash in hashes:
        print(i)
    else:
        hashes[i] = hash
