import os

while True:
    os.system('clear')
    print("Sistema para pruebas de seguridad informatico")
    print("Version 1.0 Desarrollado por Axel Adrian Garcia Aldama")
    print("1.- Busqueda de Subdominios")
    print("2.- Banner Grabbing")
    print("3.- Wad - Web Application Directory")
    print("4.- Escaneo de puertos")
    print("5.- Get IP using nslookup")
    print("6.- Get IP using socket")
    print("7.- Salir")

    opcion = int(input("Selecciona una opcion: "))
    if opcion == 1:
        target = input("Ingresa el dominio de la victima: ")
        os.system(f'python3 subdominios.py -t {target}')
        input("Presiona enter para continuar")
    elif opcion == 2:
        target = input("Ingresa la direccion ip de la victima: ")
        os.system(f'python3 bannergrabing.py -t {target}')
        input("Presiona enter para continuar")
    elif opcion == 3:
        print("Wad is not still implemented")
    elif opcion == 4:
        target = input("Ingresa la direccion ip o dominio de la victima: ")
        os.system(f'python3 port_scanner.py -t {target}')
        input("Presiona enter para continuar")
    elif opcion == 5:
        target = input("Ingresa el dominio de la victima: ")
        os.system(f'python3 get_ip_2.py -t {target}')
        input("Presiona enter para continuar")
    elif opcion == 6:
        target = input("Ingresa la direccion ip de la victima: ")
        os.system(f'python3 get_ip.py -t {target}')
        input("Presiona enter para continuar")
    elif opcion == 7:
        break
    else:
        print("Opcion no valida")
        continue