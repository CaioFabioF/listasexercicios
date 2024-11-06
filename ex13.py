lista1 = []
while True:
    n = int(input('Digite a sua nota: '))
    if n == -1 :
        break
    lista1.append(n)
print(f'A quantidade de termos na lista é de {len(lista1)} termos.')
print(f'A lista é: {lista1}')
lista1.reverse()
print(f'A lista em ordem reversa é : {lista1}')
s = 0
for a in lista1 :
    s += a
print(f'A soma dos valores é {s}')
media = s / len(lista1)
print(f'A média é {media}')
for a in lista1:
    if a > media :
        print(f'O valor {a} está acima da média')
    elif a > 7 : 
        print(f'O valor {a} é maior do que o número 7')
    else :
        print()
print('Fim')