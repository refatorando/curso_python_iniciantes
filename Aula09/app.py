i = 1

while i < 10:
    print(i)
    #i += 1


print("terminou")
print(i)

criancas = ["Manu", "Vini", "Selina"]
#             0       1        2
for item in criancas:
    print(item)


canal = "Refatorando"

for letra in canal:
    print(letra)

for index in range(len(criancas)):
    print(criancas[index],index)

for index in range(len(criancas)):
    if index == 0:
        print(f"primeira linha {criancas[index]}")
    else:
        print(f"outras linhas {criancas[index]}")

matrix_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
]

for linha in matrix_numeros:
    print(linha)
    print("----")
    for coluna in linha:
        print(coluna)
