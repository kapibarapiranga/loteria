# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 01:37:42 2023

@author: vicospacorum
"""
import csv

# Inicio das Atividades
print("Bem-Vind ao Programa LoTo 2000")
input("Pressione qualquer tecla para continuar")

# Ler o arquivo
with open('teste/so_sorteio.csv', newline='') as arquivo:
    sorteio = csv.reader(arquivo, delimiter=',', quotechar='|')
    for row in sorteio:
        #print(', '.join(row))
        print(row)
        #for item in row:
        #    print(item)


# Fim do Programa
print("Obrigd")