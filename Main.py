import pickle
from gerador_de_chaves import gerandoChaves
from calculo_hash import calcular_hash_SHA3
from cifracao import cifrarMensagem
from decifracao import decifrarMensagem
from datetime import datetime

def RSA_Creator(msg, fileNameCreate):
    print("************ Executando o código de criação da mensagem cifrada ************")
    # generate a key-pair
    [PublicKey, PrivateKey] = gerandoChaves()

    print(f"Public key:  (n={hex(PublicKey[0])}, e={hex(PublicKey[1])})")
    print(f"Private key: (n={hex(PrivateKey[0])}, d={hex(PrivateKey[1])}")


    # Calculate the hashs in SHA-3
    hash = calcular_hash_SHA3(msg)
    print("Hash: ", hex(hash))

    # Cifra a mensagem
    mensagemCifrada = cifrarMensagem(msg, PublicKey[0], PublicKey[1])
    print(f"mensagem cifrada: {mensagemCifrada}")

    # Save the result in a pkl file
    Data = {
        "MensagemCifrada" : mensagemCifrada,
        "PrivateKey": PrivateKey,
        "Hash": hash,
    }
    a_file = open(fileNameCreate, "wb")
    pickle.dump(Data, a_file)
    a_file.close()
    print(f"Todos os dados salvos no arquivo {fileNameCreate}")

def RSA_Reader(fileNameRead):
    print(f"************ Executando o código de decifração da mensagem ************")
    # Parsing of the signed document
    print(f"{datetime.now()} STATUS: Lendo o arquivo {fileNameRead}")
    a_file = open(fileNameRead, "rb")
    fileRead = pickle.load(a_file)
    a_file.close()
    mensagemParaDecifrar = fileRead["MensagemCifrada"]
    PrivateKeyParaDecifrar = fileRead["PrivateKey"]
    hashMsgCifrada = fileRead["Hash"]
    print(f"{datetime.now()} STATUS: Arquivo lido com sucesso {fileNameRead}")

    # Decrypt the sign
    mensagemDecifrada = decifrarMensagem(mensagemParaDecifrar, PrivateKeyParaDecifrar[0], PrivateKeyParaDecifrar[1])
    print(f"mensagemDecifrada: {mensagemDecifrada}")

    # Calculate and compare the hash of the file
    hashMsgDecifrada = calcular_hash_SHA3(mensagemDecifrada)
    if(hashMsgDecifrada == hashMsgCifrada):
        print(f"Os hashs são iguais")
    else:
        print(f"Os hashs são diferentes")


# Choice the functions you want to run
msg = "Mensagem" # insert your precious message in here
fileNameCreate = "data.pkl"
RSA_Creator(msg, fileNameCreate)

fileNameRead = "data.pkl"
RSA_Reader(fileNameRead)
