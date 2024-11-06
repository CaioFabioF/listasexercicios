# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
notas = []
valores = []
s= 0
media = s / 4
maior = 0
for g in range(0,3) :
    valores.clear()
    for c in range(0,4):
        valores.append(int(input(f'Digite a sua {c+1}° nota, aluno{g+1}: ')))
    notas.append(valores[:])
for a, b in enumerate(notas):
    s = 0
    for c in b :
        s += c
    media = s / 4
    if media >= 70 :
        maior += 1
print(f'Lista de notas dos alunos: {notas}')
print(f'{maior} tiraram a media maior que 70')