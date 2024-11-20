compras=[1,2,3,4,5,6,7,8,9,10,]
cont=str

compras[0]=input("Digite um item: ")
print("\n")
compras[1]=input("Digite um item: ")
print("\n")
compras[2]=input("Digite um item: ")
print("\n")
compras[3]=input("Digite um item: ")
print("\n")
compras[4]=input("Digite um item: ")
print("\n")
compras[5]=input("Digite um item: ")
print("\n")
compras[6]=input("Digite um item: ")
print("\n")
compras[7]=input("Digite um item: ")
print("\n")
compras[8]=input("Digite um item: ")
print("\n")
compras[9]=input("Digite um item: ")
print("\n")
cont=input("quer continuar adicionando coisas ?: ")

if cont=="sim":
    compras[11]=input("Digite um item: ")
    compras.append(compras[11])
    
elif cont=="não":
   print("ok,lista finalizada")

elif cont=="":
   print("ERRO")

else :
   print("ERRO")




    

