import random

usuarioParImpar = input("Digite 'par' ou 'impar': ").strip().lower()
usuarioNumero = int(input("Digite seu numero de 1 a 10: "))
pcNumero = random.randint(1,10)
soma = pcNumero + usuarioNumero

print(f"Numero sorteado {pcNumero}")
print(f"Soma = {soma}")

if soma %2 == 0:
    print("Deu par")
    resultados = 'par'
else:
    print("Deu impar")
    resultados = 'impar'

if resultados == usuarioParImpar:
    print("Ganhou")
else:
    print("Perdeu kkkkk")