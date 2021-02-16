import random

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
    chute = input("Qual letra??")
    chute = chute.strip().upper() #não deixa espaços no inicio e no final
    return chute

def marca_chuteCorreto(chute, palavra_secreta, letra):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def menssagemVencedor():
    print("Você Ganhou!!")
def menssagemPerdedor():
    print("Você Perdeu :/")
    
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
            marca_chuteCorreto(chute, palavra_secreta, letra)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

        
    if(acertou):
        menssagemVencedor()
    else:
        menssagemPerdedor()
        
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar_forca()