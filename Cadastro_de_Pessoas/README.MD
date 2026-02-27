# 📋 Sistema de Cadastro de Pessoas em Python

Projeto simples desenvolvido em Python que simula um sistema de cadastro de pessoas utilizando arquivo `.txt` para armazenamento de dados.

O sistema roda em modo console e permite cadastrar e listar pessoas de forma organizada.

---

## 🚀 Funcionalidades

- 📄 Ver pessoas cadastradas  
- ➕ Cadastrar nova pessoa  
- 📁 Criação automática do arquivo caso não exista  
- 🔢 Validação de idade (aceita apenas números válidos)  
- 🚪 Sair do sistema  

---

## 🧠 Conceitos praticados

- Modularização com pacotes (`lib.interface` e `lib.arquivo`)  
- Manipulação de arquivos `.txt`  
- Estruturas condicionais (`if`, `elif`, `else`)  
- Laço de repetição `while`  
- Funções  
- Tratamento de erros  
- Organização de código em módulos  

---

## 📂 Estrutura do Projeto


projeto/
│
├── cadastro.txt
├── main.py
│
└── lib/
├── interface.py
└── arquivo.py


---

## ⚙️ Como funciona

### 📁 Arquivo de Dados

O sistema utiliza um arquivo chamado:


cadastro.txt


Se o arquivo não existir, ele é criado automaticamente ao iniciar o sistema.

---

### 📌 Menu Interativo

O usuário pode escolher entre:

1. Ver pessoas cadastradas  
2. Cadastrar nova pessoa  
3. Sair do sistema  

---

### ➕ Cadastro

Ao cadastrar uma pessoa, o sistema solicita:

- Nome  
- Idade (com validação numérica)  

Os dados são armazenados no arquivo `cadastro.txt`.

---

## ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git

Entre na pasta:

cd nome-do-repositorio

Execute o sistema:

python main.py
🎯 Objetivo do Projeto

Este projeto foi criado para praticar:

Organização de código em módulos

Persistência de dados sem banco de dados

Desenvolvimento de sistemas simples em Python

Construção de base sólida para projetos maiores


---

Agora sim 👏  

Você cola isso dentro de um arquivo chamado:


README.md


Salva.

Depois no terminal:

```bash
git add README.md
git commit -m "Adicionando README"
git push