
def jogar_forca():
    print("*********************************")
    print("***Bem vindo ao jogo da FORCA!***")
    print("*********************************")

    palavra_secreta = "cinderella"
    acertou = False
    enforcou = False

    while(not enforcou and not acertou):
        chute = input("Qual letra??")
        chute = chute.strip() #não deixa espaços no inicio e no final

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("Encontrou a letra {} na posição {}".format(letra, index))
            index = index + 1

if(__name__ == "__main__"):
    jogar_forca()