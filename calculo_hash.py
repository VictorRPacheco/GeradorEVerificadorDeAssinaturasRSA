import hashlib

h = hashlib.sha384()
h.update("uma frase qualquer")
print(h.hexdigest())
