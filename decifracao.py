def decifrarMensagem(msgCifrada, PrivateKeyN, PrivateKeyD):
    mensagemDecifrada = []
    for pos in range(len(msgCifrada)):
        letraDecifrada = ((msgCifrada[pos] ** PrivateKeyD)% PrivateKeyN)
        print(f"Caracteres da frase decifrada: {letraDecifrada}")
        mensagemDecifrada.append(chr(letraDecifrada))

    return(''.join(mensagemDecifrada))