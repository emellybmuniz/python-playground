# 🏦 Sistema Bancário Modularizado | Modularized Banking System 

## 🇧🇷 Português

### 📋 Descrição do Desafio
O objetivo deste projeto é refatorar um sistema bancário existente para aumentar a modularidade e a manutenibilidade do código. A nova versão (v2) organiza as operações de **saque**, **depósito** e **extrato** em funções específicas e introduz novas funcionalidades para o cadastro de **usuários** (clientes) e **contas correntes**.

### 🚀 Funcionalidades e Regras

1.  **Separação em Funções**: Todas as operações devem ser encapsuladas em funções.
2.  **Saque (`sacar`)**:
    * Deve receber argumentos apenas por **nome** (*keyword only*).
    * Sugestão de argumentos: `saldo`, `valor`, `extrato`, `limite`, `numero_saques`, `limite_saques`.
    * Retorno: `saldo` e `extrato`.
3.  **Depósito (`depositar`)**:
    * Deve receber argumentos apenas por **posição** (*positional only*).
    * Sugestão de argumentos: `saldo`, `valor`, `extrato`.
    * Retorno: `saldo` e `extrato`.
4.  **Extrato (`exibir_extrato`)**:
    * Deve receber argumentos por **posição e nome** (*positional and keyword*).
    * Argumentos posicionais: `saldo`.
    * Argumentos nomeados: `extrato`.
5.  **Novas Funções de Cadastro**:
    * **Criar Usuário**: Armazena nome, data de nascimento, CPF (apenas números, deve ser único) e endereço (string formatada: "logradouro, nro - bairro - cidade/sigla estado").
    * **Criar Conta Corrente**: Vincula uma conta a um usuário. Composta por agência (fixo "0001"), número da conta (sequencial iniciando em 1) e usuário. Um usuário pode ter várias contas.

---

## 🇺🇸 English

### 📋 Challenge Description
The goal of this project is to refactor an existing banking system to improve code modularity and maintainability. The new version (v2) organizes **withdrawal**, **deposit**, and **statement** operations into specific functions and introduces new features for registering **users** (clients) and **current accounts**.

### 🚀 Features and Rules

1.  **Function Separation**: All operations must be encapsulated within functions.
2.  **Withdraw (`sacar`)**:
    * Must receive arguments by **keyword only**.
    * Suggested arguments: `saldo` (balance), `valor` (amount), `extrato` (statement), `limite` (limit), `numero_saques` (withdrawal_count), `limite_saques` (withdrawal_limit).
    * Return: `saldo` and `extrato`.
3.  **Deposit (`depositar`)**:
    * Must receive arguments by **position only**.
    * Suggested arguments: `saldo`, `valor`, `extrato`.
    * Return: `saldo` and `extrato`.
4.  **Statement (`exibir_extrato`)**:
    * Must receive arguments by **position and keyword**.
    * Positional arguments: `saldo`.
    * Keyword arguments: `extrato`.
5.  **New Registration Functions**:
    * **Create User**: Stores name, date of birth, CPF (numbers only, must be unique), and address (formatted string: "street, number - neighborhood - city/state abbreviation").
    * **Create Current Account**: Links an account to a user. Composed of agency (fixed "0001"), account number (sequential starting at 1), and user. A user can have multiple accounts.