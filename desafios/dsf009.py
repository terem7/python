import random

n = random.randint(1,100)

while True:
  chute = int(input("Advinhe o numero de 1 a 100: "))

  if chute > n:
    print("Errou. Menor")
    continue
  elif chute == n:
    print("Acertou")
    break
  else:
    print("Errou, Maior")
    continue