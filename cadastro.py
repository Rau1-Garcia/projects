import sys
import time 
from colorama import Fore, Style, init
from pwinput import pwinput

dados = []
frase = "Oi tudo bem ? \nvamos  fazer seu  cadastro ?"

for texto in frase:
    sys.stdout.write(Fore.YELLOW + texto)
    sys.stdout.flush()
    time.sleep(0.07)
print(Style.RESET_ALL)

resp = input("Digite: ").strip().lower()

while resp != "sim":
    if resp == "não":
        resp = input("ok digite sim quando querer fazer o cadastro: ").strip().lower()
    else:
        resp = input("resposta invalida digite novamente: ").strip().lower()

frase = ("Ok, então vamos começar")
for texto in frase:
    sys.stdout.write(Fore.YELLOW + texto)
    sys.stdout.flush()
    time.sleep(0.07)
print(Style.RESET_ALL)

frase = (
    "Muito bem , primeiramente vamos criar uma senha \n"
    "para voce visualizar suas inforamações quando quiser"
)

for texto in frase:
    sys.stdout.write(Fore.YELLOW + texto)
    sys.stdout.flush()
    time.sleep(0.07)

print(Style.RESET_ALL)

senha = pwinput("crie sua senha: ", mask="*")

while senha == "":
    senha = pwinput("crie sua senha: ", mask="*")
    print("senha cadastrada")

nome = input("\nSeu nome: ")
while nome == "":
    nome = input("\nSeu nome: ")
dados.append(nome)

pai = input("\nNome do Pai : ")
while pai == "":
    pai = input("\nnome do pai: ")
dados.append(pai)

if pai == "ausente":
    idade = int(input("digte sua idade: "))
    if idade <= 17:
        responsavel_legal_paterno = input("digte o nome do responsavel: ")
        while responsavel_legal_paterno == "":
            responsavel_legal_paterno = input("digte o nome do responsavel: ")
        dados.append(responsavel_legal_paterno)
    else:
        pai = "ausente"
        dados.append(pai)

mae = input("\nDigite o nome da Mãe : ")
while mae == "":
    mae = input("\nDigite o nome da mãe: ")
dados.append(mae)

if mae == "ausente":
    idade = int(input("Digte sua idade: "))
    if idade <= 17:
        responsavel_legal_materno = input("\ndigte o nome do responsavel: ")
        while responsavel_legal_materno == "":
            responsavel_legal_materno = input("\ndigte o nome do responsavel: ")
        dados.append(responsavel_legal_materno)
    else:
        mae = "ausente"
        dados.append(mae)

data = input("\nDigite sua data de nascimento: ")
while data == "":
    data = input("\nDigite sua data de nascimento: ")
dados.append(data)

cpf = input("\nDigite seu CPF: ")
while cpf == "" or not cpf.isdigit():
    cpf = input("\nDigite seu CPF: ")
dados.append(cpf)

cep = input("\nCEP: ")
while cep == "" or not cep.isdigit():
    cep = input("\nDigite seu CEP: ")
dados.append(cep)

cidade = input("\nCidade: ")
while cidade == "":
    cidade = input("\nDigite o nome da sua cidade: ")
dados.append(cidade)

estado_civil = input("\nEstado civil: ")
while estado_civil == "":
    estado_civil = input("\nDigite seu estado civil: ")
dados.append(estado_civil)

escolaridade = input("\nDigite seu nivel de escolaridade: ")
while escolaridade == "":
    escolaridade = input("\nDigite seu nivel de escolaridade: ")
dados.append(escolaridade)

telefone = input("\nDigite seu numero de telefone: ")
while telefone == "" or not telefone.isdigit():
    telefone = input("\nDigite seu numero de telefone: ")
dados.append(telefone)

estado = input("\nDigite o nome do seu estado: ")
while estado == "":
    estado = input("\nDigite o nome do seu estado: ")
dados.append(estado)

nacionalidade = input("\ndigite sua nacionalida: ")
while nacionalidade == "":
    nacionalidade = input("\ndigite sua nacionalida: ")
dados.append(nacionalidade)

endereco = input("\nDigite seu endereço:  ")
while endereco == "":
    endereco = input("\nDigite seu endereço: ")
dados.append(endereco)

frase = "Para vizualizar suas informações digite sua senha "
for texto in frase:
    sys.stdout.write(Fore.YELLOW + texto)
    sys.stdout.flush()
    time.sleep(0.07)
print(Style.RESET_ALL)

