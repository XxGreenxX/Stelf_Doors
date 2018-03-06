#!/usr/bin/python2.7

import socket
import requests
import sys

if len(sys.argv) < 2 or 1 == '-h':
    print "[?]Passe o argumento (-h) para obter a ajuda."





def connect():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.15)


def Main_doors():
    ports = [18, 20, 21, 22, 23, 25, 38, 43, 57, 80, 107, 110, 115, 119, 135, 137, 138, 139, 143, 443, 1080, 1433, 1434, 2082, 2083, 3306, 8080]

    for port in ports:
        connect()
        code = client.connect_ex((sys.argv[2], port))

        if code == 0:
            print "[+] "+str(port) + " --> code: 0 = Porta aberta\n"
            scan1 = open ("Scan_Portas_Principais.txt", 'a')
            scan1.write("Portas abertas: " + str(port) + '\n')

        elif code == 11:
            print "[-] "+str(port) + " --> code: 11 = Recurso temporariamente indisponivel\n"
        elif code == 111:
            print "[-] "+str(port) + " --> code: 111 = Conexao recusada\n"
        elif code == 4:
            print "[-] "+str(port) + " --> code: 4 = Chamada do sistema interrompido\n"
        elif code == 13:
            print "[-] "+str(port) + " --> code: 13 = Permissao negada\n"
        elif code == 110:
            print "[-] "+str(port) + " --> code: 110 = tempo limite de conexao\n"
        elif code == 112:
            print "[-] "+str(port) + " --> code: 112 = Host esta desativado\n"
        elif code == 101:
            print "[-] "+str(port) + " --> code: 101 = A rede esta inacessivel\n"
        elif code == 93:
            print "[-] "+str(port) + " --> code: 93 = Protocolo nao suportado\n"
        elif code == 92:
            print "[-] "+str(port) + " --> code: 92 = Protocolo nao disponivel\n"
        elif code == 91:
            print "[-] "+str(port) + " --> code: 91 = Tipo de protocolo errado para soquete\n"
        else:
            pass

        if port == ports[26]:
            client.close()
            exit(0)


def All_the_doors():
    ports2 = range(1, 65535)

    for port2 in ports2:
        connect()

        code = client.connect_ex((sys.argv[2], port2))

        if port2 == 65535:
            exit(0)

        if code == 0:
            print "[+] "+str(port2) + " --> code: 0 = Porta aberta\n"
        elif code == 11:
            print "[-] "+str(port2) + " --> code: 11 = Recurso temporariamente indisponivel\n"
        elif code == 111:
            print "[-] "+str(port2) + " --> code: 111 = Conexao recusada\n"
        elif code == 4:
            print "[-] "+str(port2) + " --> code: 4 = Chamada do sistema interrompido\n"
        elif code == 13:
            print "[-] "+str(port2) + " --> code: 13 = Permissao negada\n"
        elif code == 110:
            print "[-] "+str(port2) + " --> code: 110 = tempo limite de conexao\n"
        elif code == 112:
            print "[-] "+str(port2) + " --> code: 112 = Host esta desativado\n"
        elif code == 101:
            print "[-] "+str(port2) + " --> code: 101 = A rede esta inacessivel\n"
        elif code == 93:
            print "[-] "+str(port2) + " --> code: 93 = Protocolo nao suportado\n"
        elif code == 92:
            print "[-] "+str(port2) + " --> code: 92 = Protocolo nao disponivel\n"
        elif code == 91:
            print "[-] "+str(port2) + " --> code: 91 = Tipo de protocolo errado para soquete\n"


def Choice_of_doors():
    ports3 = []
    count = 0

    while count < 20:
        ports3.append(int(raw_input("Digite a porta: ")))

        count += 1

    for port3 in ports3:
        connect()

        code = client.connect_ex((sys.argv[2], port3))

        if code == 0:
            print "[+] "+str(port3) + " --> code: 0 = Porta aberta\n"
        elif code == 11:
            print "[-] "+str(port3) + " --> code: 11 = Recurso temporariamente indisponivel\n"
        elif code == 111:
            print "[-] "+str(port3) + " --> code: 111 = Conexao recusada\n"
        elif code == 4:
            print "[-] "+str(port3) + " --> code: 4 = Chamada do sistema interrompido\n"
        elif code == 13:
            print "[-] "+str(port3) + " --> code: 13 = Permissao negada\n"
        elif code == 110:
            print "[-] "+str(port3) + " --> code: 110 = tempo limite de conexao\n"
        elif code == 112:
            print "[-] "+str(port3) + " --> code: 112 = Host esta desativado\n"
        elif code == 101:
            print "[-] "+str(port3) + " --> code: 101 = A rede esta inacessivel\n"
        elif code == 93:
            print "[-] "+str(port3) + " --> code: 93 = Protocolo nao suportado\n"
        elif code == 92:
            print "[-] "+str(port3) + " --> code: 92 = Protocolo nao disponivel\n"
        elif code == 91:
            print "[-] "+str(port3) + " --> code: 91 = Tipo de protocolo errado para soquete\n"
        pass

def Brute_force_dyrectory():
    arquivo = open('common.txt')

    linhas = arquivo.readlines()

    for linha in linhas:
        requisicao = requests.get(sys.argv[2] + linha)
        codigo = requisicao.status_code

        print sys.argv[2] + linha + 'Codigo: '+str(codigo), '\n'

def Help():
    print "\n[?]--> Help <--[?]\n\n-m -> Para escanear portas principais\n-a -> Para escanear todas as portas posiveis de 1 a 65535\n-c -> Para escanear apenas 20 portas de sua preferencia\n-Bd -> Para buscar por diretorios\n"


if sys.argv[1] == '-m':
    Main_doors()

elif sys.argv[1] == '-a':
    All_the_doors()

elif sys.argv[1] == '-c':
    Choice_of_doors()

elif sys.argv[1] == '-Bd':
    Brute_force_dyrectory()

elif sys.argv[1] == '-h':
    Help()




