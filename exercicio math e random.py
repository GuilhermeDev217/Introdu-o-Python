import math
import random

print("Bem-vindo ao jogo de teste de conhecimentos matemáticos!")
num_aleatorio = random.randint(10, 150)
raiz = math.sqrt(num_aleatorio)
raiz_ar = round(raiz)

print("Esse é o seu número: ", num_aleatorio)

print("Qual é a raiz arredondada desse número? ")

numero = int(input())

if numero == raiz_ar:
    print("Você acertou!")
else:
    print("Você errou, a resposta correta era: ", raiz_ar)
