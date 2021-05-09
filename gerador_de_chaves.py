def gerandoChaves(p, q, d, e):
    primo_um = p
    primo_dois = q
    n = primo_um * primo_dois

    # Função Totiente

    phi_primoUm = primo_um - 1
    phi_primoDois = primo_dois - 1
    phi_n = phi_primoUm * phi_primoDois


    e = e

    d = d

    #print(f'Chave Pública -> {n}, {e}'
    #     f'\nChave Privada -> {primo_um}, {primo_dois}, {d}')

    return([[n, e], [primo_um, primo_dois]])