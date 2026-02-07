import json
from funcoes.funcoesregex import *
from funcoes.transformhash import *


def obter_dados(nome_arquivo): #obtem dados json, se nao existir, cria se nao tiver nada escrito, escreve
    while True:
        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as j:
                return json.load(j)
        except (FileNotFoundError, json.JSONDecodeError):
            with open(nome_arquivo, 'w', encoding='utf-8') as j:
                json.dump([], j)

def adicionar_usuarios(arquivo_json, usuario):
    try:
        with open(arquivo_json, 'w', encoding='utf-8') as a:
            json.dump(usuario, a, indent=4, ensure_ascii=False)
            return 'Usuario adicionado com sucesso. '
    except FileExistsError:
        return 'Pasta nao existe.'
    

def cadastro():
    usuario = {}
    
    usuario["email"] = validar_email()
    usuario["cpf"] = validar_cpf()
    usuario["telefone"] = validar_telefone()
    usuario["senha"] = transformar_hash(input("Crie uma senha: "))
    return usuario
