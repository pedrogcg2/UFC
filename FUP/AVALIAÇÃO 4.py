#Alunos:
#Pedro Gabriel Castelo Garcêz - 535926
#João Pedro Oliveira Lisboa - 536523




import matplotlib.pyplot as plt
import random as rnd


def gera_tabuleiro():           #cria uma matriz de 0's(celulas morta) e 1's (celulas vivas) randomicamente.
    tabuleiro = []             
    for _ in range(20):
        tabuleiro.append([rnd.randint(0,1) for _ in range(20)])
    return tabuleiro



def pega_vizinhos(linha, coluna, matriz):  #pega um elemento de uma matriz e retorna todos os seus vizinhos
    vizinhos = []
    
    for i in range(-1, 2):
        if linha + i == -1 or linha + i > len(matriz) - 1:
            continue
        
        for j in range(-1, 2):
            if coluna + j == -1 or coluna + j > len(matriz) - 1:
                continue
            if coluna + j == coluna and linha + i == linha:
                continue
            vizinhos.append(matriz[linha + i][coluna + j])
    
    return vizinhos


def geracoes(tabuleiro):      #gera a proxima geraçao de celulas
    proxima_geracao = []
    for i in range(len(tabuleiro)):
        linha = []
        for j in range(len(tabuleiro)):
            vizinhos = pega_vizinhos(i, j, tabuleiro)
            celula = tabuleiro[i][j]
            if celula == 0:
                linha.append(celula_morta(vizinhos))
            else:
                linha.append(celula_viva(vizinhos))
        
        proxima_geracao.append(linha) 
            
    return proxima_geracao


def celula_morta(vizinhos):     #estabelece se uma celula nasce ou continua morta.
    if vizinhos.count(1) == 3:
        return 1
    else:
        return 0

def celula_viva(vizinhos):  #estabelece se uma celula morre ou continua viva.
    if vizinhos.count(1) > 3 or vizinhos.count(1) < 2:
        return 0
    else:
        return 1




def quadrado(i, j, preenchido=False):
    if preenchido:
        plt.fill([i, i, i+1, i+1], [j, j+1, j+1, j], 'b')
    else:
        plt.fill([i, i, i+1, i+1], [j, j+1, j+1, j], 'b', fill=None)
        
    
def main():
    tabuleiro = gera_tabuleiro()
    for k in range(10):
        
        for i in range(len(tabuleiro)):
            
            for j in range(len(tabuleiro)):
                if tabuleiro[i][j] == 0: # celula morta é pintada de azul
                    quadrado(i, j, True)
                else:
                    quadrado(i, j)

        plt.savefig(f"fig{k}.png") # Salva a figura atual em arquivo
        plt.clf() # Limpa a figura
        
        tabuleiro = geracoes(tabuleiro)
        
# Cria uma lista com os nomes dos arquivos gerados
    arquivos = [f"fig{k}.png" for k in range(10)]

    plt.axis('off')

    for a in arquivos:
        im=plt.imread(a)
        plt.imshow(im)
        plt.pause(1)
        plt.draw()
        
                                                 
        
    

if __name__ == "__main__":
    main()
