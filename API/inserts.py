import psycopg2
from connectbd import bd_config

def exec_insert_autor(id_autor, primeiro_nome, sobrenome, nacionalidade):
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # Insere um novo autor na tabela 
        cursor.execute("INSERT INTO lib.autor (id_autor, primeiro_nome, sobrenome, nacionalidade) VALUES (%s, %s, %s,%s)",(id_autor, primeiro_nome, sobrenome, nacionalidade))
        conn.commit()

        return True
    except psycopg2.Error as e:
        print("Erro na inserção do autor:", e)
        return False
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()

def exec_insert_livro(id_livro, isbn, titulo, ano_publicacao, sinopse, id_autor, id_editora):
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # Insere um novo livro na tabela 
        cursor.execute("INSERT INTO lib.livro (id_livro, isbn, titulo, ano_publicacao, sinopse, id_autor, id_editora) VALUES (%s, %s, %s, %s, %s, %s, %s)",(id_livro, isbn, titulo, ano_publicacao, sinopse, id_autor, id_editora))
        conn.commit()

        return True
    except psycopg2.Error as e:
        print("Erro na inserção do livro:", e)
        return False
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()

def exec_insert_livro_premiacao(id_livro, id_premiacao, data_premiacao):
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # Insere novas informações na tabela de relacionamento 
        cursor.execute("INSERT INTO lib.livro_premiacao (id_livro, id_premiacao, data_premiacao) VALUES (%s, %s, %s)", (id_livro, id_premiacao, data_premiacao))
        conn.commit()

        return True
    except psycopg2.Error as e:
        print("Erro na inserção do livro:", e)
        return False
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()