alunos = []
aluno = []
altura = []
idade = []
nome = []
s = 0
qa = 0
maltura = s / 2
for c in range(0,2):
    altura.clear()
    idade.clear()
    nome.clear()
    nome.append(str(input('Digite o seu nome: ')))
    idade.append(int(input('Digite a sua idade: ')))
    h = int(input('Digite a sua altura, em cm: '))
    altura.append(h)
    s += h
    aluno.append(nome[:])
    aluno.append(idade[:])
    aluno.append(altura[:]) 
    alunos.append(aluno[:])
    aluno.clear()
for l, v in enumerate(alunos):
    for a in v :
        if a[2] > maltura :
            qa += 1
print(alunos)
print(qa)