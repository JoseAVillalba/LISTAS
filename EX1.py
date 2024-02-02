cadena = input()
frase = list(cadena)
res = [[] for _ in range(3)]

for x in range(len(frase)):
    res[0].append(frase[x])
    res[1].append(frase.count(frase[x]))

resultado_final = list(zip(res[0], res[1]))


print(set(resultado_final))