senha_cadastrada = pwinput("digite sua senha: ", mask="*")
if senha_cadastrada == senha:
    frase = (f"Nome: {dados [0]} ")
    for texto in frase:
        sys.stdout.write(Fore.BLUE + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    frase = (f"Pai: {dados [1]} ")
    for texto in frase:
        sys.stdout.write(Fore.BLUE + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    frase = (f"Mãe: {dados [2]} ")
    for texto in frase:
        sys.stdout.write(Fore.BLUE + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    frase = (f"Data de nascimento: {dados [3]} ")
    for texto in frase:
        sys.stdout.write(Fore.BLUE + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    frase = (f"CPF: {dados [4]} ")
    for texto in frase:
        sys.stdout.write(Fore.BLUE + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    frase = (f"CEP: {dados [5]} ")
    for texto in frase:
        sys.stdout.write(Fore.BLUE + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    frase = (f"Cidade: {dados [6]} ")
    for texto in frase:
        sys.stdout.write(Fore.BLUE + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    frase = (f"Estado civil: {dados [7]} ")
    for texto in frase:
        sys.stdout.write(Fore.BLUE + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    frase = (f"Escolaridade: {dados [8]} ")
    for texto in frase:
        sys.stdout.write(Fore.BLUE + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    frase = (f"Telefone: {dados [9]} ")
    for texto in frase:
        sys.stdout.write(Fore.BLUE + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    frase = (f"Estado: {dados [10]} ")
    for texto in frase:
        sys.stdout.write(Fore.BLUE + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    frase = (f"Nacionalidade: {dados [11]} ")
    for texto in frase:
        sys.stdout.write(Fore.BLUE + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    frase = (f"Endereço: {dados [12]} ")
    for texto in frase:
        sys.stdout.write(Fore.BLUE + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

while True:
    frase = "1 Rever informações"
    for texto in frase:
        sys.stdout.write(Fore.YELLOW + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    frase = ("_____________" * 2)
    for texto in frase:
        sys.stdout.write(Fore.YELLOW + texto)
        sys.stdout.flush()
        time.sleep(0.1)
    print(Style.RESET_ALL)

    frase = "2 Mudar informação"
    for texto in frase:
        sys.stdout.write(Fore.YELLOW + texto)
        sys.stdout.flush()
        time.sleep(0.7)
    print(Style.RESET_ALL)

    frase = ("_____________" * 2)
    for texto in frase:
        sys.stdout.write(Fore.YELLOW + texto)
        sys.stdout.flush()
        time.sleep(0.1)
    print(Style.RESET_ALL)

    frase = "3 Ver quantidade de informações"
    for texto in frase:
        sys.stdout.write(Fore.YELLOW + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    frase = ("_____________" * 2)
    for texto in frase:
        sys.stdout.write(Fore.YELLOW + texto)
        sys.stdout.flush()
        time.sleep(0.1)
    print(Style.RESET_ALL)

    frase = "4 Sair"
    for texto in frase:
        sys.stdout.write(Fore.YELLOW + texto)
        sys.stdout.flush()
        time.sleep(0.07)
    print(Style.RESET_ALL)

    opc = input("escolha um opção:")

    if opc == "1":
        frase = "Para vizualizar suas informações digite sua senha novamente"
        for texto in frase:
            sys.stdout.write(Fore.YELLOW + texto)
            sys.stdout.flush()
            time.sleep(0.07)
        print(Style.RESET_ALL)

        senha_cadastrada = pwinput("digite sua senha: ", mask="*")
        if senha_cadastrada == senha:
            frase = (f"Nome: {dados [0]} ")
            for texto in frase:
                sys.stdout.write(Fore.BLUE + texto)
                sys.stdout.flush()
                time.sleep(0.07)
            print(Style.RESET_ALL)

            frase = (f"Pai: {dados [1]} ")
            for texto in frase:
                sys.stdout.write(Fore.BLUE + texto)
                sys.stdout.flush()
                time.sleep(0.07)
            print(Style.RESET_ALL)

            frase = (f"Mãe: {dados [2]} ")
            for texto in frase:
                sys.stdout.write(Fore.BLUE + texto)
                sys.stdout.flush()
                time.sleep(0.07)
            print(Style.RESET_ALL)

            frase = (f"Data de nascimento: {dados [3]} ")
            for texto in frase:
                sys.stdout.write(Fore.BLUE + texto)
                sys.stdout.flush()
                time.sleep(0.07)
            print(Style.RESET_ALL)

            frase = (f"CPF: {dados [4]} ")
            for texto in frase:
                sys.stdout.write(Fore.BLUE + texto)
                sys.stdout.flush()
                time.sleep(0.07)
            print(Style.RESET_ALL)

            frase = (f"CEP: {dados [5]} ")
            for texto in frase:
                sys.stdout.write(Fore.BLUE + texto)
                sys.stdout.flush()
                time.sleep(0.07)
            print(Style.RESET_ALL)

            frase = (f"Cidade: {dados [6]} ")
            for texto in frase:
                sys.stdout.write(Fore.BLUE + texto)
                sys.stdout.flush()
                time.sleep(0.07)
            print(Style.RESET_ALL)

            frase = (f"Estado civil: {dados [7]} ")
            for texto in frase:
                sys.stdout.write(Fore.BLUE + texto)
                sys.stdout.flush()
                time.sleep(0.07)
            print(Style.RESET_ALL)

            frase = (f"Escolaridade: {dados [8]} ")
            for texto in frase:
                sys.stdout.write(Fore.BLUE + texto)
                sys.stdout.flush()
                time.sleep(0.07)
            print(Style.RESET_ALL)

            frase = (f"Telefone: {dados [9]} ")
            for texto in frase:
                sys.stdout.write(Fore.BLUE + texto)
                sys.stdout.flush()
                time.sleep(0.07)
            print(Style.RESET_ALL)

            frase = (f"Estado: {dados [10]} ")
            for texto in frase:
                sys.stdout.write(Fore.BLUE + texto)
                sys.stdout.flush()
                time.sleep(0.07)
            print(Style.RESET_ALL)

            frase = (f"Nacionalidade: {dados [11]} ")
            for texto in frase:
                sys.stdout.write(Fore.BLUE + texto)
                sys.stdout.flush()
                time.sleep(0.07)
            print(Style.RESET_ALL)

            frase = (f"Endereço: {dados [12]} ")
            for texto in frase:
                sys.stdout.write(Fore.BLUE + texto)
                sys.stdout.flush()
                time.sleep(0.07)
            print(Style.RESET_ALL)

        while senha_cadastrada != senha:
            senha_cadastrada = pwinput("Digite sua senha correta ", mask="*")

    elif opc == "2":
        while True:
            frase = "Para vizualizar o menu e alterar suas informações  digite sua senha novamente"
            for texto in frase:
                sys.stdout.write(Fore.YELLOW + texto)
                sys.stdout.flush()
                time.sleep(0.07)
            print(Style.RESET_ALL)

            senha_cadastrada = pwinput("digite sua senha: ", mask="*")

            if senha_cadastrada == senha:
                frase = "Neste menu você podera  selecionar  informações que podem ser alteradas\nAVISO ALGUMAS OPCÕES SÃO INALTERAVEIS ENTÃO NÃO ESTÃO DISPONIVEIS"
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                    time.sleep(0.07)
                print(Style.RESET_ALL)

                frase = ("_____________" * 2)
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                print(Style.RESET_ALL)

                frase = "1 Mudar estado civil:"
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                    time.sleep(0.07)
                print(Style.RESET_ALL)

                frase = ("_____________" * 2)
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                print(Style.RESET_ALL)

                frase = "2 Mudar endereço"
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                    time.sleep(0.01)
                print(Style.RESET_ALL)

                frase = ("_____________" * 2)
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                print(Style.RESET_ALL)

                frase = "3 Mudar Telefone"
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                    time.sleep(0.07)
                print(Style.RESET_ALL)

                frase = ("_____________" * 2)
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                print(Style.RESET_ALL)

                frase = "4 Mudar cidade"
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                    time.sleep(0.07)
                print(Style.RESET_ALL)

                frase = ("_____________" * 2)
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                print(Style.RESET_ALL)

                frase = "5 Mudar estado"
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                    time.sleep(0.07)
                print(Style.RESET_ALL)

                frase = ("_____________" * 2)
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                print(Style.RESET_ALL)

                frase = "6 Mudar CEP"
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                    time.sleep(0.07)
                print(Style.RESET_ALL)

                frase = ("_____________" * 2)
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                print(Style.RESET_ALL)

                frase = "7 Sair"
                for texto in frase:
                    sys.stdout.write(Fore.YELLOW + texto)
                    sys.stdout.flush()
                    time.sleep(0.07)
                print(Style.RESET_ALL)

                mudar = input("digite: ")

                if mudar == "1":
                    estado_civil_novo = input("Mude o seu estado_civil: ")
                    indice = dados.index(estado_civil)
                    dados[7] = estado_civil_novo

                elif mudar == "2":
                    endereco_novo = input("Digite seu novo endereço ")
                    dados[12] = endereco_novo

                elif mudar == "3":
                    telefone_novo = input("Digite seu novo numero de telefone ")
                    dados[9] = telefone_novo

                elif mudar == "4":
                    cidade_novo = input("Digite sua nova cidade: ")
                    indice = dados.index(cidade)
                    dados[6] = cidade_novo

                elif mudar == "5":
                    endereco_novo = input("Digite seu novo estado:  ")
                    indice = dados.index(estado)
                    dados[10] = endereco_novo

                elif mudar == "6":
                    cep_novo = input("Digite seu novo CEP:  ")
                    indice = dados.index(cep)
                    dados[5] = cep_novo

                elif mudar == "7":
                    break

                else:
                    print("erro")

    elif opc == "3":
        qtde = (len(dados))
        print(f"A quantidade de informações no seu cadastro é {qtde} informações")

    elif opc == "6":
        frase = "OK,muito obrigado pelo seu cadastro"
        for texto in frase:
            sys.stdout.write(Fore.YELLOW + texto)
            sys.stdout.flush()
            time.sleep(0.07)
        print(Style.RESET_ALL)
        break


           
       






   






   