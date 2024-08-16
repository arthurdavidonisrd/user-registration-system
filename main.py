from module_1.helpers import *
from arquivo.arqhelper import *
from time import sleep

archive = 'project.txt'

if not archiveExists(archive):
    createArchive(archive)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])

    if resposta == 1:
        #listagem do arquivo 
        readArchive(archive)

    elif resposta == 2:
        #cadastrar nova pessoa
        header("NOVO CADASTRO:")
        name = str(input("Digite o nome:"))
        age = readIntOption("Digite sua idade")

        insertUser(archive, name, age)

    elif resposta == 3:
        header("Saindo do sistema...")
        break
    else:
        header("Invalid Option")
        exit()
    sleep(1)
        
