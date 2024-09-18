"""
Primnera forma: nslookup {URL}
Segunda forma: nslookup.io 
Tercera forma mxtoolbox.com
Cuarta forma: script en python

Este script en python busca la ip de una URL dada por el usuario.
"""

import argparse
import socket
import sys

parse = argparse.ArgumentParser()
parse.add_argument('-t', '--target', help='Introduce la URL sin http://')
parse = parse.parse_args()

def get_ip(target):
    try:
        ip = socket.gethostbyname(target)
        print(f'[+] IP de {target}: {ip}')
    except:
        print('[-] No se pudo obtener la ip')
        sys.exit(1)

def main():
    if parse.target:
        get_ip(parse.target)
    else:
        print('[-] Debes indicar la URL')
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[-] Saliendo...')
        sys.exit(1)