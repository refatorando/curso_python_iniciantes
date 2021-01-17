familia = ["Roger","Cris","Manu","Vini","Selina"]
#            0       1       2     3       4
#             -5    -4      -3    -2      -1

print(familia[3])# - retorna um indice
print(familia[-3])# - retorna um indice de traz pra frente
print(familia[2:])# - retorna a partir do indice 2
print(familia[2:4])# - retorna a partir do indeico até o 4, excluindo o 4

print(familia)
familia[3] = "Roger"
print(familia)

familia.extend(["Fernando","Rosania"])

familia.append("Spock")
familia.insert(2,"Spock")

familia.pop()
familia.pop()

familia.remove("Spock")

familia.clear()

print(familia.count("Roger"))

print(familia)

idade_familia = [34,36,13,11,2]
print(familia)
print(idade_familia)
idade_familia.sort()
familia.sort()
print(idade_familia)
print(familia)
familia.sort()
familia.reverse()
print(familia)
 familia2 = familia
 familia.remove("Roger")
 print(familia)
 print(familia2)

coordenadas = (-49,-36)
print(coordenadas.count(-49))