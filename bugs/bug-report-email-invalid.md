# Relatório de Bug: Campo de e-mail aceita valores inválidos

## Projeto  
Projeto Loja TesteFácil

## Descrição do Bug  
O campo de entrada do e-mail no formulário de login está aceitando valores que não seguem o formato padrão de e-mail (exemplo: "teste123"), permitindo que o usuário tente fazer login com dados inválidos.

## Passos para Reproduzir  
1. Acessar a tela de login.  
2. Inserir um e-mail inválido, como "teste123".  
3. Inserir uma senha qualquer.  
4. Clicar no botão "Entrar".

## Resultado Esperado  
- Validação do formato do e-mail antes do envio.  
- Exibir mensagem "E-mail inválido" e impedir o envio do formulário.

## Resultado Atual  
- O sistema aceita o e-mail inválido e tenta o login, retornando "Usuário ou senha inválidos", o que pode confundir o usuário.

## Ambiente de Teste  
- Navegador: Google Chrome versão 120 (fictícia)  
- Sistema operacional: Windows 10  
- Ambiente: Loja TesteFácil (teste)

## Prioridade  
Média

---

*Relatório elaborado por Fábio Rodrigues*
