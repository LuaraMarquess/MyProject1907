funcao = input("Digite a sua função: Goleiro/ Zagueiro/ Lateral/Atacante/Centrovante/Volante/Meia/Ponta/ponta    ")

if funcao == "Goleiro" or funcao =="Zagueiro" or funcao =="Lateral":
    print("Defesa")
elif funcao == "Volante" or funcao == "meia":
 print("Meio Campo! ")
elif funcao == "ponta" or funcao =="atacante" or funcao == "cetrovante":
    print("Ataque")
else:
     print("Teimoso")

   