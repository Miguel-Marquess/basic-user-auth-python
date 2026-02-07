import re

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
