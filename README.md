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
- ➕ **Cadastro de Equipamentos:** Formulário padronizado com Django Forms para inclusão de novos ativos.
- 🔍 **Detalhes do Ativo:** Exibição dinâmica de especificações e status do equipamento via rotas parametrizadas (`/equipamento/<id>`).
- 🏷️ **Indicadores de Status:** Badges visuais que sinalizam disponibilidade (*Disponível* ou *Em Uso*).

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Framework Web:** Django
- **Banco de Dados:** SQLite3
- **Frontend:** HTML5, Bootstrap 5, Django Template Language (DTL)
- **Ambiente:** VS Code DevContainer / GitHub Codespaces

---

## 📐 Arquitetura do Sistema (MVT)

```mermaid
graph TD
    A[Requisicao HTTP - Navegador] --> B[urls.py - Roteamento]
    B --> C[views.py - Regra de Negocio & Logica]
    C --> D[models.py - Equipamentos]
    C --> E[templates/ - HTML + Bootstrap]
    D --> F[(db.sqlite3)]
    E --> G[Resposta HTML Renderizada]
