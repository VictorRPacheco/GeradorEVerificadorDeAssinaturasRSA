# Aqui usaremos a fórmula C = Cd mod (n)
# M -> é o valor em Codificado
# d -> é o valor de uma das chaves privadas
# n -> é o valor de n
# Após isso, você terá sua mensagem codificada em RSA

def DecodificarAscii(num):
    numero = num
    for letra in numero:

        asc = {letra: chr(letra)}

        print(asc)
