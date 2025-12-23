# 📝 API To-Do List – Python & Flask

Esta é uma API REST simples para gerenciamento de tarefas (To-Do), desenvolvida em **Python** utilizando o **Flask**.  
O projeto tem como objetivo praticar os conceitos básicos de backend, rotas, métodos HTTP e consumo de API via Postman.

---

## 🚀 Funcionalidades

- Listar todas as tarefas
- Buscar uma tarefa por ID
- Criar uma nova tarefa
- Atualizar uma tarefa existente
- Excluir uma tarefa

---

## 🛠️ Tecnologias Utilizadas

- Python
- Flask
- Postman (para testes)

---

## 📌 Endpoints

### 🔹 Listar todas as tarefas
**GET** `/tarefas`

### 🔹 Buscar tarefa por ID
**GET** `/tarefas/<id>`

### 🔹 Criar nova tarefa
**POST** `/tarefas`

**Body (JSON):**
```json
{
  "tarefa": "Nova tarefa",
  "concluido": false
}
