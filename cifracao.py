def cifrarMensagem(msg, PublicKeyN, PublicKeyE):
    mensagemCifrada = []

    for letra in msg:
        asc = ord(letra)
        print(f"Caracteres da frase original: {asc}")
        mensagemCifrada.append((asc ** PublicKeyE)% PublicKeyN)

    return(mensagemCifrada)