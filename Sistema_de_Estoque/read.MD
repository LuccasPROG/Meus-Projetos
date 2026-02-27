# 📦 Sistema de Controle de Estoque em Python

Projeto simples em Python executado via terminal para gerenciamento básico de estoque.

Permite cadastrar produtos, validar dados e visualizar informações armazenadas.

---

## 🚀 Tecnologias utilizadas

- Python 3
- Listas
- Dicionários
- Funções
- Estruturas de repetição
- Validação de dados

---

## 📋 Funcionalidades

### 1️⃣ Cadastrar Produto

- Solicita nome, preço, quantidade e código
- Não permite preço negativo
- Não permite quantidade negativa
- Impede cadastro com código duplicado

### 2️⃣ Calcular Total de Produtos em Estoque

- Soma a quantidade de todos os produtos cadastrados
- Exibe o total armazenado

### 3️⃣ Mostrar Produtos

- Lista todos os produtos cadastrados
- Exibe nome, preço, quantidade e código

### 4️⃣ Sair

- Encerra o sistema

---

## 🛠️ Estrutura de Dados

O estoque é representado por uma lista:

```python
estoque = []

Cada produto é armazenado como um dicionário:

{
    "nome": "Produto A",
    "preco": 10.0,
    "quantidade": 5,
    "codigo": 101
}
▶️ Como executar
git clone <url-do-repositorio>
cd nome-da-pasta
python nome_do_arquivo.py
🎯 Objetivo do Projeto

Este projeto foi desenvolvido para praticar:

Lógica de programação

Estruturas de dados

Validação de entrada

Organização de código