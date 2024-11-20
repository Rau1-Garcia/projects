registro=["nome","cpf","cidade","estado"]
cond1=str
cond2=str
cond3=int
print("----"*20)
registro[0]=input("digite seu nome por favor: ")
print("----"*20)
registro[1]=input("digite seu cpf por favor: ")
print("----"*20)
registro[2]=input("digite sua cidade por favor: ")
print("----"*20)
registro[3]=input("digite seu estado por favor: ")
print("----"*20)
cond1=input("gostaria de verificar seu registro ?: ")
print("----"*20)
if cond1=="sim":
 print(registro[0])
 print("----"*20)
 print(registro[1])
 print("----"*20)
 print(registro[2])
 print("----"*20)
 print(registro[3])
 print("----"*20)
elif cond1=="não":
  print("Ok,obrigado")
elif cond1 != "sim" and cond1 != "não":
    while cond1== "":
       cond1=input("por favor respnda se gostaria de verificar seu registro: ")
if cond1=="sim":    
    print(registro[0])
    print("----"*20)
    print(registro[1])
    print("----"*20)
    print(registro[2])
    print("----"*20)
    print(registro[3])
    print("----"*20)
elif cond1=="não":
    print("ok,obrigado")
else:
    print("erro")
cond2=input("gostaria de adicionar mais informações ?: ")
print("----"*20)
if cond2=="sim":
  print("----"*20)
nova=input("adiocione uma nova informação: ")
registro.append(nova)
print("----"*20)
cond3=input("gostaria de ver os registros com a nova informação ?:  ")
if cond3=="sim":
    print(registro[0])
    print("----"*20)
    print(registro[1])
    print("----"*20)
    print(registro[2])
    print("----"*20)
    print(registro[3])
    print("----"*20)
    print(registro[4])
    print("----"*20)   
else:
    print("erro")


























              
    
