# Implementação em Python do algoritmo abaixo:
# https://dl.dropboxusercontent.com/u/12141084/Aulas/RedesIISI/Trabalhos/trabalho2.pdf (página 2)


def binExponentiate(b, e, n):
    '''
    Argumentos:
        - b: base da exponenciação.
        - e: expoente.
        - n: módulo (n > 1).
    Retorna: b^e (mod n).
    '''

    res = b
    y = 1

    # Caso base
    if e == 0:
        return 1

    while (e > 1):
        if (e & 1):
            # Caso expoente impar
            y = (y * res) % n
            e = e - 1

        res = (res ** 2) % n
        e = int(e / 2)

    return (res * y) % n
