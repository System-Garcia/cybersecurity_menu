import socket
import sys
import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-t', '--target', help='Introduce la direccion ip de la victima')
parse = parse.parse_args()

def banner(ip, port):
    try:
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        print(f'[+] {ip}:{port} {banner}')
    except:
        return
    
def main():
    if parse.target:
        for port in range(1, 100):
            banner(parse.target, port)
    else:
        print('[-] Debes indicar la direccion ip de la victima')
        sys.exit(1)

main()