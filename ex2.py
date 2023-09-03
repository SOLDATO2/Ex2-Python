"""
Como é necessario levar em conta que o usuario pode definir a qnt de casas para jogar
escolhi em focar na utilização de mais lists comprehensions para facilitar o funcionamento dinamico
"""

def mostra_tab(tabuleiro):

    for linha in tabuleiro: # printa cada linha da forca
        print(linha) 

def criar_tab(tamanho):
    
    tabuleiro = []
    for x in range(tamanho):
        tabuleiro.append(['_'] * tamanho) #cria x casas por y linhas
    return tabuleiro



def verificar_vit(tabuleiro, jogador):
    

    #Porção para verificar as verticais e horizontais
    for i in range(len(tabuleiro)):
            # i = linha, j = casa               #j vai possuir o mesmo valor de casas e linhas, pode ser utilizada para definir tamanho no list comprehension
        if all((tabuleiro[i][j] == jogador) for j in range(len(tabuleiro))):#linha
            return True
        elif all(tabuleiro[j][i] == jogador for j in range(len(tabuleiro))):#coluna
            return True

    # porção para verificar diagonais

    if all(tabuleiro[i][i] == jogador for i in range(len(tabuleiro))): #diagonal p
        return True
                        #diagonal secundaria é verificada da direita para esquerda,
                        # é subtraido por -1 para ser em formato de index de listas,
                        # e '- i' para mover a verificação para esquerda
    elif all(tabuleiro[i][len(tabuleiro) - i - 1] == jogador for i in range(len(tabuleiro))): #diagonal s
        return True

    return False

def jogo_da_velha(): #funcao principal que executa o jogo


    tamanho = int(input("Escreva o tamanho do tabuleiro: "))
    tabuleiro = criar_tab(tamanho)
    X_ou_O = "X" # define x como primeira jogada

    while True:
        mostra_tab(tabuleiro)
        escolha = input(f"Você é o '{X_ou_O}', escolha uma posição para inserir o '{X_ou_O}' (exemplo: 1 2): ")
        linha, coluna = [int(x) for x in escolha.split()] # traduz as duas entradas para int e é fornecido para as variaveis linha e coluna

        if linha > tamanho or coluna > tamanho or linha < 1 or coluna < 1: #Verifica se a posição que foi escolhida é valida
            print("Posição invalida.")
            continue # se for invalida, a iteracao atual eh anulada 

        if tabuleiro[linha - 1][coluna - 1] != "_":# verifica se a ja foi ocupada, "-1" é necessario para traduzir o valor inserido para index
            print("Essa posição já está ocupada.")
            continue

        tabuleiro[linha - 1][coluna - 1] = X_ou_O

        if verificar_vit(tabuleiro, X_ou_O): # se verificar_vitoria retornar true, o jogo termina mostrando quem ganhou
            mostra_tab(tabuleiro)
            print(f"Jogador {X_ou_O} ganhou")
            break

        if all(tabuleiro[i][j] != "_" for i in range(tamanho) for j in range(tamanho)): #se todos as casas forem diferente do simbolo padrao, e nenhum dos ifs anteriores forem executatos, significa que deu velha
            mostra_tab(tabuleiro)
            print("Deu velha.")
            return

        X_ou_O = "O" if X_ou_O == "X" else "X" # troca o jogador para O e X vice-versa(por jogada)

jogo_da_velha() #executa o jogo