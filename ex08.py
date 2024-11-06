pessoas = []
pessoa = []
idade = []
altura = []
for c in range(0,2):
    idade.append(int(input('Digite a sua idade: ')))
    altura.append(int(input('Digite a sua altura em cm: ')))
    pessoa.append(idade[:])
    pessoa.append(altura[:])
    pessoas.append(pessoa[:])
    idade.clear() 
    altura.clear()
    pessoa.clear()
pessoas.sort(reverse=True)
for k, a in enumerate(pessoas):
    print(f'A pessoa {k+1} tem os dados {a}')