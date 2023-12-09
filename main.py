import random

aleatorio=random.randint(1,10)
palpite=int(input("Entre com seu palpite de 1 a 10:"))

print("Número sorteado:",aleatorio)


if palpite>aleatorio:
    print("Puxa, você chutou alto D+")
if palpite<aleatorio:
    print("Puxa, você chutou baixo D+")
if palpite==aleatorio:
    print("Aeeee!!!, acertou em cheio!")

# bom dia :)