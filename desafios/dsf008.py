nota = []

bim = int(input("Quantos notas foram: "))

for i in range(bim):
  n = float(input(f"Digite sua nota do {i+1}º: "))
  nota.append(n)
  
media = sum(nota) / bim

print(f"Media {media}")
