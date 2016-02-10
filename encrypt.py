#!/usr/bin/env python
import os
import sys
import argparse
import rsa_lib as rsa

BLOCK_SIZE = 1


parser = argparse.ArgumentParser(description='Redes II: cifra arquivo com RSA')
parser.add_argument('input', metavar='arquivo_entrada', type=str,
                    help='nome de um arquivo existente')
parser.add_argument('output', metavar='arquivo_saida', type=str,
                    help='nome para o arquivo cifrado')
parser.add_argument('n', type=int, help='número inteiro n | 255 < n < 65536')
parser.add_argument('e', metavar='chave_publica', type=int,
                    help='número primo e (chave pública)')
args = parser.parse_args()


if not os.path.exists(args.input):
    print('Arquivo não encontrado')
    exit(1)

if not (255 < args.n < 65536):
    print('Erro: `n` precisa estar entre 255 e 65536')
    exit(1)

if not (args.e < args.n):
    print('Erro: `e` precisa ser menor que `n`')
    exit(1)

with open(args.input, 'rb') as arq_origem:
    with open(args.output, 'wb') as arq_dest:
        while True:
            buff = arq_origem.read(BLOCK_SIZE)
            if not buff:
                break  # eof

            m = int.from_bytes(buff, sys.byteorder)
            d = rsa.binExponentiate(m, args.e, args.n)

            arq_dest.write(d.to_bytes(2, sys.byteorder))
