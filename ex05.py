valores = []
par = []
impar = []
for c in range(0,10) :
    valores.append(int(input('Digite um número: ')))
for a in valores:
    if a % 2 == 0 :
        par.append(a)
    else :
        impar.append(a)
print(f'A lista de todos os números é {valores}')
print(f'A lista de números pares é {par}')
print(f'A lista de números ímpares é {impar}')