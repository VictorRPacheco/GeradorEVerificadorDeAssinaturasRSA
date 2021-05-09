def assinar_mensagem(hash, PrivateKeyN, PrivateKeyD):
    return (pow(hash, PrivateKeyN, PrivateKeyD))
