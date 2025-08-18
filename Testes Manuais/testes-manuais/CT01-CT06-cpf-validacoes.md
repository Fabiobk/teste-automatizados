# Testes Manuais – Validação de CPF (CT01 a CT06)

Este conjunto de testes cobre os principais cenários de validação do campo CPF em um formulário de cadastro.

---

##  CT01 – CPF em branco

**Entrada:**  
(vazio)

**Resultado Esperado:**  
Mensagem: **"CPF é obrigatório"**

---

## CT02 – CPF com menos de 11 dígitos

**Entrada:**  
123456789

**Resultado Esperado:**  
Mensagem: **"CPF deve conter 11 números"**

---

## CT03 – CPF com letras

**Entrada:**  
abc12345678

**Resultado Esperado:**  
Mensagem: **"CPF deve conter apenas números"**

---

## CT04 – CPF com caracteres especiais

**Entrada:**  
123.456.789-09

**Resultado Esperado:**  
Mensagem: **"CPF deve conter apenas números"**

---

##  CT05 – CPF inválido (com 11 números)

**Entrada:**  
12345678900

**Resultado Esperado:**  
Mensagem: **"CPF inválido"**

---

## CT06 – CPF válido

**Entrada:**  
52998224725

**Resultado Esperado:**  
Mensagem: **"Cadastro realizado com sucesso"**

---

**Status:**  
Todos os testes foram executados manualmente no Jira e passaram conforme o esperado.  
**Ferramenta:** Jira  
**Data:** 29/07/2025

**Observações:**  
Esses testes foram executados com foco em validação de dados de entrada no campo CPF, considerando regras comuns de sistemas brasileiros.

---

**Autor:** Fábio Rodrigues  
Iniciante em QA Manual | Explorando testes de software com base em projetos reais
