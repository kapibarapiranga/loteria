# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 01:37:42 2023

@author: vicospacorum
"""

numSorteados = []
jogosFeitos = []
resultadoFinal = []

def sorteio():
    temp = []
    with open('teste/numSorteados.csv','r') as arquivo:
        for linha in arquivo:
            temp.append(linha.split())
    
    for i in range(6):
        numSorteados.append(temp[0][i])
    
def jogosRealizados(numJogos):
    with open('teste/jogosFeitos.csv','r') as arquivo:
        for linha in arquivo:
            jogosFeitos.append(linha.split())
    
def resultado(numJogos):
    for i in range(numJogos):
        acertos = 0
        for j in range(6):
            for k in range(1, 7):
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
            resultadoFinal.append(jogosFeitos[i][0])
    
    print(resultadoFinal)
    
# Inicio das Atividades
print("Bem-Vind ao Programa LoTo 2000")
#input("Pressione qualquer tecla para continuar\n")

# Processa os números sorteados
sorteio()

# Processa os jogos feitos
numJogos = int(input("Digite o número de volantes: ")) * 3
jogosRealizados(numJogos)

# Imprime na tela o resultado dos jogos
resultado(numJogos)

# Fim do Programa
print("\n\n\nObrigd")