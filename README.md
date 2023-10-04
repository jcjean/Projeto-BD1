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

Ao executar o delete na tabela ```lib.livro```, somente é preciso informar o id do livro pela rota. 

Por exemplo:
```
/delete/livro/5
```
------
- Método ```exec_delete_autor():```
  - /delete/autor/<int:id_autor> -- rota para deletar um autor

Ao executar o delete na tabela ```lib.autor```, somente é preciso informar o id do autor pela rota. 

Por exemplo:
```
/delete/autor/5
```
------
- Método ```exec_delete_livro_premiacao():```
  - /delete/livropremiacao -- rota para deletar um relacionamento

Ao executar o delete na tabela ```lib.livro_premiacao```, é preciso informar tanto o id do livro quanto o da premiacao. 

Por exemplo:
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

Exemplo de inserção de um livro:
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

Ao executar o insert na tabela ```lib.autor``` é preciso preencher todos os campos necessários. 

Exemplo de inserção de um autor:
```
{
  "id_autor": 22,
  "primeiro_nome": "Teste",
  "sobrenome": "da Silva",
  "nacionalidade": "Brasileiro",
}
```
------
- Método ```exec_insert_livro_premiacao():```
  - /insert/livropremiado -- rota para inserir o livro, sua premiação e também a data da premiação

Ao executar o insert na tabela ```lib.livro_premiacao```, é preciso preencher todos os campos necessários.

Exemplo de inserção na tabela de relacionamento:
```
{
  "id_livro": 10,
  "id_premiacao": 2,
  "data_premiacao": "2023-01-01"",
}
```
------
- Método ```exec_update_livro():```
  - /update/livro/<int:id_livro> -- rota para atualizar dados do livro

Ao executar o update na tabela ```lib.livro```, é preciso informar, pela rota, o id do livro que será atualizado e informar os campos que serão atualizados.
Obs.: É preciso informar ao menos 1 campo para atualização.

Exemplos de um update no livro:
```
Rota: /update/livro/15

Campo que será atualizado:
{
    "sinopse": "Neste jogo mortal, Katniss Everdeen deve lutar pela sobrevivência em uma arena brutal enquanto o país assiste à carnificina."
}
```
```
Rota: /update/livro/20

Campos que serão atualizado:
{
  "titulo": "Novo titulo",
  "sinopse": "Nova descrição"
  "ano_publicacao": 2020
}
```
------
- Método ```exec_update_autor():```
  - /update/autor/<int:id_autor> -- rota para atualizar dados do autor

Ao executar o update na tabela ```lib.autor```, é preciso informar, pela rota, o id do autor que será atualizado e informar os campos que serão atualizados.
Obs.: É preciso informar ao menos 1 campo para atualização.

Exemplos de um update no autor:
```
Rota: /update/autor/22

Campo que será atualizado:
{
   "nacionalidade": "Brasileira",
}
```
```
Rota: /update/autor/22

Campos que serão atualizado:
{
  "primeiro_nome": "Teste",
  "sobrenome": "da Silva",
}
```
- Método ```exec_update_livro_premiacao():```
  - /update/livropremiacao/<int:id_livro>/<int:id_premiacao> -- rota para atualizar dados do livro premiado

Ao executar o update na tabela ```lib.livro_premiacao```, é preciso informar, pela rota, o id do livro e o id da premiacao. Para atualizar esse relacionamento é preciso informar os campos que serão atualizados.
Obs.: É preciso informar ao menos 1 campo para atualização.

Exemplos de um update no livro premiado:
```
Rota: /update/livropremiacao/10/2

Campo que será atualizado:
{
    "id_premiacao": 1
}
```
```
Rota: /update/livropremiacao/10/1

Campos que serão atualizado:
{
  "id_livro": 10,
  "id_premiacao": 2,
  "data_premiacao": "2012-02-01"",
}
```
------
