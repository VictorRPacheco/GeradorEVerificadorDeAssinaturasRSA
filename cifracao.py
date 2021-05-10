def cifrarMensagem(msg, PublicKeyN, PublicKeyE):
    mensagemCifrada = []

    for letra in msg:
        asc = ord(letra)
        mensagemCifrada.append((asc ** PublicKeyE)% PublicKeyN)

    return(mensagemCifrada)