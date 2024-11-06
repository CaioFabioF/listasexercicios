caracteres = []
vogais = ['A','E','I','O','U']
for c in range(0,5) :
    caracteres.append(str(input('Digite 1 caractere: ')).upper())
for a in caracteres :
    if a not in 'AEIOU' :
        print(f'{a}',end=' ')
print('\nFim')
