nome = str(input('Digite o seu nome: '))
saltos = []
s = 0
for c in range(0,5):
    s = float(input(f'Digite a sua altura do {c+1}° salto, em metros: '))
    saltos.append(s)
for b in saltos:
    s += b
media = s / 5
print(f'Atleta: {nome}')
for a in range(0,5):
    print(f'Salto {a+1} de {saltos[a]}m.')
print(f'A média de altura dos saltos é {media}m.')
