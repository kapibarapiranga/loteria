# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 01:37:42 2023
Updated on Wed Dec 31 11:06 2025

@author: vicospacorum
@author: kapibarapiranga
"""

numSorteados = []
jogosFeitos = []
resultadoFinal = []

def sorteio():
    temp = []
    with open('Jogos/2025-numSorteados.csv','r') as numSorteados_csv:
        for linha in numSorteados_csv:
            temp.append(linha.split())
    
    for i in range(6):
        numSorteados.append(temp[0][i])
    
def jogosRealizados():
    with open('Jogos/2025-jogosFeitos.csv','r') as jogosFeitos_csv:
        for linha in jogosFeitos_csv:
            jogosFeitos.append(linha.split())
    
def resultado(numJogos):
    for i in range(numJogos):
        acertos = 0
        for j in range(6):
            for k in range(1, len(jogosFeitos[i])):
                if (numSorteados[j] == jogosFeitos[i][k]):
                    acertos +=1
                    break
        
        if(acertos == 6):
            resultadoFinal.append(jogosFeitos[i][0] + " SENA!!!!")
        elif(acertos == 5):
            resultadoFinal.append(jogosFeitos[i][0] + " Quina")
        elif(acertos == 4):
            resultadoFinal.append(jogosFeitos[i][0] + " Quadra")
        else:
            resultadoFinal.append(jogosFeitos[i][0] + " Água!")
    
    print(resultadoFinal)
    
# Inicio das Atividades
print("Bem-Vind ao Programa LoTo 2000")
#input("Pressione qualquer tecla para continuar\n")

# Processa os números sorteados
sorteio()

# Processa os jogos feitos
numJogos = int(input("Digite o número de Jogos: "))
jogosRealizados()

# Imprime na tela o resultado dos jogos
resultado(numJogos)

# Fim do Programa
print("\n\n\nObrigd")