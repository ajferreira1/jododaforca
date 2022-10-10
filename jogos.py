import adivinhacao
import forca

print("*********************************")
print("Bem vindo! Escolha um jogo")
print("*********************************")

print("(1) Adivinhação  (2) Forca ")

jogo = int(input("Escolha um jogo"))

if jogo == 1:
    print("Jogo escolhido: Adivinhação")
    adivinhacao.jogar()
elif jogo == 2:
    print("Jogo escolhido: Forca")
    forca.jogar()
