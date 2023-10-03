import psycopg2
from connectbd import bd_config

def exec_delete_livro(id_livro):
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # Deleta um livro da tabela
        cursor.execute("DELETE FROM lib.livro WHERE id_livro = %s", (id_livro,))
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

        # Deleta um autor da tabela
        cursor.execute("DELETE FROM lib.autor WHERE id_autor = %s", (id_autor,))
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

        # Deleta um livro e a premiação da tabela de relacionamento
        cursor.execute("DELETE FROM lib.livro_premiacao WHERE id_livro = %s AND id_premiacao = %s", (id_livro, id_premiacao))
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