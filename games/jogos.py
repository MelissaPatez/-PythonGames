import adivinhacao
import forca 

def escolhe_jogo():
    print("********************************")
    print("*****Escolha o seu jogo!!******")
    print("********************************")

    print("(1)Forca (2)Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("jogo da forca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("jogo de adivinhação")
        adivinhacao.jogar_adivinhacao()

if(__name__ "__main__"):
    escolhe_jogo()