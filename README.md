# Sistema de Cadastro e Verificação de Login em Python


Projeto em Python que implementa um sistema simples de cadastro e login com validação de dados usando Regex, armazenamento em JSON e proteção de senhas com hash SHA-256.

O foco do projeto é aplicar boas práticas iniciais de back-end, como:

- separação de módulos
- validação de entrada
- persistência de dados
- segurança básica de senhas

---

## Funcionalidades 

- validação de email com Regex
- validação de CPF no formato **XXX.XXX.XXX-XX**
- validação de telefone no formato **(DD) XXXXX-XXXX**
- criptografia de senha usando SHA-256
- armazenamento dos usuários em arquivo JSON
- sistema de login com verificação de senha criptografada

---

```
## Estrutura do projeto

CADASTRO_VERIFICACAO_LOGIN/
│
├── funcoes/
│   ├── arquivosjson.py      # Leitura, escrita e cadastro no JSON
│   ├── funcoesregex.py      # Validações com Regex + login
│   ├── transformhash.py     # Criptografia da senha
│   └── menu.py              # Exibição do menu
│
├── dados_pessoas.json       # Banco de dados em JSON
├── main.py                  # Arquivo principal do sistema
├── README.md                # Documentação do projeto
└── .gitignore
```

---

## Tecnologias Utilizadas 

- Python 3
- Regex(`re`)
- JSON
- Hashlib (SHA-256)

---

## Como funciona 

### Cadastro

1. O usuário informa:
    - email
    - CPF
    - telefone
    - senha
2. Todos os dados passam por validação com Regex.
3. A senha é convertida em hash SHA-256.
4. Os dados são armazenados no arquivo **dados_pessoas.json**.

### Login

1. O usuário informa o email.
2. Se o email existir:
    - a senha digitada é criptografada
    - o hash é comparado com o salvo no JSON
3. Se coincidir → login realizado com sucesso

---

## Como executar

1. Clone o repositório: 
```

git clone https://github.com/Miguel-Marquess/basic-user-auth-python.git

```

2. Entre na pasta do projeto

3. Execute o sistema:

```
python main.py
```

---

## Segurança 

- as senhas não são armazenadas em texto puro
- é utilizado o algoritmo SHA-256
- Projeto com foco didático

---

## Objetivo do projeto

- treinar lógica de programação 
- praticar organização de código
- aplicar conceitos iniciais de back-end

---

***Projeto desenvolvido pensando puramente no aprendizado.***