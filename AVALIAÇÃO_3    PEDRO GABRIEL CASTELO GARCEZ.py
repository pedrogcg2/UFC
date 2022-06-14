import itertools as it
import random
import numpy as np


def quadrados_latinos(n, matriz=None):
    quadrados = gera_quadrados(n)
    quadrados_corretos = []
    for quadrado in quadrados:
        
        if not colunas_repetidas(quadrado):
            quadrados_corretos.append(quadrado)
            imprimirMatriz(quadrado)
    
    print(f'numero de quadrados latinos de ordem {n} é {len(quadrados_corretos)}\n')
    
    if matriz != None and completa_quadrados(matriz) != None:
        matriz = completa_quadrados(matriz)
        print('Matriz completa:', imprimirMatriz(matriz))

    return quadrados_corretos



#GERA TODAS AS MATRIZES POSSIVEIS
def gera_quadrados(num):
    permutacoes = list(it.permutations(x for x in range(1,num+1)))
    quadrados = list(it.permutations(permutacoes,num))
    return quadrados



#CHECA LINHAS REPETIDAS NAS COLUNAS
def colunas_repetidas(quadrado):
    for i in range(len(quadrado)):
        coluna = []
        for j in range(len(quadrado)):
            coluna.append(quadrado[j][i])
        
        if len(set(coluna)) != len(coluna):
            return True
        
    return False



#DESAFIO ÀS VEZES EXCEDE O NÚMERO MAXIMO DE RECURSÕES
def completa_quadrados(quadrado):
    
    print('Matriz antiga: ')
    imprimirMatriz(quadrado)
    
    ordem = len(quadrado)
    
    if colunas_repetidas:
        print('esse quadrado não é latino')
        return None

    for i in range(ordem):
        
        quadrado[i] = list(quadrado[i])
        quadrado[i] = muda_linha(quadrado[i],quadrado, ordem)
            
    return quadrado

#CRIEI ESTA FUNÇÃO PARA PODER TER ACESSO A RECURSÃO
def muda_linha(linha,quadrado,ordem):
    for x in linha:
        coluna = []
        linha_antiga = linha
        if x == 0:
            for j in range(ordem):   
                coluna.append(quadrado[j][linha.index(x)])
                
            diferença = list(set(range(1, ordem + 1)).difference(set(coluna), set(linha)))
            if len(diferença) == 0:
                linha = linha_antiga
                return muda_linha(linha,quadrado,ordem)
            else:
                escolha = random.choice(diferença)
                linha[linha.index(0)] = escolha
            
    return linha


def imprimirMatriz(M):
    nLin = len(M)
    nCol = len(M[0])
    for i in range(nLin):
        for j in range(nCol):
            print("{:3}".format(M[i][j]), end=" ")
        print("")
    print("")

ordem = random.randint(1,4)
matriz = [[random.randint(0,ordem) for _ in range(ordem)]for i in range(ordem)]
quadrados_latinos(ordem, matriz)
