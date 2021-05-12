from datetime import datetime
from hashlib import sha512

def calcular_hash_SHA3(msg):
    print(f"{datetime.now()} STATUS: Calculando hash")
    return (int.from_bytes(sha512(str.encode(msg)).digest(), byteorder='big'))