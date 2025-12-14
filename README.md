# 🍲 API de Receitas Culinárias

## 📌 Descrição

Esta API REST foi desenvolvida com **Flask** como parte da atividade de Desenvolvimento de API. O objetivo do projeto é gerenciar receitas culinárias, permitindo criar, listar, atualizar e remover receitas utilizando os métodos HTTP.

Os dados são armazenados **em memória** (lista de dicionários), sem uso de banco de dados.

---

## 🚀 Tecnologias Utilizadas

* Python 3
* Flask
* Git e GitHub

---

## ▶️ Como executar o projeto

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/api-receitas-culinarias.git
```

### 2️⃣ Acesse a pasta do projeto

```bash
cd api-receitas-culinarias
```

### 3️⃣ Instale o Flask

```bash
pip install flask
```

### 4️⃣ Execute a aplicação

```bash
python app.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

---

## 📚 Estrutura do Projeto

```
api-receitas-culinarias/
│
├── app.py
└── README.md
```

---

## 🔗 Endpoints da API

### 🏠 GET /

Retorna uma mensagem inicial da API.

**Resposta:**

```json
{
  "mensagem": "API de Receitas Culinárias"
}
```

---

### 📥 GET /receitas

Lista todas as receitas cadastradas.

---

### 🔍 GET /receitas/{id}

Busca uma receita pelo ID.

---

### ➕ POST /receitas

Cadastra uma nova receita.

**Exemplo de JSON:**

```json
{
  "nome": "Panqueca",
  "ingredientes": ["leite", "ovo", "farinha"],
  "modo_preparo": "Misture tudo e frite."
}
```

---

### ✏️ PUT /receitas/{id}

Atualiza uma receita existente.

**Exemplo de JSON:**

```json
{
  "nome": "Panqueca Doce"
}
```

---

### ❌ DELETE /receitas/{id}

Remove uma receita pelo ID.

---

## 🧪 Testes

A API pode ser testada utilizando ferramentas como:

* Postman
* Insomnia
* Thunder Client (VS Code)

---

## 👩‍🎓 Contexto Acadêmico

Projeto desenvolvido para a disciplina de **Desenvolvimento de APIs com Flask**, com o objetivo de praticar:

* Rotas HTTP
* Métodos GET, POST, PUT e DELETE
* Versionamento com Git

---

## ✍️ Autora

**Evelyn da Silva**

---

✅ Projeto concluído e versionado no GitHub.
