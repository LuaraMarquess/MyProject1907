
execucao = input("Serviço foi prestado? sim/nao:  ")
avaliacao = int(input("Qual é a nota da avaliação: (1/5) ?  "))

if execucao == "sim" and avaliacao ==1:
    print("O serviço foi péssimo!")
elif execucao == "sim" and avaliacao ==2:
    print("O serviço foi ruim")
elif execucao == "sim" and avaliacao ==3:
    print("O serviço foi razoavel")
elif execucao == "sim" and avaliacao ==4:
    print("O serviço foi Bom") 
elif   execucao == "sim" and avaliacao ==1:
    print("O serviço foi ótimo")
else:
    if execucao =="nao" and avaliacao == 0:
      reclamação = input("Descreva a sua reclamação   ")  
    else: 
     print("As suas avaliações nao fazem sentido!")
    
