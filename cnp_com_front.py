import requests
import customtkinter as custom 
custom.set_appearance_mode("dark")
def pagina_info_cnpj():
    cnpj = entrada_cnpj.get()

    if cnpj == "":
        mensagem_erro = custom.CTkTextbox(projeto_cnpj,width=250,height=10)
        mensagem_erro.insert("0.0","você não digitou nada ")
        mensagem_erro.configure(state= "disabled")
        mensagem_erro.pack()
        mensagem_erro.after(2000,mensagem_erro.destroy) 
        
       




    elif (len(cnpj)) !=14:
        mensagem_erro = custom.CTkTextbox(projeto_cnpj,width=250,height=10)
        mensagem_erro.insert("0.0"," CNPJ deve conter 14 numeros")
        mensagem_erro.configure(state= "disabled")
        mensagem_erro.pack()
        mensagem_erro.after(2000,mensagem_erro.destroy) 
        
    elif  cnpj.isdigit():
        pagina_info = custom.CTkToplevel(projeto_cnpj)
        custom.set_appearance_mode("dark")
        entrada_cnpj.delete(0,"end")
        link = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"
        res = requests.get(link)
        info_cnpj = res.json()
        descricao_info_cnpj=custom.CTkLabel(pagina_info,text="informações do CNPJ",font=("Arial",30))
        descricao_info_cnpj.pack()
        frame=custom.CTkFrame(pagina_info,width=1500,height=1000)
        frame.pack(pady=270)
        infos_cnpj = custom.CTkLabel(frame,text=f"""
                                  Nome da empresa: {info_cnpj.get("razao_social","Não encontrado")} 
                                  \n
                                  Estado: {info_cnpj.get("uf","Não encontrado")}
                                  \n
                                  Cidade: {info_cnpj.get("municipio","Não encontrado")}
                                  \n
                                  Patrimonio liquido: {info_cnpj.get("valor_patrimonio_liquido","Não encontrado")}               
                                  \n
                                  Email: {info_cnpj.get("Email","Não encontrado")}
                                  \n
                                  Pais: {info_cnpj.get("Pais","Não encontrado")}
                                  \n
                                  Telefone:{info_cnpj.get("ddd_telefone_1","Não encontrado")}
                                  \n
                                  Natureza juridica: {info_cnpj.get("natureza_juridica","Não encontrado")}
                                  \n
                                  Status: {info_cnpj.get("status","Não encontrado")}
                                  \n
                                  Tipo:: {info_cnpj.get("type","Não encontrado")}


""")
           
        infos_cnpj.pack()
    
        

projeto_cnpj = custom.CTk()
projeto_cnpj.geometry("550x550")
descricao_cnpj=custom.CTkLabel(projeto_cnpj,text="Busca de CNPJ",font=("Arial",30))
descricao_cnpj.pack(pady=250)
entrada_cnpj = custom.CTkEntry(projeto_cnpj,placeholder_text="Digite o numero do CNPJ",width=270)
entrada_cnpj.pack(pady=1)
custom.CTkButton(projeto_cnpj,text ="buscar",command=pagina_info_cnpj).pack(pady=30)

projeto_cnpj.mainloop()