# Projeto de Banco de Dados📚

# Funcionamento da API:

- Método ```exec_select_livro():```
  - /select/livro -- rota para consultar livro 

Ao executar o select na tabela ```lib.livros```, a consulta pode ser feita de duas maneiras: pelo id ou pelo título do livro, que irá retornar apenas as informações do livro correspondente àquele id ou título.

Exemplo de consultas pelo id e pelo titulo:
```
{
  "id_livro": 15
}
```
```
{
  "titulo": "O Código da Vinci"
}
```
Caso não seja passado nenhum parâmetro, será executado o comando ```Select *``` na tabela ```lib.livro``` e todo o conteúdo será exibido.

------
- Método ```exec_select_autor():```
  - /select/autor -- rota para consultar livro

Ao executar o select na tabela ```lib.autor```, a consulta deve ser feita passando dois parametros: primeiro nome e sobrenome, que irá retornar apenas as informações do autor correspondente.

Exemplo de consulta pelo nome e sobrenome:
```
{
  "primeiro_nome": "J.K.",
  "sobrenome": "Rowling"
}
```
Caso não seja passado nenhum parâmetro, será executado o comando ```Select *``` na tabela ```lib.autor``` e todo o conteúdo será exibido.

------
- Método ```exec_select_livro_premiacao():```
  - /select/livro_premiacao -- rota para consultar relacionamento

Ao executar o select na tabela ```lib.livro_premiacao```, a consulta pode ser feita de duas maneiras: pelo id do livro, que irá retornar o relacionamento daquele livro com uma premiação ou pelo id da premiacao, que irá retornar o relacionamento daquela premiação com 1 ou mais livro(s) na tabela.

Exemplo de consultas pelo id do livro e pelo id da premiacao:
```
{
    "id_livro": 2
}
```
```
{
    "id_premiacao": 1
}
```
Caso não seja passado nenhum parâmetro, será executado o comando ```Select *``` na tabela ```lib.livro_relacionamento``` e todo o conteúdo será exibido.

------

- Método ```exec_delete_livro():```
  - /delete/livro/<int:id_livro> -- rota para deletar um livro

Ao executar o delete na tabela ```lib.livro```, somente é preciso informar o id do livro pela rota. Por exemplo:
```
/delete/livro/5
```
------
- Método ```exec_delete_autor():```
  - /delete/autor/<int:id_autor> -- rota para deletar um autor

Ao executar o delete na tabela ```lib.autor```, somente é preciso informar o id do autor pela rota. Por exemplo:
```
/delete/autor/5
```
------
- Método ```exec_delete_livro_premiacao():```
  - /delete/livropremiacao -- rota para deletar um relacionamento

Ao executar o delete na tabela ```lib.livro_premiacao```, é preciso informar tanto o id do livro quanto o da premiacao. Por exemplo:
```
{
  "id_livro": 1
  "id_premiacao": 2
}
```
------
- Método ```exec_insert_livro():```
  - /insert/livro -- rota para inserir um livro

Ao executa o insert na tabela ```lib.livro``` é preciso preencher todos os campos necessários.
Exemplo de inserção:
```
{
  "id_livro": 20,
  "isbn": "123-456789",
  "titulo": "Titulo teste",
  "ano_publicacao": 2000,
  "sinopse": "Descrição do filmes",
  "id_autor": 5,
  "id_editora": 5
}
```
------
- Método ```exec_insert_autor():```
  - /insert/autor -- rota para inserir um autor

Ao executar o insert na tabela ```lib.autor``` é preciso preencher todos os campos necessários. Por exemplo:
```
{
  "id_autor": ,
  "primeiro_nome": "123-456789",
  "sobrenome": "Titulo teste",
  "nacionalidade": "Brasileiro",
  "sinopse": "Descrição do filmes",
  "id_autor": 5,
  "id_editora": 5
}
```
