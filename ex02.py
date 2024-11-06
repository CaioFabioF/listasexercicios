a = []
for c in range(0,5) :
    a.append(int(input('Digite um número: ')))
a.sort(reverse=True)
for b in a :
    print(b,end=' ')