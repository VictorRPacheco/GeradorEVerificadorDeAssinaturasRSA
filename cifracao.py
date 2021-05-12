from datetime import datetime

def cifrarMensagem(msg, PublicKeyN, PublicKeyE):
    print(f"{datetime.now()} STATUS: Cifrando a mensagem, isso pode demorar um pouco")

    mensagemCifrada = []

    for letra in msg:
        asc = ord(letra)
        mensagemCifrada.append((asc ** PublicKeyE) % PublicKeyN)

    return(mensagemCifrada)