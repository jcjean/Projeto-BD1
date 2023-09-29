import psycopg2
from connectbd import bd_config

def exec_select_livro(): 
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # consulta na tabela livro
        cursor.execute("SELECT * FROM lib.livro")
        results = cursor.fetchall()

        return results
    except psycopg2.Error as e:
        print("Erro na consulta:", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()

def exec_select_autor(): 
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # consulta na tabela autor
        cursor.execute("SELECT * FROM lib.autor")
        results = cursor.fetchall()

        return results
    except psycopg2.Error as e:
        print("Erro na consulta:", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()

def exec_select_livro_premiacao(): 
    cursor = None
    try:
        conn = psycopg2.connect(**bd_config)
        cursor = conn.cursor()

        # consulta na tabela livro_premiacao
        cursor.execute("SELECT * FROM lib.livro_premiacao")
        results = cursor.fetchall()

        return results
    except psycopg2.Error as e:
        print("Erro na consulta:", e)
        return None
    finally:
        if cursor:
            cursor.close()
        if 'conn' in locals():
            conn.close()