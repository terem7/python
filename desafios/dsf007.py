numeros = []
numeros_pares = []
numeros_impar = []

for i in range(10):
  num = int(input("Digite numero: "))
  numeros.append(num)

for j in numeros:
  if j %2 == 0:
    numeros_pares.append(j)
  else:
    numeros_impar.append(j)

print(numeros)
print(numeros_impar)
print(numeros_pares)