numeros = []

for i in range(10):
  num = int(input("Digite um numero: "))
  numeros.append(num)

numeros_pares = []

for j in numeros:
  if j %2 == 0:
    numeros_pares.append(j)

print(numeros_pares)