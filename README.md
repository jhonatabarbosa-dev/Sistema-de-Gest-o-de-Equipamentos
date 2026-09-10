# 📦 Gestão de Ativos & Equipamentos

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

Sistema web desenvolvido em Python e Django para controle e gestão de equipamentos de empresas.

---

## 📋 Funcionalidades Principais

- 📊 **Painel de Controle (Dashboard):** Visualização centralizada do inventário com suporte a identificação rápida por ID, Patrimônio e Status.
- ➕ **Cadastro de Equipamentos:** Formulário padronizado com formulários Django para inclusão de novos ativos.
- 🔍 **Detalhes do Ativo:** Exibição dinâmica de especificações e status do equipamento via rotas parametrizadas (`/equipamento/<id>`).
- 🏷️ **Indicadores de Status:** Badges visuais que sinalizam disponibilidade (*Disponível* ou *Em Uso*).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Framework Web:** Django
- **Banco de Dados:** SQLite
- **Frontend:** HTML5, Bootstrap 5, Django Template Language (DTL)
- **Ambiente:** VS Code DevContainer / GitHub Codespaces

---

## 📐 Arquitetura do Sistema (MVT)

'
       [ Requisição HTTP (Navegador) ]
                     │
                     ▼
             ┌───────────────┐
             │    urls.py    │ (Roteamento de URLs)
             └───────┬───────┘
                     │
                     ▼
             ┌───────────────┐
             │   views.py    │ (Regra de Negócio & Lógica)
             └───────┬───────┘
            ┌────────┴────────┐
            ▼                 ▼
   ┌────────────────┐ ┌───────────────┐
   │   models.py    │ │  templates/   │
   │  (Equipamento) │ │ (lista.html,  │
   └───────┬────────┘ │ cadastro.html,│
           │          │ detalhes.html)│
           ▼          └───────┬───────┘
   ┌────────────────┐         │
   │   db.sqlite3   │         │
   └────────────────┘         │
            │                 │
            └────────┬────────┘
                     ▼
       [ Resposta HTML Renderizada ]

---

## 💻 Como Executar o Projeto Localmente

1. **Clone o repositório:**
   bash
   git clone [https://github.com/jhonatabarbosa-dev/Sistema-de-Gest-o-de-Equipamentos.git](https://github.com/jhonatabarbosa-dev/Sistema-de-Gest-o-de-Equipamentos.git)
   cd Sistema-de-Gest-o-de-Equipamentos

Execute as migrações do banco de dados:

Bash
python manage.py migrate


Inicie o servidor de desenvolvimento:

Bash
python manage.py runserver

Acesse http://127.0.0.1:8000/ no navegador.
