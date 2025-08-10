# ✈️ Sistema de Reserva de Assentos Aéreos

> Uma aplicação web simples para simular a reserva de assentos em um voo, construída com Python e o microframework Flask.

![Demonstração da Aplicação Web](https://i.imgur.com/JzUnQc5.gif)
<!-- Sugestão: Grave um GIF da sua aplicação funcionando e substitua o link acima -->

---

## 📝 Sobre o Projeto

Este projeto, desenvolvido como parte dos estudos em Algoritmos e desenvolvimento web, simula um sistema de reserva de assentos para uma aeronave. A aplicação web permite que o usuário visualize um mapa de assentos em tempo real e interaja com ele para marcar ou desmarcar lugares.

O backend foi construído com **Python** e **Flask**, gerenciando o estado dos assentos em memória. O frontend utiliza um template **HTML** com **Jinja2** para renderizar dinamicamente o mapa de assentos, aplicando CSS para diferenciar visualmente os assentos livres e ocupados.

---

## ✨ Funcionalidades

* **Visualização do Mapa de Assentos:** Exibe uma grade completa de 6 fileiras por 30 colunas, representando todos os assentos da aeronave.
* **Feedback Visual em Tempo Real:** Assentos livres são exibidos em verde (`livre`) e assentos ocupados em vermelho (`ocupado`), com a página sendo atualizada após cada ação.
* **Marcar Assento:** Um formulário permite ao usuário inserir a fileira e a coluna para ocupar um assento.
* **Desmarcar Assento:** Um segundo formulário permite desocupar um assento previamente marcado.
* **Validação Simples:** O backend processa as requisições, atualiza o estado do mapa de assentos e redireciona o usuário de volta para a visualização principal.

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** [Python](https://www.python.org/)
* **Framework Web:** [Flask](https://flask.palletsprojects.com/en/3.0.x/)
* **Template Engine:** [Jinja2](https://jinja.palletsprojects.com/en/3.1/)
* **Frontend:** HTML5 e CSS3
* **Versionamento:** [Git](https://git-scm.com/)

---

## ▶️ Como Executar o Projeto

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
* [Git](https://git-scm.com)
* [Python 3.9+](https://www.python.org/downloads/)
* `pip` (geralmente vem com a instalação do Python)

### Rodando a Aplicação Web

```bash
# 1. Clone este repositório
$ git clone [https://github.com/marinho-marcos/sistema-assentos-aviao](https://github.com/marinho-marcos/sistema-assentos-aviao)

# 2. Acesse a pasta do projeto no terminal/cmd
$ cd sistema-assentos-aviao

# 3. Crie e ative um ambiente virtual
# No Windows
$python -m venv venv$ .\\venv\\Scripts\\activate
# No Linux/Mac
$python3 -m venv venv$ source venv/bin/activate

# 4. Instale as dependências do projeto listadas no requirements.txt
$ pip install -r requirements.txt

# 5. Execute a aplicação Flask
$ python app.py

# 6. Abra seu navegador e acesse a URL abaixo:
[http://127.0.0.1:5000](http://127.0.0.1:5000)
