vetor = []
s = 0
for c in range(0,10):
    vetor.append(int(input('Digite o seu número: ')))
for a in vetor :
    a = a ** 2
    s += a
print(f'A lista numérica é : {vetor}')
print(f'A soma dos quadros de todos os números é: {s}')