import socket
import sys
import argparse
from os import path

## Get the current directory
current_dir = path.dirname(path.abspath(__file__))
path_file = path.join(current_dir, 'puertos.txt')

# Create the parser
parse = argparse.ArgumentParser()
parse.add_argument('-t', '--target', help='Introduce la direccion ip o dominio de la victima')
parse = parse.parse_args()


# Function to scan the ports
def scanneer(target):
    if not parse.target:
        print('[-] Debes indicar la direccion ip de la victima')
        sys.exit(1)
    
    if not path.exists(path_file):
        print('[-] No se encontro el archivo puertos.txt')
        sys.exit(1)
    try:
        portlist = open(path_file, 'r')
        porlist = portlist.read().split('\n')
        print(portlist.read())

        if len(porlist) == 0:
            print('[-] No se encontro el archivo puertos.txt')
            sys.exit(1)

        for port in porlist:
            try:
                s = socket.socket()
                s.settimeout(0.5)
                s.connect((target, int(port)))
                s.close()
                print(f'[+] {target}:{port} esta abierto')
            except:
                print(f'[-] {target}:{port} esta cerrado')
    except Exception as e:
        print(f'[-] Ocurrió un error: {e}')
        sys.exit(1)

    
def main():
    if parse.target:
        scanneer(parse.target)
    else:
        print('[-] Debes indicar la direccion ip de la victima')
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n[-] Saliendo...')
        sys.exit(1)
        