try:
    numero = int(input("Digite um numero: "))
    print(numero)
except ZeroDivisionError:
    print("Divisão por zero não é possivel")
except ValueError:
    print("digite um valor valido.")
except:
    print("Erro inesperado")
finally:
    print("Sempre Executa")