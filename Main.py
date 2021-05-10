import random
import pickle
from gerador_de_chaves import gerandoChaves
from calculo_hash import calcular_hash_SHA3
from assinar import assinar_mensagem
from cifracao import cifrarMensagem
from decifracao import decifrarMensagem

def RSA_Creator(msg, fileNameCreate):
    # generate a 1024-bit RSA key-pair
    [PublicKey, PrivateKey] = gerandoChaves(random.randint(0000, 9999), random.randint(0000, 9999), random.randint(0000, 9999), random.randint(0000, 9999))

    print(f"Public key:  (n={hex(PublicKey[0])}, e={hex(PublicKey[1])})")
    print(f"Private key: (n={hex(PrivateKey[0])}, d={hex(PrivateKey[1])})")


    # Calculate the hashs in SHA-3
    hash = calcular_hash_SHA3(msg)
    print("Hash: ", hex(hash))

    # Sign the message
    signature = assinar_mensagem(hash, PrivateKey[1], PrivateKey[0])
    print("Signature: ", hex(signature))

    # Cifra a mensagem
    mensagemCifrada = cifrarMensagem(msg, PublicKey[0], PublicKey[1])
    print(f"mensagem cifrada: {mensagemCifrada}")

    # 3) Save the result
    Data = {
        "OriginalMessage": msg,
        "MensagemCifrada" : mensagemCifrada,
        "PublicKey": PublicKey,
        "PrivateKey": PrivateKey,
        "Hash": hash,
        "Signature": signature,
    }
    a_file = open(fileNameCreate, "wb")
    pickle.dump(Data, a_file)
    a_file.close()
    print(f"Todos os dados salvos no arquivo {fileNameCreate}")

def RSA_Reader(fileNameRead):
    # Verification in 3 steps:
    # 1) Parsing of the signed document
    print(f"Lendo o arquivo {fileNameRead}")
    a_file = open(fileNameRead, "rb")
    fileRead = pickle.load(a_file)
    a_file.close()
    print(fileRead["OriginalMessage"])

    # 2) Decrypt the sign
    mensagemParaDecifrar = fileRead["MensagemCifrada"]
    PublicKeyParaDecifrar = fileRead["PublicKey"]
    # mensagemDecifrada = decifrarMensagem(mensagemParaDecifrar, PublicKeyParaDecifrar[0], PublicKeyParaDecifrar[1])
    # print(f"mensagemDecifrada: {mensagemDecifrada}")

    # 3) Calculate and compare the hash of the file


# Passos para executar
msg = "This is a really important message that really needs to be secured Teste 123"
fileNameCreate = "data.pkl"
RSA_Creator(msg, fileNameCreate)

fileNameRead = "data.pkl"
RSA_Reader(fileNameRead)
