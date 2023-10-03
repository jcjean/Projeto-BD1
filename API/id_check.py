import psycopg2
from connectbd import bd_config

def id_livro_exists(id_livro):
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # Verifique se o ID existe na tabela livro
        cursor.execute("SELECT id_livro FROM lib.livro WHERE id_livro = %s", (id_livro,))
        result = cursor.fetchone()

        return result is not None
    except psycopg2.Error as e:
        print("Erro na verificação de ID:", e)
        return False
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()

def id_autor_exists(id_autor):
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # Verifique se o ID existe na tabela autor
        cursor.execute("SELECT id_autor FROM lib.autor WHERE id_autor= %s", (id_autor,))
        result = cursor.fetchone()

        return result is not None
    except psycopg2.Error as e:
        print("Erro na verificação de ID:", e)
        return False
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()

def id_livro_premiacao_exists(id_livro, id_premiacao):
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # Verifique se o IDs existem na tabela de relacionamento
        cursor.execute("SELECT id_livro, id_premiacao FROM lib.livro_premiacao WHERE id_livro = %s AND id_premiacao= %s", (id_livro, id_premiacao))
        result = cursor.fetchone()

        return result is not None
    except psycopg2.Error as e:
        print("Erro na verificação de ID:", e)
        return False
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()