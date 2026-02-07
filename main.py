from funcoes.funcoesregex import *
from funcoes.arquivosjson import *
from funcoes.transformhash import *


nome_arquivo = "dados_pessoas.json"
lista_dados = obter_dados(nome_arquivo)
print(lista_dados)
novo_usuario = cadastro()
lista_dados.append(novo_usuario)
adicionar_usuarios(nome_arquivo, lista_dados)









# print(validar_email("miguel_pica123-@gmail.com"))
# print(validar_cpf("123.456.789-78"))
# print(validar_telefone("(84) 92165-1336"))
# print(transformar_hash("123.456.789-65"))