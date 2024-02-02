cadena = input()
frase = list(cadena)
res = [[] for _ in range(3)]

for x in range(len(frase)):
    res[0].append(frase[x])
    res[1].append(frase.count(frase[x]))

resultado_final = list(zip(res[0], res[1]))


print(set(resultado_final))
.................................................
taula=[[0]*15 for i in range(5)]

for i in range(5):
    for j in range(15):
        if i == 0 or i == 4 or j == 0 or j == 14:
            taula[i][j]=1

for fila in taula:
    for elemento in fila:
        print(elemento, end='')
    print()
