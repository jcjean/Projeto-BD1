# Projeto de Banco de Dados📚

# Funcionamento da API:
- Método ```exec_select_livro(parametros)```

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
Caso não seja passado nenhum critério de filtragem, é executado o comando ```Select *``` na tabela ```lib.livro``` e todo o conteúdo é exibido.

- Método ```exec_select_autor(parametros):```

Ao executar o select na tabela lib.autor, a consulta pode ser feita de duas maneiras: pelo primeiro nome e sobrenome, que irá retornar apenas as informações do autor correspondente e sem nenhum parametro, que nesse caso será executado o comando ```Select *``` na tabela ```lib.autor```.

Exemplo de consulta pelo nome e sobrenome:
```
{
  "primeiro_nome": "J.K.",
  "sobrenome": "Rowling"
}
```
