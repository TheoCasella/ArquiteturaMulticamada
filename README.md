# Arquitetura Multicamada em Python

Este projeto demonstra a implementação de uma **Arquitetura Multicamada (N-Tier)**, focada na separação de responsabilidades, facilidade de manutenção e testabilidade através do uso de **Interfaces** e **Injeção de Dependência**.

---

## 🏗️ Estrutura do Projeto
O projeto está dividido em quatro camadas principais, seguindo o fluxo de comunicação definido:

### 1. Apresentação (`/Apresentacao`)
* **Responsabilidade:** Interface com o usuário/sistema externo.
* **Conteúdo:** Controllers e rotas da API.
* **Fluxo:** Recebe a requisição e aciona a camada de **Negócio**.

### 2. Negócio (`/Negocio`)
* **Responsabilidade:** Contém as regras de negócio e a lógica da aplicação.
* **Conteúdo:** `Services`.
* **Diferencial:** Não sabe de onde os dados vêm. Ela depende apenas de uma **Interface** definida na camada de Dados.

### 3. Dados (`/Dados`)
* **Responsabilidade:** Define o contrato de persistência e a implementação real.
* **Conteúdo:** * `IRepositorioLivro`: Classe abstrata (Interface) que define os métodos obrigatórios.
    * `LivroRepository`: Implementação voltada para um banco de dados real (MySQL/SQLite).

### 4. Stub (`/Stub`)
* **Responsabilidade:** Simulação de persistência para desenvolvimento e testes.
* **Conteúdo:** `LivroRepositoryStub`.
* **Uso:** Permite rodar o projeto inteiramente em memória, sem necessidade de configurar um banco de dados externo.

---

## 🔄 Fluxo de Dados
A comunicação entre as camadas é bem definida para evitar o acoplamento:

> **Apresentação** ➔ **Negócio (Service)** ➔ **Interface (Dados)** ➔ **Implementação (Stub ou Real)**

---

## 🛠️ Tecnologias e Conceitos Aplicados
* **Python 3.x**
* **Inversão de Dependência:** O Service recebe o repositório no construtor, permitindo trocar o Banco Real pelo Stub facilmente.
* **Classes Abstratas (abc):** Garantia de que todos os repositórios sigam o mesmo padrão de métodos.

---

## 🚀 Como executar
1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/TheoCasella/ArquiteturaMulticamada.git](https://github.com/TheoCasella/ArquiteturaMulticamada.git)