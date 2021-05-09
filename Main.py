import random
from gerador_de_chaves import gerandoChaves
from calculo_hash import calcular_hash_SHA3
from assinar import assinar_mensagem

# generate a 1024-bit RSA key-pair
[PublicKey, PrivateKey] = gerandoChaves(random.randint(0000, 9999), random.randint(0000, 9999), random.randint(0000, 9999), random.randint(0000, 9999))

print(f"Public key:  (n={hex(PublicKey[0])}, e={hex(PublicKey[1])})")
print(f"Private key: (n={hex(PrivateKey[0])}, d={hex(PrivateKey[1])})")


# RSA sign the message in 3 steps:
# 1) Calculate the hashs in SHA-3
msg = b'This is a really important message that really needs to be secured'
hash = calcular_hash_SHA3(msg)
print("Hash: ", hex(hash))

# 2) Sign the message
signature = assinar_mensagem(hash, PrivateKey[1], PrivateKey[0])
print("Signature: ", hex(signature))

# 3) Format the result


# Verification in 3 steps:
# 1) Parsing of the signed document
# 2) Decrypt the sign
# 3) Calculate and compare the hash of the file

