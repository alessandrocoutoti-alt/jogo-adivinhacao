import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while tentativas < 10:
    try:
        palpite = int(input("Digite um número entre 1 e 100: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Mais alto!")
        elif palpite > numero_secreto:
            print("Mais baixo!")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas!")
            break

    except ValueError:
        print("Por favor, digite um número válido.")
else:
    print(f"Você não conseguiu em 10 tentativas. O número era {numero_secreto}.")