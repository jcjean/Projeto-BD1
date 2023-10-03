import psycopg2
from connectbd import bd_config

def exec_select_livro(parametros):
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        titulo = parametros.get('titulo')
        id_livro = parametros.get('id_livro')

        # consulta SQL com base nos parâmetros fornecidos
        if not titulo and not id_livro:
            cursor.execute("SELECT * FROM lib.livro ORDER BY id_livro")
        elif titulo:
            cursor.execute("SELECT id_livro, isbn, titulo, ano_publicacao, sinopse, id_autor, id_editora FROM lib.livro WHERE titulo = %s", (titulo,))
        elif id_livro:
            cursor.execute("SELECT id_livro, isbn, titulo, ano_publicacao, sinopse, id_autor, id_editora FROM lib.livro WHERE id_livro = %s", (id_livro,))
        results = cursor.fetchall()

        if results:
            # Formatando os resultados com as especificações dos campos da tabela
            formatted_results = []
            for result in results:
                id_livro, isbn, titulo, ano_publicacao, sinopse, id_autor, id_editora = result
                formatted_result = {
                    "id_livro": id_livro,
                    "isbn": isbn,
                    "titulo": titulo,
                    "ano_publicacao": ano_publicacao,
                    "sinopse": sinopse,
                    "id_autor": id_autor,
                    "id_editora": id_editora
                }
                formatted_results.append(formatted_result)
            
            return formatted_results
        else:
            return None  # Nenhum resultado encontrado
    except psycopg2.Error as e:
        print("Erro na consulta:", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()

def exec_select_autor(parametros): 
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        primeiro_nome = parametros.get('primeiro_nome')
        sobrenome = parametros.get('sobrenome')

        # consulta na tabela autor
        if not primeiro_nome and not sobrenome:
            cursor.execute("SELECT * FROM lib.autor ORDER BY id_autor")
        elif (primeiro_nome and sobrenome):
            cursor.execute("SELECT id_autor, primeiro_nome, sobrenome, nacionalidade FROM lib.autor WHERE primeiro_nome = %s AND sobrenome = %s", (primeiro_nome, sobrenome,))
        results = cursor.fetchall()

        if results:
            # Formatando os resultados com as especificações dos campos da tabela
            formatted_results = []
            for result in results:
                id_autor, primeiro_nome, sobrenome, nacionalidade = result
                formatted_result = {
                    "id_autor": id_autor,
                    "primeiro_nome": primeiro_nome,
                    "sobrenome": sobrenome,
                    "nacionalidade": nacionalidade,
                }
                formatted_results.append(formatted_result)

        return formatted_results
    except psycopg2.Error as e:
        print("Erro na consulta:", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()

def exec_select_livro_premiacao(parametros): 
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        id_premiacao = parametros.get('id_premiacao')
        id_livro = parametros.get('id_livro')

        # consulta na tabela de relacionamento livro_premiacao
        if not id_premiacao and not id_livro:
            cursor.execute("SELECT * FROM lib.livro_premiacao")
        elif id_premiacao:
            cursor.execute("SELECT id_livro, id_premiacao, data_premiacao FROM lib.livro_premiacao WHERE id_premiacao = %s", (id_premiacao,))
        elif id_livro:
            cursor.execute("SELECT id_livro, id_premiacao, data_premiacao FROM lib.livro_premiacao WHERE id_livro = %s", (id_livro,))
        results = cursor.fetchall()

        if results:

            formatted_results = []
            for result in results:
                id_livro, id_premiacao, data_premiacao = result
                formatted_result = {
                    "id_livro": id_livro,
                    "id_premiacao": id_premiacao,
                    "data_premiacao": data_premiacao,
                }
                formatted_results.append(formatted_result)

        return formatted_results
    except psycopg2.Error as e:
        print("Erro na consulta:", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()