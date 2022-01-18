from test import *


lista = []
contador = 0
registradores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

if __name__ == '__main__':
    x = input("Insira o nome do arquivo: ")
    texto = open(f'D:/Documentos/Desenvolvimento_Software/Python/PyTreino/{x}.txt', "r")
    with open(f"D:/Documentos/Desenvolvimento_Software/Python/PyTreino/{x}.txt") as texto:
        for valor in texto:
            codigo = valor.split("\n")
            lista.append(codigo[0])


f(lista, contador)
print("======== comandos ========")
print(*lista, sep='\n')
print("==========================")
for valor in lista:
    operar(valor, registradores)
    print("======= registradores =======")
    print(*registradores, sep='\n')
    print("=============================")


