from datetime import datetime

def decifrarMensagem(msgCifrada, PrivateKeyN, PrivateKeyD):
    print(f"{datetime.now()} STATUS: Decifrando a mensagem, isso pode demorar um pouco")

    mensagemDecifrada = []
    for pos in range(len(msgCifrada)):
        letraDecifrada = ((msgCifrada[pos] ** PrivateKeyD)% PrivateKeyN)
        mensagemDecifrada.append(chr(letraDecifrada))

    return(''.join(mensagemDecifrada))