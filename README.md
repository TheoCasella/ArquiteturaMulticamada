# 📚 Livraria Digital - Exercício de Arquitetura Multicamada

Este projeto é um protótipo de uma Livraria Digital desenvolvido para o exercício de Engenharia de Software. O objetivo principal foi refatorar um MVP (Produto Mínimo Viável) com arquitetura MVC para uma **Arquitetura Multicamada (N-Tier)** de 4 níveis, garantindo a separação de preocupações e integridade dos dados.

## 🏗️ Arquitetura do Projeto

O sistema foi dividido em 4 camadas distintas dentro do diretório `src/`, seguindo o fluxo de dependência:



1.  **Apresentação (Presentation):** Responsável pelas rotas Flask e renderização da interface (HTML/JS).
2.  **Aplicação (Application):** Onde residem as regras de negócio e os serviços. Aqui é controlada a lógica de aplicação de descontos únicos.
3.  **Negócio (Domain):** Contém as entidades e definições de dados fundamentais do sistema.
4.  **Dados (Infrastructure):** Camada de persistência que gerencia o armazenamento dos dados (atualmente em memória).

## 🚀 Funcionalidades Implementadas

-   **Listagem de Livros:** Exibição dinâmica de títulos consumindo uma API interna.
-   **Sistema de Promoção (Idempotência):** Implementação de uma regra de negócio que permite a aplicação de 10% de desconto apenas uma vez.
-   **Interface Responsiva:** Desenvolvida com Tailwind CSS.
-   **Checkout com QR Code:** Geração de QR Code dinâmico para simulação de pagamento via PIX ao clicar em "Detalhes".
-   **Tratamento de Erros:** Pop-up informativo caso o usuário tente aplicar o desconto mais de uma vez.

## 🛠️ Tecnologias Utilizadas

-   **Linguagem:** Python 3.x
-   **Framework Web:** Flask
-   **Estilização:** Tailwind CSS
-   **Ícones:** FontAwesome
-   **API de Terceiros:** QRServer (para geração de QR Codes)

## 📦 Como Rodar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone <url-do-seu-repositorio>
    cd Exercicio_Arquitetura
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Linux/Mac:
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install flask
    ```

4.  **Execute a aplicação:**
    ```bash
    python app.py
    ```
5.  **Acesse no navegador:** `http://127.0.0.1:5000`

## 📄 Licença
Este projeto foi desenvolvido para fins educacionais na disciplina de Engenharia de Software.