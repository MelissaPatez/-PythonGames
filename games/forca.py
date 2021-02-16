import random

def jogar_forca():

    menssagemAbertura()
    palavra_secreta = palavraSecreta()  
   
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    acertou = False
    enforcou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = solicitaChute()
       
        if (chute in palavra_secreta):
            marca_chuteCorreto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        
    if(acertou):
        menssagemVencedor()
    else:
        menssagemPerdedor(palavra_secreta)
        
    print("Fim do jogo")


def menssagemAbertura():
    print("*********************************")
    print("***Bem vindo ao jogo da FORCA!***")
    print("*********************************")

def palavraSecreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def solicitaChute():
    print("------------------")
    chute = input("Qual letra?? ")
    chute = chute.strip().upper() #não deixa espaços no inicio e no final
    return chute
   

def marca_chuteCorreto(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def menssagemVencedor():
    print("---------------------------------")
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print("---------------------------------")

def menssagemPerdedor(palavra_secreta):
    print("------------------------------------------------------")
    print(
            """
            _____       ___       ___  ___   _____  
            /  ___|     /   |     /   |/   | |  ___| 
            | |        / /| |    / /|   /| | | |__   
            | |  _    / ___ |   / / |__/ | | |  __|  
            | |_| |  / /  | |  / /       | | | |___  
            \_____/ /_/   |_| /_/        |_| |_____|
            
            _____   _     _   _____   _____   
            /  _  \ | |   / / |  ___| |  _  \  
            | | | | | |  / /  | |__   | |_| |  
            | | | | | | / /   |  __|  |  _  /  
            | |_| | | |/ /    | |___  | | \ \  
            \_____/ |___/     |_____| |_|  \_\

            """
        )
    print("A palavra era {}".format(palavra_secreta))
    print("------------------------------------------------------")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if(__name__ == "__main__"):
    jogar_forca()