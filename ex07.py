numeros = []
s = 0
m = 1
for c in range(0,5):
    numeros.append(int(input('Digite um número: ')))
for a in numeros :
    s += a
for b in numeros:
    m *= b
print(f'A lista de números é {numeros}')
print(f'A soma de todos os números é {s}')
print(f'A multiplicação de todos os números é {m}')