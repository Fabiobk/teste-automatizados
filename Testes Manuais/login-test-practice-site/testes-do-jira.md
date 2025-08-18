# Casos de Teste Criados no Jira – Login do site Practice Test Automation

## CT01 – Login com dados válidos

**ID Jira:** QA-01  
**Status:** ✅ Concluído  
**Descrição:** Validar login com credenciais corretas.

**Passos:**
1. Acessar: https://practicetestautomation.com/practice-test-login/
2. Usuário: `student`
3. Senha: `Password123`
4. Clicar em “Submit”

**Resultado Esperado:** Acesso à página com mensagem “Congratulations”
**Resultado Obtido:** Conforme esperado

---

## CT02 – Login com dados inválidos

**ID Jira:** QA-02  
**Status:** ✅ Concluído  
**Descrição:** Verificar o comportamento do sistema com senha incorreta.

**Passos:**
1. Usuário: `student`
2. Senha: `errado123`
3. Clicar em Submit

**Resultado Esperado:** Mensagem de erro clara
**Resultado Obtido:** Exibe “Your password is invalid!”

---

## CT03 – Mensagem de erro genérica

**ID Jira:** QA-03  
**Status:** ✅ Concluído  
**Descrição:** Validar a clareza das mensagens de erro ao inserir usuário e senha incorretos.

**Passos:**
1. Usuário: `admin`
2. Senha: `123456`
3. Clicar em Submit

**Resultado Esperado:** Mensagem de erro que mostre ambos os campos incorretos
**Resultado Obtido:** Mensagem genérica apenas do campo de usuário → Pode confundir o usuário
