import re
from funcoes.transformhash import *
def validar_email():
    rule = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    # email@empresa.endereço
    while True:
        try:
            email = input("Digite seu email: ")
            if re.match(rule, email):
                return email
            else:
                raise ValueError
        except ValueError:
            print('Digite um valor válido')

def validar_cpf():
    rule = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
    while True:
        try:
            cpf = input("Digite seu CPF: ")
            if re.match(rule, cpf):
                return cpf
            else:
                raise ValueError
        except ValueError:
            print('Digite um valor válido. ')


def validar_telefone():
    rule = r"^\(\d{2}\)\s\d{4,5}-\d{4}$"
    while True:
        try:
            telefone = input("Digite seu telefone: ")
            if re.match(rule, telefone):
                return telefone
            else:
                raise ValueError
        except ValueError:
            print('Digite um valor válido. ') 


def validar_login(lista_dados, email_usuario):
    for usuario in lista_dados:
            if usuario["email"] == email_usuario:
                while True:
                    try:
                        senha = transformar_hash(input("Digite sua senha: \n >>> "))
                        if senha != usuario["senha"]:
                            raise ValueError
                        print("-"*40)
                        print(f"Login feito com sucesso!")
                        print("-"*40)  
                        return True
                    except ValueError:
                        print("Senha errada! Digite novamente. ")

    else:
        print("Email não existe. ")
        return False