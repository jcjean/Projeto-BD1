# Projeto de Banco de Dados📚

# Funcionamento da API:
- Método ```select_livro():```

Ao executar o select na tabela lib.livros, a consulta pode ser feita de duas maneiras: pelo id do livro, que irá retornar apenas as informações do livro referente àquele id.

Exemplo de consulta pelo id do livro:
```
{
  "id_livro": 15
}
```
Exemplo de consulta pelo título do livro:
```
{
  "titulo": "O Código da Vinci"
}
```
