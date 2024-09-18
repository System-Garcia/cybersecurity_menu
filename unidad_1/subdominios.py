'''
programa para encontrar subdominions de un sitio.
explicar que hace este script.
desarrollado por Axel Adrian Garcia Aldama
'''
import requests
from os import path
import argparse
import sys

current_dir = path.dirname(path.abspath(__file__))
path_file = path.join(current_dir, 'subdominios.txt')

parse = argparse.ArgumentParser()
#print(f'{parse}\n\n')
parse.add_argument('-t', '--target', help='indica el dominio de la vistima')
parse = parse.parse_args()
#print(parse)
'''
ESTE SCRIPT BUSCA SUBDOMINIOS DE UN SITIO WEB
'''
def main():
    if parse.target:
        if path.exists(path_file):
            worldlist = open(path_file, 'r')
            worldlist = worldlist.read().split('\n')

            print(f'[+] Buscando subdominios http en {parse.target}')
      
            for subdomain in worldlist:
                url = f'http://{subdomain}.{parse.target}'
                try:
                    requests.get(url, timeout=3)
                except requests.ConnectionError:
                    pass
                else:
                    print(f'[+] Subdominio encontrado: {url}')

            print('\n[+] Busqueda finalizada para http')
            print('\n[+] Busqueda para https')
            for subdomain in worldlist:
                url = f'https://{subdomain}.{parse.target}'
                try:
                    requests.get(url, timeout=3)
                except requests.ConnectionError:
                    pass
                else:
                    print(f'[+] Subdominio encontrado: {url}')
        else: 
            print('[-] No se encontro el archivo subdominios.txt')
            sys.exit(1)
    else:
        print('[-] Debes indicar el dominio de la victima')
        sys.exit(1)


main()


            