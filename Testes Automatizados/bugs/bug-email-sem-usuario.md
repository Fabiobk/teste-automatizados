# Bug: Campo de e-mail aceita valor sem nome de usuário (@gmail.com)
Passos para reproduzir
1. Acesse o formulário
2. Digite `@gmail.com`
3. Clique em “Enviar”
Resultado atual
- Formulário é enviado sem erro
 Resultado esperado
- Exibir: "E-mail inválido"
- Bloquear envio

Sugestão de correção
- Validar presença de texto antes do `@`
- Exibir mensagem amigável ao usuário

 Relacionado a
- Caso de Teste: CT-01 – Validação do campo de e-mail
