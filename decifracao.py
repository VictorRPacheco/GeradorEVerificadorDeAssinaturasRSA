def decifrarMensagem(msgCifrada, PublicKeyN, PublicKeyE):
    mensagemDecifrada = []

    for pos in range(len(msgCifrada)):
        letraDecifrada = ((msgCifrada[pos] ** PublicKeyE)% PublicKeyN)
        print(f"LetraCecifrada: {letraDecifrada}")
        print(f"LetraDecifrada: {chr(letraDecifrada)}")
        mensagemDecifrada.append(chr(letraDecifrada))

    return(mensagemDecifrada)