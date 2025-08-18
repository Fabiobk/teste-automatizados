# CT-01 – Validação do Campo de E-mail

## Objetivo
Verificar o comportamento do campo de e-mail no formulário de contato.

---

## Cenários de Teste

### Cenário 1 – Campo de e-mail obrigatório
- Passos:
  1. Acesse: https://www.seusite.com/formulario
  2. Deixe o campo e-mail em branco
  3. Clique em “Enviar”
- Resultado esperado: "Campo de e-mail obrigatório"

---

### Cenário 2 – E-mail inválido (sem domínio)
- Entrada: `teste@email`
- Resultado esperado: "E-mail inválido"

---

### ❌ Cenário 3 – E-mail inválido (sem usuário)
- Entrada: `@gmail.com`
- Resultado esperado: "E-mail inválido"
- Resultado obtido: Formulário foi enviado sem erro

➡️ **Bug criado:** [`bug-email-sem-usuario.md`](../bugs/bug-email-sem-usuario.md)

---

### Cenário 4 – E-mail válido
- Entrada: `usuario@dominio.com`
- Resultado esperado: Formulário enviado com sucesso
