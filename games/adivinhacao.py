import random
def jogar_adivinhacao():
    print("********************************")
    print("Bem vindo no jogo de Adivinhacao")
    print("********************************")

    num_secreto = random.randrange(1,101)
    totalTentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual o nível de dificuldade??", num_secreto)
    print("(1)Fácil (2)Médio (3)Dificil")

    nivel= int(input("Define o nível: "))

    if (nivel == 1):
        totalTentativas = 10
    elif(nivel == 2):
        totalTentativas = 5
    else:
        totalTentativas = 3 

    for rodada in range(1, totalTentativas + 1):
        print("Tentativa {} de {}".format(rodada, totalTentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute = int(chute_str)
        print("----------------------------------------------")

        if(chute < 1 or chute > 100 ):
            print("Você deve digitar um número entre 1 e 100!!!")
            print("----------------------------------------------")
            continue

        acertou = chute == num_secreto
        maior = chute > num_secreto
        menor = chute < num_secreto


        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            print("----------------------------------------------")
            break
        else:
            if(maior):
                print("Você errou! o seu chute foi maior do que o número secreto.")
                print("----------------------------------------------")
            elif(menor):
                print("Você errou! o seu chute foi menor do que o número secreto.")
                print("----------------------------------------------")
        rodada = rodada +1
        pontos_perdidos = abs(num_secreto - chute)
        pontos = pontos - pontos_perdidos

    print("Fim do Jogo!!")

if(__name__ "__main__"):
    jogar_adivinhacao()