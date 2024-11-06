vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = list()
for c in range(0,3):
    vetor1.append(int(input('Digite um número para o vetor1: ')))
for c in range(0,3):
    vetor2.append(int(input('Digite um número para o vetor2: ')))
for c in range(0,3):
    vetor3.append(int(input('Digite um número para o vetor3: ')))
for a in range(0,3):
    vetor4.append(vetor1[a])
    vetor4.append(vetor2[a])
    vetor4.append(vetor3[a])
print(vetor1)
print(vetor2)
print(vetor3)
print(vetor4)