from funcoes.funcoesregex import *
from funcoes.arquivosjson import *
from funcoes.transformhash import *
from funcoes.menu import *


nome_arquivo = "dados_pessoas.json"
while True:
    lista_dados = obter_dados(nome_arquivo)
    print("-"*40)
    menu1 = str(menu(["Cadastrar-se", "Login", "Apagar usúario", "Sair do sistema"]))
    print("-"*40)
    if menu1 == "1":
        novo_usuario = cadastro()
        lista_dados.append(novo_usuario)
        adicionar_lista(nome_arquivo, lista_dados)
    elif menu1 == "2":
        email_usuario = validar_email()
        validar_login(lista_dados, email_usuario)
       
    elif menu1 == "3":
        email_usuario = validar_email()
        login = validar_login(lista_dados, email_usuario)
        if login:
            while True:
                cpf_del = validar_cpf()
                for usuario in lista_dados:
                    if usuario["cpf"] == cpf_del and usuario["email"] == email_usuario:
                        flag = str(input("Quer mesmo deletar seu usuário? (S/N)\n>>> ")).strip().upper()[0]
                        if flag == "S":
                            lista_dados.remove(usuario)
                            adicionar_lista(nome_arquivo, lista_dados)
                            print("-"*40)
                            print("O usuário foi removido do sistema. ")
                            print("-"*40)
                            break
                        elif flag == "N":
                            print("-"*40)
                            print("Usuario não foi deletado!")
                            print("-"*40)
                            break
                
                else:
                    print("CPF incorreto! Digite novamente. ")

                break
    elif menu1 == "4":
        print("Saindo do menu...")
        break

    else:
        print("Digite uma opçao válida. ")

