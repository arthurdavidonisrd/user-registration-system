def readIntOption(msg):
    while True:
        try:
            number = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO: Digite um número inteiro válido")
            continue
        except (KeyboardInterrupt):
            print("Operação cancelada pelo usúario")
            return 0
        else:
            return number

def linha(tamanho = 42):
    return '-' * tamanho

def header(msg):
    print(linha())
    print(msg.center(42))
    print(linha())
    

def menu(listOptions):
    header("Main Menu")
    c = 1
    for item in listOptions:
        print(f"{c} -- {item}")
        c += 1
    print(linha())
    optionChoice = readIntOption("Digite sua opção:")
    return optionChoice