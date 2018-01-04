#/usr/bin/python2.7

import socket



def Menu_method():
    print "Digite = (1) Para fazer um scan apenas de portas principais"
    print "Digite = (2) Para fazer um scan completo de todas as portas"
    print "Digite = (3) Para escanear 20 portas personalizadas"
    print "Digite = (4) Para Sair\n"
    global method

    method = raw_input("Metodo: ")

    if method == str(1):
        Main_doors()
    elif method == str(2):
        All_the_doors()
    elif method == str(3):
        Choice_of_doors()
    elif method == 4:
        exit(0)
    else:
        pass

    if method < str(1) or method > str(4):
        print "Metodo incorreto !!!\n"
        Menu_method()


def Back_home():
    back = input("\nVoltar ao menu principal S/n > ")
    if back != "s" or back == " ":
        Menu_method()
    elif back == "n":
        exit(0)

def Host():
    global host
    host = raw_input("Host: ")


def connect():
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.15)


def Main_doors():
    Host()
    ports = [18, 20, 21, 22, 23, 25, 38, 43, 57, 80, 107, 110, 115, 119, 135, 137, 138, 139, 143, 443, 1080, 1433, 1434, 2082, 2083, 3306, 8080]

    for port in ports:
        connect()
        code = client.connect_ex((host, port))

        if code == 0:
            print str(port) + " --> code: 0 = Porta aberta\n"
            scan1 = open ("Scan_Portas_Principais.txt", 'a')
            scan1.write("Portas abertas: " + str(port) + '\n')

        elif code == 11:
            print str(port) + " --> code: 11 = Recurso temporariamente indisponivel\n"
        elif code == 111:
            print str(port) + " --> code: 111 = Conexao recusada\n"
        elif code == 4:
            print str(port) + " --> code: 4 = Chamada do sistema interrompido\n"
        elif code == 13:
            print str(port) + " --> code: 13 = Permissao negada\n"
        elif code == 110:
            print str(port) + " --> code: 110 = tempo limite de conexao\n"
        elif code == 112:
            print str(port) + " --> code: 112 = Host esta desativado\n"
        elif code == 101:
            print str(port) + " --> code: 101 = A rede esta inacessivel\n"
        elif code == 93:
            print str(port) + " --> code: 93 = Protocolo nao suportado\n"
        elif code == 92:
            print str(port) + " --> code: 92 = Protocolo nao disponivel\n"
        elif code == 91:
            print str(port) + " --> code: 91 = Tipo de protocolo errado para soquete\n"

        else:
            Menu_method()

        if port == ports[26]:
            client.close()
            Back_home()


def All_the_doors():
    Host()
    ports2 = range(1, 65535)

    for port2 in ports2:
        connect()

        code = client.connect_ex((host, port2))

        if port2 == 65535:
            Menu_method()

        if code == 0:
            print str(port2) + " --> code: 0 = Porta aberta\n"
        elif code == 11:
            print str(port2) + " --> code: 11 = Recurso temporariamente indisponivel\n"
        elif code == 111:
            print str(port2) + " --> code: 111 = Conexao recusada\n"
        elif code == 4:
            print str(port2) + " --> code: 4 = Chamada do sistema interrompido\n"
        elif code == 13:
            print str(port2) + " --> code: 13 = Permissao negada\n"
        elif code == 110:
            print str(port2) + " --> code: 110 = tempo limite de conexao\n"
        elif code == 112:
            print str(port2) + " --> code: 112 = Host esta desativado\n"
        elif code == 101:
            print str(port2) + " --> code: 101 = A rede esta inacessivel\n"
        elif code == 93:
            print str(port2) + " --> code: 93 = Protocolo nao suportado\n"
        elif code == 92:
            print str(port2) + " --> code: 92 = Protocolo nao disponivel\n"
        elif code == 91:
            print str(port2) + " --> code: 91 = Tipo de protocolo errado para soquete\n"


def Choice_of_doors():
    Host()
    ports3 = []
    count = 0

    while count < 20:
        ports3.append(int(raw_input("Digite a porta: ")))

        count += 1

    for port3 in ports3:
        connect()

        code = client.connect_ex((host, port3))

        if code == 0:
            print str(port3) + " --> code: 0 = Porta aberta\n"
        elif code == 11:
            print str(port3) + " --> code: 11 = Recurso temporariamente indisponivel\n"
        elif code == 111:
            print str(port3) + " --> code: 111 = Conexao recusada\n"
        elif code == 4:
            print str(port3) + " --> code: 4 = Chamada do sistema interrompido\n"
        elif code == 13:
            print str(port3) + " --> code: 13 = Permissao negada\n"
        elif code == 110:
            print str(port3) + " --> code: 110 = tempo limite de conexao\n"
        elif code == 112:
            print str(port3) + " --> code: 112 = Host esta desativado\n"
        elif code == 101:
            print str(port3) + " --> code: 101 = A rede esta inacessivel\n"
        elif code == 93:
            print str(port3) + " --> code: 93 = Protocolo nao suportado\n"
        elif code == 92:
            print str(port3) + " --> code: 92 = Protocolo nao disponivel\n"
        elif code == 91:
            print str(port3) + " --> code: 91 = Tipo de protocolo errado para soquete\n"
        Menu_method()


Menu_method()


