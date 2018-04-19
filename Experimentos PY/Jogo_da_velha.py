#################
### VARIAVEIS ###
#################
matriz = [['_','_','_'],['_','_','_'],['_','_','_']]
jg1 = 'O'
jg2 = 'X'
cont = 0

#######################
### EXIBE TABULEIRO ###
#######################
def tabuleiro():
    for x in range(len(matriz)):
        for y in range(len(matriz[x])):
            print(matriz[x][y], end=' ')
        print()
    print()

#################################
### VERIFICA SE ALGUÉM GANHOU ###
#################################
def verifica_ganhador():

    if(((matriz[0][0] == jg1) and (matriz[0][1] == jg1) and (matriz[0][2] == jg1))
    or ((matriz[1][0] == jg1) and (matriz[1][1] == jg1) and (matriz[1][2] == jg1))
    or ((matriz[2][0] == jg1) and (matriz[2][1] == jg1) and (matriz[2][2] == jg1))
    or ((matriz[0][0] == jg1) and (matriz[1][0] == jg1) and (matriz[2][0] == jg1))
    or ((matriz[0][1] == jg1) and (matriz[1][1] == jg1) and (matriz[2][1] == jg1))
    or ((matriz[0][2] == jg1) and (matriz[1][2] == jg1) and (matriz[2][2] == jg1))
    or ((matriz[0][0] == jg1) and (matriz[1][1] == jg1) and (matriz[2][2] == jg1))
    or ((matriz[0][2] == jg1) and (matriz[1][1] == jg1) and (matriz[2][0] == jg1))):
        print("Jogador 1 Venceu.")
        return False

    if(((matriz[0][0] == jg2) and (matriz[0][1] == jg2) and (matriz[0][2] == jg2))
    or ((matriz[1][0] == jg2) and (matriz[1][1] == jg2) and (matriz[1][2] == jg2))
    or ((matriz[2][0] == jg2) and (matriz[2][1] == jg2) and (matriz[2][2] == jg2))
    or ((matriz[0][0] == jg2) and (matriz[1][0] == jg2) and (matriz[2][0] == jg2))
    or ((matriz[0][1] == jg2) and (matriz[1][1] == jg2) and (matriz[2][1] == jg2))
    or ((matriz[0][2] == jg2) and (matriz[1][2] == jg2) and (matriz[2][2] == jg2))
    or ((matriz[0][0] == jg2) and (matriz[1][1] == jg2) and (matriz[2][2] == jg2))
    or ((matriz[0][2] == jg2) and (matriz[1][1] == jg2) and (matriz[2][0] == jg2))):
        print("Jogador 2 Venceu.")
        return False

    return True

############################
### Inteligencia Maquina ###
############################
#def inteligencia_maqina():




#################
### PRINCIPAL ###
#################
começar = input("Vamos Jogar? \nSim(s) Não(n) \n")

if(começar == 's'):
    tabuleiro()
    while(verifica_ganhador()):

            px = int(input("posição x: "))
            py = int(input("posição y: "))

            if (matriz[px][py] == '_'):
                if ((cont % 2) == 0):
                    matriz[px][py] = jg1
                    cont += 1
                else:
                    matriz[px][py] = jg2
                    cont += 1
            else:
                print("Jogada Impossível")
            tabuleiro()

else:
    exit()