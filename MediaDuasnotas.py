#programa duas notas 

nota1 = float(input("Digite a primeira nota:  "))
nota2 = float(input("Digite a segunda nota:   "))

media = (nota1 + nota2)/2


if (media < 4):
    print(f"Aluno reprovado com media = {media}  ")
elif (media > 6):
    print(f"Aluno aprovado direto")
elif media >=4 and media <6: 
    nota_rec = float(input("Digite a nota de recuperação"))
    if nota_rec<=5:
        print(f"Reprovado na recuperacao com nota: {nota_rec}")
else:
    print(f"Aprovado na recuperacao: ")