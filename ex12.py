a1 = []

tel = int(input('Telefonou para a vítima?[1-S/2-N]: '))
a1.append(tel)
est = int(input('Esteve no local do crime?[1-S/2-N]: '))
a1.append(est)
mor = int(input('Mora perto da vítima?[1-S/2-N]: '))
a1.append(est)
dev = int(input('Devia para a vítima?[1-S/2-N]: '))
a1.append(dev)
tra = int(input('Já trabalhou para a vítima?[1-S/2-N]: '))
a1.append(tra)
q = 0
for b in a1 :
    if b == 1 :
        q += 1
if q == 2 :
    print('Suspeita')
elif q > 2 and q <= 4 :
    print('Cúmplice')
elif q == 5 :
    print('Assasino')
else:
    print('Inocente')