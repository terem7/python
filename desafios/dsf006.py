numeros = []

for i in range(5):
  num = float(input("Digite um numero: "))
  numeros.append(num)

num_acima = []

for j in numeros:
  if j > 0:
    num_acima.append(j)

print(f"Numeros acime de zero: {len(num_acima)}")
print(f"Eles são {num_acima}")