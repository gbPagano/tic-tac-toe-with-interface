def verificar_resultado(t):
    for i in range(3): #linhas
        if t[i][0] == t[i][1] and t[i][1] == t[i][2] and t[i][0] != " ":            
            return [1,"coluna", i]
    for i in range(3): #colunas
        if t[0][i] == t[1][i] and t[1][i] == t[2][i] and t[0][i] != " ":            
            return [1, "linha", i]
    #diagonais
    if t[0][0] == t[1][1] and t[1][1] == t[2][2] and t[1][1] != " ":       
        return [1, "diagonal_1"]
    if t[0][2] == t[1][1] and t[1][1] == t[2][0] and t[1][1] != " ":       
        return [1, "diagonal_2"]

    velha = True
    for i in range(3):
        for j in range(3):
            if t[i][j] == " ":
                velha = False
    if velha: return 2
    return 0

import random

def inteligencia(t,j1,j2,jogador,d):
   
    melhor_jogada = None
    melhor_result = None    
    
    if d == 2:
        disponiveis = verificar_disponibilidade(t)
        prof = 999999
        if len(disponiveis) == 9:
            return 0,0
        elif len(disponiveis) == 8:
            if t[1][1] == " ":
                return 1,1
            else: return 0,0
        else:
            for possibilidade in disponiveis:

                t[possibilidade[0]][possibilidade[1]] = j1
                result = minimax(t,j1,j2,jogador,prof)
                t[possibilidade[0]][possibilidade[1]] = " "
                                
                if melhor_result == None:
                    melhor_jogada = possibilidade
                    melhor_result = result
                elif result > melhor_result:
                    melhor_result = result
                    melhor_jogada = possibilidade
                    
            return melhor_jogada

    elif d == 1:
        disponiveis = verificar_disponibilidade(t)
        prof = 3                
        if len(disponiveis) == 8 and t[1][1] == " ":
            disponiveis.remove([1,1])
            return random.choice(disponiveis)
        elif len(disponiveis) == 9 or len(disponiveis) == 8:
            return random.choice(disponiveis)
        for possibilidade in disponiveis:

            t[possibilidade[0]][possibilidade[1]] = j1
            result = minimax(t,j1,j2,jogador,prof)
            t[possibilidade[0]][possibilidade[1]] = " "                
            if melhor_result == None:
                melhor_jogada = possibilidade
                melhor_result = result
            elif result > melhor_result:
                melhor_result = result
                melhor_jogada = possibilidade            
        if melhor_jogada == -1:
            return random.choice(disponiveis)
        return melhor_jogada
      
def minimax(t,j1,j2,jogador,prof):
    acabou = verificar_resultado2(t)
    if acabou == 1:
        if jogador == j1:
            return 1
        elif jogador == j2:
            return -1
    elif acabou == 2:
        return 0
    elif acabou == 0:
        if prof <= 0:
            return 0

        if jogador == j2:
            jogador = j1
        elif jogador == j1:
            jogador = j2
        melhor_result = None
        disponiveis = verificar_disponibilidade(t)
        for possibilidade in disponiveis:
            t[possibilidade[0]][possibilidade[1]] = jogador
            result = minimax(t,j1,j2,jogador,prof)
            t[possibilidade[0]][possibilidade[1]] = " "

            if melhor_result == None:
                melhor_result = result
            elif result < melhor_result:
                if jogador == j2:
                    melhor_result = result
            elif result > melhor_result:
                if jogador == j1:
                    melhor_result = result
            prof -=1
    
    return melhor_result

def verificar_disponibilidade(t):

    disponiveis = []
    for i in range(3):
        for j in range(3):
            if t[i][j] == " ":
                disponiveis.append([i,j])

    return disponiveis

def verificar_resultado2(t):
    for i in range(3): #linhas
        if t[i][0] == t[i][1] and t[i][1] == t[i][2] and t[i][0] != " ":         
            return 1
    for i in range(3): #colunas
        if t[0][i] == t[1][i] and t[1][i] == t[2][i] and t[0][i] != " ":          
            return 1
    #diagonais
    if t[0][0] == t[1][1] and t[1][1] == t[2][2] and t[1][1] != " ":        
        return 1
    if t[0][2] == t[1][1] and t[1][1] == t[2][0] and t[1][1] != " ":       
        return 1

    velha = True
    for i in range(3):
        for j in range(3):
            if t[i][j] == " ":
                velha = False
    if velha: return 2
    return 0