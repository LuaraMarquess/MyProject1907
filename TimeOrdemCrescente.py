#programa crescente

x = int(input("Digite um número:   "))
y = int(input("Digite o segundo numero:   "))
z = int(input("Digite o terceiro numero:  "))


if x < y  and  y> z:
    print("Ordem crescente")
elif x > y and  y<z:
    print("Ordem decrescente")
else:
    print("Estão misturados...")