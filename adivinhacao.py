import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")
    numero_secreto = round(random.randrange(1, 101))
    print("Numero secreto é ", numero_secreto)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Selecione nivel de dificuldade!", numero_secreto)
    print("(1)Facil  (2)Medio  (3)Dificil")

    print("operador novo", format(3 // 2))

    nivel = int(input("Definir nivel: "))

    if nivel == 1:
        total_de_tentativas = 15
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    while rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabéns! Você acertou! Sua pontuação foi {}".format(pontos))
            break
        else:
            if maior:
                print("O seu chute foi maior do que o número secreto!")
            elif (menor):
                print("O seu chute foi menor do que o número secreto!")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
