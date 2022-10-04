import os

class bcolors:
    Reset = '\x1b[0m'
    Bright = '\x1b[1m'
    Dim = '\x1b[2m'
    Underscore = '\x1b[4m'
    Blink = '\x1b[5m'
    Reverse = '\x1b[7m'
    Hidden = '\x1b[8m'
    FgBlack = '\x1b[30m'
    FgRed = '\x1b[31m'
    FgGreen = '\x1b[32m'
    FgYellow = '\x1b[33m'
    FgBlue = '\x1b[34m'
    FgMagenta = '\x1b[35m'
    FgCyan = '\x1b[36m'
    FgWhite = '\x1b[37m'
    BgBlack = '\x1b[40m'
    BgRed = '\x1b[41m'
    BgGreen = '\x1b[42m'
    BgYellow = '\x1b[43m'
    BgBlue = '\x1b[44m'
    BgMagenta = '\x1b[45m'
    BgCyan = '\x1b[46m'
    BgWhite = '\x1b[47m'


def menu():
    print(f'{bcolors.FgGreen}------- APOSTAS -------{bcolors.Reset}')
    print(f'{bcolors.FgGreen}1. {bcolors.FgMagenta}Cadastrar aposta{bcolors.Reset}')
    print(f'{bcolors.FgGreen}2. {bcolors.FgMagenta}Visualizar apostas{bcolors.Reset}')
    print(f'{bcolors.FgGreen}3. {bcolors.FgMagenta}Excluir apostas{bcolors.Reset}')
    print(f'{bcolors.FgGreen}4. {bcolors.FgMagenta}Sair{bcolors.Reset}')


def cadastrar_aposta():
    times = []
    time = input(f'{bcolors.BgBlue}Time:{bcolors.Reset}')
      
    while ('.') in time:
        times.append(time)
        time = input(f'{bcolors.BgBlue}Time:{bcolors.Reset}')
    else:
        print('')
        lucro = input(f'{bcolors.BgYellow}Lucro: R${bcolors.Reset} ')
    

def visualizar_apostas():
    apostas = []
    apostas.append(cadastrar_aposta)
    print(apostas)
    

def excluir_apostas():
    print('Excuir apostas...')

def init():
    option = 0
    while option is not '4':
        menu()
        option = input('-> ')
        os.system('clear')
        match option:
            case '1':
                cadastrar_aposta()
            case '2':
                visualizar_apostas()
            case '3':
                excluir_apostas()
            case '4':
                return 0
            case _:
                print('Opcao nao encontrada')

init()