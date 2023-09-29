import psycopg2
from connectbd import bd_config

'''def id_exists(cursor, id_livro):
    try:
        # Consulta para verificar se o ID existe na tabela
        cursor.execute("SELECT 1 FROM lib.livro WHERE id_livro = %s", (id_livro,))
        result = cursor.fetchone()
        return result is not None
    except psycopg2.Error as e:
        print("Erro na verificação de ID:", e)
        return False'''

def exec_delete_livro(id_livro):
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # Verifique se o ID existe na tabela antes de excluir
        #if not id_exists(cursor, id_livro):
        #    print("ID não encontrado na tabela.")
        #    return False

        # deleta um livro da tabela
        delete = ("DELETE FROM lib.livro WHERE id_livro = %s")

        cursor.execute(delete, (id_livro,))
        conn.commit()

        return True
    except psycopg2.Error as e:
        print("Erro na exclusão:", e)
        return False
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()

def exec_delete_autor(id_autor):
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # deleta um autor da tabela
        delete = ("DELETE FROM lib.autor WHERE id_autor = %s")

        cursor.execute(delete, (id_autor,))
        conn.commit()

        return True
    except psycopg2.Error as e:
        print("Erro na exclusão:", e)
        return False
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()

def exec_delete_livro_premiacao(id_livro, id_premiacao):
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # deleta um livro e a premiação da tabela de relacionamento
        delete = ("DELETE FROM lib.livro_premiacao WHERE id_autor = %s AND id_premiacao = %s")

        cursor.execute(delete, (id_livro, id_premiacao))
        conn.commit()

        return True
    except psycopg2.Error as e:
        print("Erro na exclusão:", e)
        return False
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()