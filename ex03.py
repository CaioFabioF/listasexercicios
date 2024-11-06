notas = []
s = 0
for c in range(0,4) :
    notas.append(int(input('Digite a sua nota: ')))
for f, c in enumerate(notas):
    print(f'A nota {f+1} é {c}')
for c in notas :
    s += c
media = s / 4
print(f'A média é {media}')