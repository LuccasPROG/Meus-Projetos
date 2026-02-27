# 📝 Lista de Tarefas com Desfazer e Refazer

Projeto simples em Python que simula uma lista de tarefas com sistema de:

- ✅ Adicionar tarefas
- 📋 Listar tarefas
- ↩️ Desfazer última ação
- ↪️ Refazer ação desfeita
- 💾 Salvamento automático em arquivo JSON

---

## 🚀 Tecnologias utilizadas

- Python 3
- Módulo `json`
- Manipulação de arquivos
- Estruturas de lista

---

## 📂 Como funciona

O sistema mantém duas listas:

- `lista_de_tarefas`
- `lista_de_desfazer`

Quando você:

### ➕ Adiciona uma tarefa
Ela é salva na lista principal e persistida no arquivo `tarefas.json`.

### ↩️ Desfaz
Remove o último item da lista principal e envia para a lista de desfazer.

### ↪️ Refaz
Retorna o último item desfeito para a lista principal.

Todas as alterações são automaticamente salvas no arquivo JSON.

---

## ▶️ Como executar

1. Clone o repositório:

```bash
git clone <url-do-repositorio>