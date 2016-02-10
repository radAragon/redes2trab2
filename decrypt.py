#!/usr/bin/env python
import os
import sys
import argparse
import rsa_lib as rsa

BLOCK_SIZE = 2


parser = argparse.ArgumentParser(description='Redes II: decifra arquivo com RSA')
parser.add_argument('input', metavar='arquivo_entrada', type=str,
                    help='nome de um arquivo cifrado existente')
parser.add_argument('output', metavar='arquivo_saida', type=str,
                    help='nome para o arquivo decifrado')
parser.add_argument('n', type=int, help='número inteiro n | 255 < n < 65536')
parser.add_argument('d', metavar='chave_privada', type=int,
                    help='número primo d (chave privada)')
args = parser.parse_args()


if not os.path.exists(args.input):
    print('Arquivo não encontrado')
    exit(1)

if not (255 < args.n < 65536):
    print('Erro: `n` precisa estar entre 255 e 65536')
    exit(1)

if not (args.d < args.n):
    print('Erro: `d` precisa ser menor que `n`')
    exit(1)

with open(args.input, 'rb') as arq_origem:
    with open(args.output, 'wb') as arq_dest:
        error = False
        while True:
            buff = arq_origem.read(BLOCK_SIZE)
            if not buff:
                break  # eof

            if len(buff) < 2:
                print('Erro: número impar de bytes no arquivo_cifrado')
                error = True
                break

            m = int.from_bytes(buff, sys.byteorder)
            e = rsa.binExponentiate(m, args.d, args.n)

            if (e > 255):
                print('Erro: um bloco decifrado não é representável (> 255)')
                error = True
                break

            arq_dest.write(e.to_bytes(1, sys.byteorder))

    if (error):
        os.remove(args.output)
