# Casos de Teste – Projeto Login

## CT01 – Login com dados válidos

**Passos:**
1. Acessar: https://practicetestautomation.com/practice-test-login/
2. Usuário: `student`
3. Senha: `Password123`
4. Clicar em Submit

**Resultado Esperado:** Página de sucesso com mensagem “Congratulations”

## CT02 – Login com dados inválidos

**Passos:**
1. Usuário: `student`
2. Senha: `errado123`
3. Clicar em Submit

**Resultado Esperado:** Mensagem de erro “Your password is invalid!”

## CT03 – Erro genérico com múltiplos erros

**Passos:**
1. Usuário: `admin`
2. Senha: `123456`
3. Clicar em Submit

**Resultado Esperado:** Deveria exibir múltiplas mensagens
**Resultado Obtido:** Mensagem genérica → Falta clareza para o usuário
