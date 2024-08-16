from module_1.helpers import *

def archiveExists(nameArchive):
    try:
        archive = open(nameArchive, 'rt')
        archive.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def createArchive(nameArchive):
    try:
        archive = open(nameArchive, 'wt+')
        archive.close()
    except:
        print(f'Houve um erro na criação do arquivo {nameArchive}')
    else:
        print(f'Arquivo {nameArchive} criado com sucesso!')

def readArchive(archiveName):
    try:
        archive = open(archiveName, 'rt')
    except:
        print(f'Houve um erro ao abrir o arquivo {archiveName}')
        return
    else:
        header('PESSOAS CADASTRADAS:')
        print(archive.read())

    
def insertUser(archiveName, nameUser = 'unknow', ageUser = 0):
    try:
        archive = open(archiveName, 'at')
    except:
        print(f'Houve um erro ao abrir o arquivo {archiveName}')
        return
    else:
        try:
            archive.write(f'{nameUser},{ageUser}\n')
        except:
            print('Houve um erro ao gravar os dados do usuário no arquivo')
        else:
            print(f"Usuário {nameUser} cadastrado com sucesso")
            archive.close()
            
