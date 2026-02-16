# 📈 Smart Asset Allocation: Simulador de FIIs

![Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Finance](https://img.shields.io/badge/Financial_Engineering-Smart_Money-gold?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Finalizado-success?style=for-the-badge)

## 🌐 Visão Geral

Este repositório contém uma ferramenta de **Simulação e Alocação de Ativos** focada em Fundos de Investimento Imobiliários (FIIs). O projeto resolve a principal dor do investidor iniciante: *"Quanto e onde investir?"* utilizando parâmetros baseados em perfis de risco e capacidade financeira real (salário).

Desenvolvido como o projeto final do curso de Excel da **DIO**, este simulador aplica conceitos de porcentagem, lógica de decisão e estruturação de dados para automação financeira.

---

## 🚀 Funcionalidades Técnicas

### 1. ⚙️ Engine de Configurações
O sistema processa o salário base e sugere automaticamente uma reserva de 30% para investimentos, calculando o aporte mensal de forma dinâmica.
* **Parâmetro de Rendimento:** Baseado em uma taxa conservadora de 0,6% ao mês para simulação de fluxo de caixa passivo.

### 2. 🛡️ Alocação por Perfil (Asset Allocation)
A planilha utiliza uma tabela de apoio inteligente (`tbl_apoio`) que distribui os recursos entre diferentes classes de FIIs:
* **Tijolo:** Foco em imóveis físicos.
* **Papel:** Foco em recebíveis imobiliários (CRIs).
* **Híbridos & FOFs:** Diversificação em outros fundos e estratégias mistas.

### 3. 📊 Dinâmica de Risco
O simulador altera as porcentagens de alocação conforme o perfil selecionado (Conservador, Moderado, Arrojado), garantindo que a carteira esteja alinhada ao apetite de risco do usuário.

---

## 📁 Estrutura do Arquivo

| Aba / Seção | Função |
| :--- | :--- |
| **DIO_INVEST** | Dashboard principal para inserção de dados (salário) e visualização de resultados. |
| **TBL_APOIO** | Banco de dados com as chaves de perfil e as porcentagens de distribuição por categoria. |

---
> "Um bom algoritmo financeiro não prevê o futuro, ele prepara você para qualquer um deles."